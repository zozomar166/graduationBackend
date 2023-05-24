from django.contrib.auth.backends import ModelBackend
from .models import Customer


class CustomerAuthBackend(ModelBackend):
    def authenticate(self, request, user=None, **kwargs):
        try:
            customer = Customer.objects.get(user=user)
            if customer.active:
                return customer
        except Customer.DoesNotExist:
            return None
