from django.db import models
from usuarios.models import Usuario
from patrones.models import Patron

# Create your models here.
class Compra(models.Model):
    comprador = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    patron = models.ForeignKey( Patron, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['comprador', 'patron'], name='compra_unica_por_usuario_patron')
        ]