from rest_framework import serializers

from friend_app.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['users_receivers', ]
        read_only_fields = ['current_user']

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='current_user',
    )
