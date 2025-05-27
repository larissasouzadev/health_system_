from django.contrib import admin
from appointment import models
from appointment.models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'appointment', 'doctor','speciliaties','date','created_at','updated_at' ]
    search_fields = ['name', 'appointment']
    list_filter = ['name', 'date']


