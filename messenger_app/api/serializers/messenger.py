from rest_framework import serializers

from messenger_app.models import Messenger


class MessengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messenger
        fields = "__all__"
        read_only_fields = ['sender']

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )