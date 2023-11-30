from rest_framework.serializers import ModelSerializer
from main.models import Salom


class SalomSerializers(ModelSerializer):
    class Meta:
        model = Salom
        fields = '__all__'