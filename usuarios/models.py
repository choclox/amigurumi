from django.db import models
from django.contrib.auth.models import AbstractUser
from compras.models import Compra
from patrones.models import Patron

# Create your models here.
class Usuario(AbstractUser):
    # Campos adicionales
    es_vendedor = models.BooleanField(default=False)
    
    def ha_comprado(self, patron):
        return Compra.objects.filter(comprador=self, patron=patron).exists()

    def patrones_comprados(self):
        return Compra.objects.filter(comprador=self).values_list('patron', flat=True)
    
    def patrones_subidos(self):
        return Patron.objects.filter(vendedor=self)
    
    