from django.db import models
from clients.models import Client
from doctors.models import Doctors

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return f"{self.client} - {self.doctor} - {self.date} {self.hour}"
