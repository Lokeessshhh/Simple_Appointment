from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from reminders.models import Appointment
from reminders.utils import send_whatsapp_message
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Sends WhatsApp reminders for appointments within the next hour'

    def handle(self, *args, **options):
        now = timezone.now()
        one_hour_later = now + timedelta(hours=1)
        
        # Find appointments in the next 1 hour that haven't had a reminder sent
        upcoming_appointments = Appointment.objects.filter(
            appointment_datetime__gte=now,
            appointment_datetime__lte=one_hour_later,
            reminder_sent=False
        )
        
        count = upcoming_appointments.count()
        self.stdout.write(f"Found {count} upcoming appointments for reminders.")
        
        for appt in upcoming_appointments:
            try:
                msg_body = f"Reminder: Hi {appt.customer_name}, you have an appointment coming up at {appt.appointment_datetime.strftime('%I:%M %p')} today."
                send_whatsapp_message(appt.phone_number, msg_body)
                
                appt.reminder_sent = True
                appt.save()
                
                self.stdout.write(self.style.SUCCESS(f"Sent reminder to {appt.customer_name} ({appt.phone_number})"))
            except Exception as e:
                logger.error(f"Failed to send reminder to {appt.customer_name}: {e}")
                self.stdout.write(self.style.ERROR(f"Error sending to {appt.customer_name}: {e}"))
        
        self.stdout.write(self.style.SUCCESS("Reminder check complete."))
