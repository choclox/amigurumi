from django.shortcuts import render
from .models import Patron

def patrones_disponibles_view(request):
    patrones = Patron.objects.all()  # Más adelante filtraremos por usuario
    context = {
        'patrones': patrones
    }
    return render(request, 'patrones_disponibles.html', context)
