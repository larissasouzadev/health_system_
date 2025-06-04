from django.contrib import admin
from appointment import models
from appointment.models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'available_schedule', 'doctor','speciliaties','date','created_at','updated_at', 'hour']
    search_fields = ['name', 'doctor']
    list_filter = ['name', 'date']
# desabilita os horários ocupados
    def qs_list(self, request):
        pass