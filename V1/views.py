from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import CustomerSerializer
from .models import Customer


# Create your views here.
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
