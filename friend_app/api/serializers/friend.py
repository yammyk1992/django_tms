from rest_framework import serializers

from friend_app.models import Friend, FollowRequest


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
        # read_only_fields = ['user', 'friendship_result', ]

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )


class FollowSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер подписки"""

    class Meta:
        model = FollowRequest
        fields = '__all__'
        # read_only_fields = ['user', ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )
