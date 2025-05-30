from django.db import models

from clients.models import Client
from doctors.models import Doctors


# o appointment é responsável pelo agendamento consulta marcada entre médico e paciente


# Create your models here.
MEDICAL_SPECIALTIES = [
    ('cardiologia', 'Cardiologia'),
    ('cirurgia_geral', 'Cirurgia Geral'),
    ('cirurgia_plastica', 'Cirurgia Plástica'),
    ('cirurgia_vascular', 'Cirurgia Vascular'),
    ('clinica_medica', 'Clínica Médica'),
    ('dermatologia', 'Dermatologia'),
    ('endocrinologia', 'Endocrinologia'),
    ('ginecologia_e_obstetricia', 'Ginecologia e Obstetrícia'),
    ('homeopatia', 'Homeopatia'),
    ('infectologia', 'Infectologia'),
    ('medicina_de_familia_e_comunidade', 'Medicina de Família e Comunidade'),
    ('medicina_do_trabalho', 'Medicina do Trabalho'),
    ('medicina_intensiva', 'Medicina Intensiva'),
    ('nefrologia', 'Nefrologia'),
    ('neurologia', 'Neurologia'),
    ('nutrologia', 'Nutrologia'),
    ('oftalmologia', 'Oftalmologia'),
    ('ortopedia_e_traumatologia', 'Ortopedia e Traumatologia'),
    ('otorrinolaringologia', 'Otorrinolaringologia'),
    ('pediatria', 'Pediatria'),
    ('pneumologia', 'Pneumologia'),
    ('psiquiatria', 'Psiquiatria'),
    ('radiologia_e_diagnostico_por_imagem', 'Radiologia e Diagnóstico por Imagem'),
    ('reumatologia', 'Reumatologia'),
    ('urologia', 'Urologia'),
]


class Appointment (models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Client,
                             on_delete=models.CASCADE,
                             verbose_name='nome')
    appointment = models.CharField( max_length=50, 
                                   default='',
                                   verbose_name='consulta')
    doctor = models.ForeignKey(Doctors,
                               on_delete=models.CASCADE,
                               verbose_name='médico', 
                               blank=True, 
                               null=True)
    speciliaties = models.CharField(max_length=50, 
                                    choices=MEDICAL_SPECIALTIES, verbose_name='especialidade')
    date = models.DateTimeField(verbose_name='data')
    observations = models.TextField(max_length=500,
                                    null=True,
                                    blank=True,
                                    verbose_name='observações',
                                    default='')
    is_available = models.BooleanField(verbose_name='é avaliado')
    carried_out = models.BooleanField(verbose_name='realizada')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='data de criação')
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name='data de atualização')
    
class Meta:
        verbose_name = ("Agendamento")
        verbose_name_plural = ("Appointments")

def __str__(self):
        return self.name
