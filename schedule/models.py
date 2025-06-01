from django.db import models
from clients.models import Client
from doctors.models import Doctors

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, 
                               on_delete=models.CASCADE,
                               verbose_name='cliente')
    doctor = models.ForeignKey(Doctors,
                               on_delete=models.CASCADE,
                               verbose_name='médico'
                               )
    date = models.DateField(verbose_name='data')
    available_schedule = models.BooleanField(default=False,
                                             verbose_name="horário disponível")
    hour = models.TimeField(verbose_name='horário')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='criado em ')
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='atualizado em')

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"

    def __str__(self):
        return f"{self.client} - {self.doctor} - {self.date} {self.hour}"
