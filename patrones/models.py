from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Patron(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='patrones/imagenes/')
    archivo = models.FileField(upload_to='patrones/pdfs/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.autor.es_vendedor:
            raise ValueError("El autor debe ser un vendedor para publicar un patrón.")
        super().save(*args, **kwargs)
