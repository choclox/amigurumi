from django.urls import path
from .views import TejidosListView

urlpatterns = [
    path('tejidos/', TejidosListView.as_view(), name='tejidos_disponibles'),
]
