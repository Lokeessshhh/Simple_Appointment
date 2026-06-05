from django.db import models

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    appointment_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_sent = models.BooleanField(default=False)
    reminder_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-appointment_datetime']

    def __str__(self):
        return f"{self.customer_name} - {self.appointment_datetime}"
