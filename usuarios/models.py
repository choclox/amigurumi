from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps  # Importación clave para evitar ciclos


class Usuario(AbstractUser):
    es_vendedor = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='usuarios/fotos_perfil', blank=True, null=True)

    def ha_comprado(self, patron):
        Compra = apps.get_model('compras', 'Compra')
        return Compra.objects.filter(comprador=self, patron=patron).exists()

    def get_productos_subidos(self):
        Tejido = apps.get_model('tejidos', 'Tejido')
        Patron = apps.get_model('patrones', 'Patron')
        return dict(
            tejidos=
            Tejido.objects.filter(autor=self),
            patrones=
            Patron.objects.filter(autor=self)
        )
    
    def get_productos_comprados(self):
        Orden = apps.get_model('compras', 'Orden')
        OrdenItem = apps.get_model('compras', 'OrdenItem')

        ordenes = Orden.objects.filter(user=self, is_active=False)
        items = OrdenItem.objects.filter(orden__in=ordenes)

        return [item.producto for item in items]
