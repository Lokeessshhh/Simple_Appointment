from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .utils import send_whatsapp_message
from datetime import datetime
from django.utils.timezone import make_aware
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dt_str = request.POST.get('datetime')
        
        try:
            # HTML5 datetime-local returns 'YYYY-MM-DDTHH:MM'
            dt_obj = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M')
            dt_obj = make_aware(dt_obj)
            
            appointment = Appointment.objects.create(
                customer_name=name,
                phone_number=phone,
                appointment_datetime=dt_obj
            )
            
            # Send WhatsApp confirmation
            try:
                msg_body = f"Hi {name}, your appointment is confirmed for {dt_obj.strftime('%B %d, %Y at %I:%M %p')}."
                send_whatsapp_message(phone, msg_body)
                appointment.confirmation_sent = True
                appointment.save()
                messages.success(request, f"Appointment saved and confirmation sent to {phone}!")
            except Exception as e:
                logger.error(f"Twilio error: {e}")
                messages.warning(request, f"Appointment saved, but WhatsApp confirmation failed: {str(e)}")
            
            return redirect('index')
            
        except ValueError as e:
            messages.error(request, f"Invalid date format: {e}")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    appointments = Appointment.objects.all()
    return render(request, 'reminders/index.html', {'appointments': appointments})
