from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_request')
    user_invite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship')
    friendship_result = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     """Информационная строка кто с кем дружит"""
    #     return f"User #{self.user} and user #{self.user_invite} friendship requested: {self.friendship_result}"

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Друзья'
        # для множественного числа
        verbose_name_plural = 'Друзья'
        unique_together = ('user', 'user_invite')


class FollowRequest(models.Model):
    """Модель подписки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_request')
    user_follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Информационная строка кто на кого подписан"""
        return f"User #{self.user} follows #{self.user_follow}"

    # class Meta:
    #     """Создаём уникальные поля"""
    #     unique_together = ('user', 'user_follow')

    # @classmethod
    # def make_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(
    #         current_user=current_user
    #     )
    #     friend.users.add(new_friend)
    #
    # @classmethod
    # def lose_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(
    #         current_user=current_user
    #     )
    #     friend.users.remove(new_friend)
