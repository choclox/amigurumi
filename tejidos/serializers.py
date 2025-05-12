from rest_framework.serializers import ModelSerializer
from .models import Tejido


class TejidoSerializer(ModelSerializer):
    class Meta:
        model = Tejido
        fields = "__all__"