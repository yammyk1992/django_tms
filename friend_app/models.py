from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Friend(models.Model):
    users_receivers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', null=True)

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Друзья'
        # для множественного числа
        verbose_name_plural = 'Друзья'

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
