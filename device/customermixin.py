from django.contrib.auth import get_user_model
from requests import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework import status
import logging

from user.models import User

logger = logging.getLogger(__name__)


class CreateCustomMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        logger.info(request.data)

        serializer = self.get_serializer(data=request.data)
        headers = self.get_success_headers(serializer.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = get_user_model()
        # if user.is_staff:
        # customer = User.objects.create_user(username=request., password=)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
