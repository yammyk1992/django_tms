from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# сигнал для сохранения создаваемого пользователя в базу и для редактирования пользователя
from .models import Profile


# Определим сигналы, чтобы наша модель Profile автоматически обновлялась при создании/изменении данных модели User.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, *args, **kwargs):
#     if not created:
#         return
#
#     profile = Profile(user=instance)
#     profile.save()


