from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    title = models.CharField(max_length=256, unique=False, blank=False, null=False, verbose_name='Заголовок')
    nationality = models.TextField(max_length=256, unique=False, blank=False, null=False, verbose_name='Национальность')
    content = models.TextField(blank=True, null=False, verbose_name='Пост')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    # для вывода в режиме shell терминал заголовков объектов из базы данных

    def __str__(self):
        return self.title

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Пост'
        # для множественного числа
        verbose_name_plural = 'Спортсмены'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Категория'
        # для множественного числа
        verbose_name_plural = 'Категории'
        ordering = ['id']