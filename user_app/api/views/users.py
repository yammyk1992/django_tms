from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from user_app.api.serializers.users import UserSerializer
from user_app.models import User


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
