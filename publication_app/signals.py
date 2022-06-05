from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# сигнал для сохранения создаваемого пользователя в базу и для редактирования пользователя
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return

    profile = Profile(user=instance)
    profile.save()