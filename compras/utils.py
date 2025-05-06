from django.core.exceptions import ValidationError
from .models import Compra

def comprar_patron(usuario, patron):
    """
    Función para realizar la compra de un patrón por un usuario.
    """
    if patron.autor == usuario:
        raise ValidationError("No puedes comprar tu propio patrón.")
    
    if Compra.objects.filter(comprador=usuario, patron=patron).exists():
        raise ValidationError("Ya has comprado este patrón.")

    compra = Compra.objects.create(comprador=usuario, patron=patron)
    return compra

