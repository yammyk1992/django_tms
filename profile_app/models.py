from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_model', verbose_name='Пользователь')
    avatar = models.ImageField(blank=True, null=True)
