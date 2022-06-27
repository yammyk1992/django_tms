from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from media_app.models import Media
from tags_app.models import Tag


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Слаг')
    content = models.TextField(blank=True, null=False, verbose_name='Пост')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории', null=True)

    tag = models.ManyToManyField(Tag, blank=True, related_name='tag_post')

    # для вывода в режиме shell терминал заголовков объектов из базы данных

    def __str__(self):
        return self.title

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Пост'
        # для множественного числа
        verbose_name_plural = 'Посты'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image_posts')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Фото')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def get_absolute_url(self):
    #     return f'/image{self.id}'

    class Meta:
        verbose_name = 'Фотография поста'
        verbose_name_plural = 'Фотограции постов'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Категория'
        # для множественного числа
        verbose_name_plural = 'Категории'
        ordering = ['id']
