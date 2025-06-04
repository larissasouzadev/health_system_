from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from appointment.models import Appointment

@receiver(post_save, sender=Appointment)
def updated_available_status(sender, instance, created, **kwargs):
    """Atualiza automaticamente a disponibilidade do horário"""
    if created:  # Se for um novo agendamento
        instance.available_schedule = False
        instance.save()
   
   
   
   
   
   
   
    # if hasattr(instance, 'available_schedule') and instance.available_schedule:
    #     instance.available_schedule.available = (instance.hour is None)
    #     instance.available_schedule.save()
      
      
    #   arrumar signals e add hour a display list