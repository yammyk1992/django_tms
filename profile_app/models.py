from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='Пользователь')
    photo = models.ImageField(blank=True, null=True)
    about = models.TextField(max_length=4096, verbose_name='О себе', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub')
    # friends = models.ManyToManyField(User, related_name='friends', blank=True)

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Профиль'
        # для множественного числа
        verbose_name_plural = 'Профили'
        ordering = ['id']
#
#     def get_friends(self):
#         return self.friends.all()
#
#     def get_friends_no(self):
#         return self.friends.all().count
