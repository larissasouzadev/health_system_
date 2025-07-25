# Generated by Django 5.2.1 on 2025-06-02 03:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='Nome')),
                ('crm', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='O CRM deve estar no formato 123456/SP (4 a 6 dígitos, seguido da sigla do estado).', regex='^\\d{4,6}/[A-Z]{2}$')])),
                ('specialties', models.CharField(choices=[('cardiologia', 'Cardiologia'), ('cirurgia_geral', 'Cirurgia Geral'), ('cirurgia_plastica', 'Cirurgia Plástica'), ('cirurgia_vascular', 'Cirurgia Vascular'), ('clinica_medica', 'Clínica Médica'), ('dermatologia', 'Dermatologia'), ('endocrinologia', 'Endocrinologia'), ('ginecologia_e_obstetricia', 'Ginecologia e Obstetrícia'), ('homeopatia', 'Homeopatia'), ('infectologia', 'Infectologia'), ('medicina_de_familia_e_comunidade', 'Medicina de Família e Comunidade'), ('medicina_do_trabalho', 'Medicina do Trabalho'), ('medicina_intensiva', 'Medicina Intensiva'), ('nefrologia', 'Nefrologia'), ('neurologia', 'Neurologia'), ('nutrologia', 'Nutrologia'), ('oftalmologia', 'Oftalmologia'), ('ortopedia_e_traumatologia', 'Ortopedia e Traumatologia'), ('otorrinolaringologia', 'Otorrinolaringologia'), ('pediatria', 'Pediatria'), ('pneumologia', 'Pneumologia'), ('psiquiatria', 'Psiquiatria'), ('radiologia_e_diagnostico_por_imagem', 'Radiologia e Diagnóstico por Imagem'), ('reumatologia', 'Reumatologia'), ('urologia', 'Urologia')], max_length=50)),
                ('photo', models.ImageField(upload_to='media/')),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='Descrição')),
                ('is_acctivate', models.BooleanField(default=True, verbose_name='está disponivel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
