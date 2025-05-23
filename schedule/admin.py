from django.contrib import admin
from schedule import models
from schedule.models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'appointment', 'doctor','speciliaties','date','created_at','updated_at' ]
    search_fields = ['name', 'appointment']
    list_filter = ['name', 'date']
