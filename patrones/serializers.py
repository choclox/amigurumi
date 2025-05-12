from rest_framework.serializers import ModelSerializer
from .models import Patron


class PatronSerializer(ModelSerializer):
    class Meta:
        model = Patron
        fields = "__all__"