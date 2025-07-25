# Generated by Django 5.2.1 on 2025-05-13 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='CPF')),
                ('phone', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='atualizado em')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
            ],
        ),
    ]
