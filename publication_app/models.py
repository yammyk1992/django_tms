from django.db import models


# Create your models here.
class Post(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    title = models.CharField(max_length=256, unique=False, blank=False, null=False, verbose_name='Заголовок')
    nationality = models.TextField(max_length=256, unique=False, blank=False, null=False, verbose_name='Национальность')
    text = models.TextField(blank=False, null=False, verbose_name='Пост')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Пост'
        # для множественного числа
        verbose_name_plural = 'Великие футболисты'
        ordering = ['-created_at', 'title']
