from django.contrib import admin
from clients import models 
from clients.models import Client
# criar class no admin para melhorar a experiencia doa user admin
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
        list_display = ['name', 'phone', 'state', 'created_at', 'updated_at',]
        search_fields = ['name']
        list_filter = ['name']

