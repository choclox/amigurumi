from django.shortcuts import render
from django.views import generic
from .models import Patron

class PatronesListView(generic.ListView):
    template_name = "patrones_disponibles.html"
    model = Patron
    context_object_name = "patrones"
