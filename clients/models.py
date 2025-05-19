from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# client
STATES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]

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
    adress = models.CharField(max_length=200,
                              null=True,
                              blank=True , 
                              verbose_name='Endereço',default='' )
    photo = models.ImageField(upload_to='media/', default='')
    state = models.CharField(max_length=2, choices=STATES, default='')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='atualizado em')
    class Meta:
        verbose_name ='Cliente'
        verbose_name_plural = 'Clientes'
    def __str__(self):
        return self.name
    
    
    
    
    