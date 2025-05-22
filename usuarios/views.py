from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .forms import RegistroForm
from .models import Usuario

from compras.models import Orden

class RegisterView(generic.CreateView):
    form_class = RegistroForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class PerfilView(generic.TemplateView):
    template_name = "perfil_usuario.html"

    def get(self, request, user_name, *args, **kwargs):
        self.perfil_usuario = get_object_or_404(Usuario, username=user_name)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_actual = self.request.user

        context["usuario"] = self.perfil_usuario
        context["compras"] = self.perfil_usuario.get_productos_comprados()
        context["es_dueño"] = usuario_actual == self.perfil_usuario
        context["publicaciones"] = self.perfil_usuario.get_productos_subidos()
        context["pedidos"] = self.perfil_usuario.orden_set.filter(is_active=False)
        return context
    