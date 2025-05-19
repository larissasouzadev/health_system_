from django.db import models
from django.core.validators import  RegexValidator

# doctors

crm_validator = RegexValidator(
    regex=r'^\d{4,6}/[A-Z]{2}$',
    message='O CRM deve estar no formato 123456/SP (4 a 6 dígitos, seguido da sigla do estado).'
)
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

class Doctors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, 
                            default='',
                            unique=True,
                            verbose_name='Nome')
    crm = models.CharField(max_length=9, 
                           validators = [crm_validator],
                           unique=True)
    specialties = models.CharField(max_length=50,
                                   choices=MEDICAL_SPECIALTIES)
    photo = models.ImageField(upload_to='media/')
    description = models.TextField(max_length=500,
                                   null=True,
                                   blank=True,
                                   default='', 
                                   verbose_name='Descrição',
                                   )         
    is_acctivate = models.BooleanField(default=True,
                                       verbose_name='está disponivel')
    created_at = models.DateTimeField(auto_now_add= True)
    upadated_at= models.DateTimeField( auto_now_add=True)
    class Meta():
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        
    def __str__(self):
        return self.name