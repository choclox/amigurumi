from django.urls import path
from .views import PatronesListView

urlpatterns = [
    path('patrones/', PatronesListView.as_view(), name='patrones_disponibles'),
]
