from django.urls import path
from .views import ProductosListView

urlpatterns = [
    path('', ProductosListView.as_view(), name='productos'),
]
