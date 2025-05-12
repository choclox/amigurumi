from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView

from .models import Orden, OrdenItem
from .forms import OrderProductForm

class OrdenView(LoginRequiredMixin, TemplateView):
    template_name = "mi_orden.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden = Orden.objects.filter(user=self.request.user, is_active=True).first()
        context["orden"] = orden
        return context


class CreateOrderProductView(LoginRequiredMixin, FormView):
    form_class = OrderProductForm
    template_name = "crear_orden.html"
    success_url = reverse_lazy("mi_orden")

    def form_valid(self, form):
        orden, _ = Orden.objects.get_or_create(user=self.request.user, is_active=True)

        content_type_str = form.cleaned_data["content_type"]
        object_id = form.cleaned_data["object_id"]

        content_type = ContentType.objects.get(model=content_type_str)
        producto = content_type.get_object_for_this_type(id=object_id)

        item_existente = OrdenItem.objects.filter(
            orden=orden, content_type=content_type, object_id=object_id
        ).first()

        if item_existente:
            item_existente.cantidad += 1
            item_existente.save()
        else:
            OrdenItem.objects.create(
                orden=orden,
                content_type=content_type,
                object_id=object_id,
                cantidad=1,
            )

        return super().form_valid(form)

