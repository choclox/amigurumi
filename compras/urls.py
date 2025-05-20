from django.urls import path
from .views import ActualizarCantidadItemView, EliminarItemView, OrdenView, CreateOrderProductView

urlpatterns = [
    path("mi_orden", OrdenView.as_view(), name="mi_orden"),
    path("agregar_producto", CreateOrderProductView.as_view(), name="agregar_producto"),
    path("actualizar_item/<int:item_id>", ActualizarCantidadItemView.as_view(), name="actualizar_item"),
    path("eliminar_item/<int:item_id>", EliminarItemView.as_view(), name="eliminar_item"),
]