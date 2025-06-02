from django.contrib import admin
from . import models
# Register your models here.
from .models import Schedule
@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    list_display = ['client', 'doctor', 'date','hour',]
    list_filter = [ 'doctor', 'date']


# add verbose-NAME aos campos do schedule