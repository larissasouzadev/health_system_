from django.db import models
from clients.models import Client
from doctors.models import Doctors
from appointment.models import Appointment
class Schedule(models.Model):
    client = models.ForeignKey(Client, 
                      on_delete=models.CASCADE,
                      verbose_name='cliente')
    doctor = models.ForeignKey(Doctors,
                               on_delete=models.CASCADE,
                               verbose_name='médico'
                               )
    date = models.ForeignKey(Appointment,
                             on_delete=models.PROTECT,
                             verbose_name='data',
                             related_name='date_schedule')
    
    hour = models.ForeignKey(Appointment,
                             on_delete=models.PROTECT,
                             verbose_name='horário',
                             related_name='hour_schedule',
                             
    )
    carried_out = models.BooleanField(default=False,
                                      verbose_name='realizada')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='criado em ')
    updated_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='atualizado em')

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"

    def __str__(self):
        return f"{self.client} - {self.doctor} - {self.date} {self.hour}"
