from rest_framework import generics
from main.models import Salom
from main.serializers import SalomSerializers


class SalomView(generics.CreateAPIView):
    queryset = Salom.objects.all()
    serializer_class = SalomSerializers
    http_method_names = ['post']