from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='Пользователь')
    photo = models.ImageField(blank=True, null=True)
    about = models.TextField(max_length=4096, verbose_name='О себе', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub')

    # friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return f'Профиль для  {self.user.username}'

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Профиль'
        # для множественного числа
        verbose_name_plural = 'Профили'
        ordering = ['id']
