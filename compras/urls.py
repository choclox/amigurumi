from django.urls import path
from .views import OrdenView, CreateOrderProductView

urlpatterns = [
    path("mi_orden", OrdenView.as_view(), name="mi_orden"),
    path("agregar_producto", CreateOrderProductView.as_view(), name="agregar_producto"),
]