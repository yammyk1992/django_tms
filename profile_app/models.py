from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_model',
                                verbose_name='Пользователь')
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9, 15}$')], max_length=17, blank=True,
                             null=True, verbose_name='Номер телефона')
    about = models.TextField(max_length=4096, verbose_name='О себе', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub')
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
#
#     def get_friends(self):
#         return self.friends.all()
#
#     def get_friends_no(self):
#         return self.friends.all().count
#
#
# STATUS_CHOICES = (
#     ('send', 'send'),
#     ('accepted', 'accepted'),
# )
