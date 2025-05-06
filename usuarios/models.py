from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps  # Importación clave para evitar ciclos


class Usuario(AbstractUser):
    es_vendedor = models.BooleanField(default=False)

    def ha_comprado(self, patron):
        Compra = apps.get_model('compras', 'Compra')
        return Compra.objects.filter(comprador=self, patron=patron).exists()

    def obtener_patrones_comprados(self):
        Compra = apps.get_model('compras', 'Compra')
        return Compra.objects.filter(comprador=self).values_list('patron_id', flat=True)

    def obtener_patrones_subidos(self):
        Patron = apps.get_model('patrones', 'Patron')
        return Patron.objects.filter(autor=self).values_list('id', flat=True)

    def obtener_patrones_disponibles(self):
        Patron = apps.get_model('patrones', 'Patron')
        ids_comprados = self.obtener_patrones_comprados()
        ids_subidos = self.obtener_patrones_subidos()
        return Patron.objects.exclude(id__in=ids_comprados).exclude(id__in=ids_subidos).distinct()

