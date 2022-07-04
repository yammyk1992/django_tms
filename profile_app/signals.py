from django.contrib.auth.models import User
from django.db.models.signals import post_save

# сигнал для сохранения создаваемого пользователя в базу и для редактирования пользователя
from .models import Profile


# Определим сигналы, чтобы наша модель Profile автоматически обновлялась при создании/изменении данных модели User.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, *args, **kwargs):
#     if not created:
#         return
#
#     profile = Profile(user=instance)
#     profile.save()
