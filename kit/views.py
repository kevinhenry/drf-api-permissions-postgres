from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from kit.permissions import IsOwnerOrReadOnly
from .serializers import KitSerializer
from .models import Kit

# Create your views here.
class KitList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

class KitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,) 
    queryset = Kit.objects.all()
    serializer_class = KitSerializer
