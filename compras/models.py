from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Orden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"Orden #{self.id} de {self.user.username}"

    def get_total(self):
        return sum(item.cantidad * item.producto.precio for item in self.items.all())


class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    producto = GenericForeignKey("content_type", "object_id")
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('orden', 'content_type', 'object_id')

    def __str__(self):
        return f"{self.cantidad} x {self.producto}"
    
    def subtotal(self):
        return self.cantidad * self.producto.precio


