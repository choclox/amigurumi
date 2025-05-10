from django.db import models
from django.core.exceptions import ValidationError
from usuarios.models import Usuario
from patrones.models import Patron

class Tejido(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tejidos/imagenes/')
    autor = models.ForeignKey(Usuario, related_name='tejidos', on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, related_name='tejidos', on_delete=models.SET_NULL, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.autor.es_vendedor:
            raise ValidationError("Solo los vendedores pueden publicar productos.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre