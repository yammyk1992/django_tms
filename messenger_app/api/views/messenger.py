from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from messenger_app.api.serializers.messenger import MessengerSerializer
from messenger_app.models import Messenger


class MessengerView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = MessengerSerializer
    queryset = Messenger.objects.all()
