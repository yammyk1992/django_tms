from rest_framework import serializers

from friend_app.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
