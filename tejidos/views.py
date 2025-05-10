from django.shortcuts import render
from django.views import generic
from .models import Tejido

# Create your views here.
class TejidosListView(generic.ListView):
    template_name = "tejidos_disponibles.html"
    model = Tejido
    context_object_name = "tejidos"