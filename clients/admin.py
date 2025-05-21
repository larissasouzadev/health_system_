from django.contrib import admin
from clients import models 
from clients.models import Client

# Register your models here.
admin.site.register(Client)