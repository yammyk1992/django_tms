import sender as sender
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

from profile_app.models import Profile


class Friends(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='username')
    friends = models.ManyToManyField(Profile, blank=True, related_name='friends')

    def __str__(self):
        return self.user.name

    def add_friend(self, account):
        """
        Добавление нового друга
        """
        if account not in self.friends.all():
            self.friends.add(account)
            self.save()

    def remove_friend(self, account):
        """
        Удаляем друга
        """
        if account not in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, delete_friend):
        """
        Логика удаление кого-либо из друзей
        """
        remover_friends = self
        remover_friends.remove_friend(delete_friend)
        friends_list = Friends.objects.get(user=delete_friend)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """
        Логика взаимных друзей
        """
        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    """
    Запрос в друзья состоит из двух главных частей:
        1. Отправитель:
            - Аккаунт поосылает запрос в друзья
        2. Получатель:
            - Аккаунт получает запрос в друзья
    """
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    is_active = models.BooleanField(blank=True, null=False, default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.name

    def accept(self):
        """
        Принимаем запрос на друга и обновляем список друзей
        """
        receiver_friend_list = Friends.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friends_list = Friends.objects.get(user=self.sender)
            if sender_friends_list:
                sender_friends_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """
        Отклоняем запрас на дружбу когда настройки поля 'is_active' = False
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
         Выходим из зупроса в друзья когда настройки поля 'is_active' = False
        """
        self.is_active = False
        self.save()



