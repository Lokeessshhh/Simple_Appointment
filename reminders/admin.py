from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'appointment_datetime', 'confirmation_sent', 'reminder_sent')
    list_filter = ('confirmation_sent', 'reminder_sent', 'appointment_datetime')
    search_fields = ('customer_name', 'phone_number')
    readonly_fields = ('created_at',)
