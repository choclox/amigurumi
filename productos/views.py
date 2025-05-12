from django.views.generic import TemplateView
from patrones.models import Patron
from tejidos.models import Tejido

class ProductosListView(TemplateView):
    template_name = "lista_productos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patrones'] = Patron.objects.all()
        context['tejidos'] = Tejido.objects.all()
        return context