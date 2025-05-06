from django.urls import path
from . import views

urlpatterns = [
    path('', views.patrones_disponibles_view, name='patrones_disponibles'),
]
