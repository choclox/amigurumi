from django import forms
from django.contrib.contenttypes.models import ContentType

class OrderProductForm(forms.Form):
    PRODUCT_CHOICES = [
        ('patron', 'Patrón'),
        ('tejido', 'Tejido'),
    ]

    content_type = forms.ChoiceField(choices=PRODUCT_CHOICES, label="Tipo de producto")
    object_id = forms.IntegerField(label="ID del producto")

    def form_invalid(self, form):
        print("Formulario inválido:", form.errors)
        return super().form_invalid(form)
