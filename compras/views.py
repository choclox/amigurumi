from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from django.views import View
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView

from .models import Orden, OrdenItem
from .forms import OrderProductForm

class OrdenView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the current active order of the logged-in user.
    Inherits from:
        LoginRequiredMixin: Ensures that only authenticated users can access this view.
        TemplateView: Renders the specified template with the provided context.
    Attributes:
        template_name (str): The name of the template to render ("mi_orden.html").
    Methods:
        get_context_data(self, **kwargs):
            Adds the active order (`Orden`) for the current user to the context under the key "orden".
            Returns the context dictionary for template rendering.
    """
    template_name = "mi_orden.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden = Orden.objects.filter(user=self.request.user, is_active=True).first()
        context["orden"] = orden
        return context


class CreateOrderProductView(LoginRequiredMixin, FormView):
    """
    View to handle the creation of an order item for the currently authenticated user.
    This view uses a form to receive the content type and object ID of the product to be added to the user's active order.
    If the product already exists in the order, its quantity is incremented by one. Otherwise, a new order item is created.
    Upon successful form submission, the user is redirected to the 'mi_orden' page.
    Attributes:
        form_class (OrderProductForm): The form used to add a product to the order.
        template_name (str): The template rendered for the form.
        success_url (str): The URL to redirect to after successful form submission.
    Methods:
        form_valid(form):
            Handles the logic for adding or updating an order item based on the submitted form data.
    """
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

class ActualizarCantidadItemView(LoginRequiredMixin, View):
    """
    View to handle updating the quantity of an item in the user's active order.
    This view allows authenticated users to increase or decrease the quantity of a specific item
    in their current active order. If the quantity is decreased below 1, the item is removed from the order.
    Methods:
        get(request, item_id):
            Handles GET requests to either increase or decrease the quantity of an order item.
            - If 'accion' is 'aumentar', increments the item's quantity by 1.
            - If 'accion' is 'disminuir', decrements the item's quantity by 1, or deletes the item if quantity reaches 0.
            Redirects to the 'mi_orden' view after processing.
    """
    def get(self,request,item_id):
        item = get_object_or_404(OrdenItem, id=item_id, orden__user=request.user, orden__is_active=True)
        accion = request.GET.get("accion")

        if accion == "aumentar":
            item.cantidad += 1
            item.save()
        
        elif accion == "disminuir":
            if item.cantidad > 1:
                item.cantidad -= 1
                item.save()
            else:
                item.delete()
        
        return redirect("mi_orden")
    
class EliminarItemView(LoginRequiredMixin, View):
    """
    View to handle the deletion of an item from the user's active order.

    This view requires the user to be authenticated. When accessed via a GET request with a specific item ID,
    it retrieves the corresponding `OrdenItem` object that belongs to the current user's active order.
    If the item exists, it is deleted from the order. After deletion, the user is redirected to the "mi_orden" page.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item to be deleted.
    Returns:
        HttpResponseRedirect: Redirects the user to the "mi_orden" page after successful deletion.
    Raises:
        Http404: If the specified item does not exist or does not belong to the user's active order.
    """
    def get(self,request,item_id):
        item = get_object_or_404(OrdenItem, id=item_id, orden__user=request.user, orden__is_active=True)
        item.delete()
        return redirect("mi_orden")
