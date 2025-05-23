from django.contrib import admin
from doctors import models
from doctors.models import Doctors
# Register your models here.
@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialties', 'created_at','updated_at']
    search_fields = ['name', 'specialties']
    list_filter = ['name', 'is_acctivate']