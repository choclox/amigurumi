from .forms import RegistroForm
from django.views import generic
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    form_class = RegistroForm
    template_name = "register.html"
    success_url = reverse_lazy("login")