from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# client
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, 
        blank=True,
        null=True,
        related_name='clients',
        verbose_name='Cliente',
    )
    name= models.CharField(max_length=100, default='', verbose_name='Nome')
    cpf = models.CharField(max_length=15,
                           blank=True,
                           null=True,
                           verbose_name='CPF' ,
                           default=''
                           )
    phone = models.CharField(max_length=15,
                             null=True,
                             blank=True,
                             verbose_name='Telefone',
                             default='')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='atualizado em')
    def __str__(self):
        return self.user