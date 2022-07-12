from django.contrib.auth.models import User
from rest_framework import serializers

from profile_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo', 'github_link', 'about']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
