from django.db import models
from doctors.models import Doctors
# Create your models here.
class Slots(models.Model):
    doctor = models.ForeignKey(
        Doctors,
        on_delete=models.PROTECT,
        related_name='doctors_slots'
    )
    hour = models.TimeField(
        verbose_name='hora',
        default='00:00'
    )
    date = models.DateField(verbose_name='data',
                                default='')
    is_occupied = models.BooleanField()
     
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='data de criação')
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name='data de atualização')
    
class Meta:
        unique_together = ('doctor', 'date','hour')
        verbose_name = ("Vagas")
        verbose_name_plural = ("Slots")

def __str__(self):
        return self.doctor


     