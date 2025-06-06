from django.contrib import admin
from slots.models import Slots
# Register your models here.
@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
    list_display = ['hour', 'date', 'doctor', 'is_occupied']
    search_fields = [ 'doctor']
    list_filter = ['date']
   
# desabilita os horários ocupados