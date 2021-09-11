from rest_framework import generics
from .serializers import KitSerializer
from .models import Kit

# Create your views here.
class KitList(generics.ListCreateAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
