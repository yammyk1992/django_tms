from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, null=False, verbose_name='Пост')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    tags = models.ManyToManyField('Tag', related_name='tags', null=True, blank=True)

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
        return reverse('post', kwargs={'post_slug': self.slug})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9, 15}$')], max_length=17, blank=True,
                             null=True, verbose_name='Номер телефона')
    about = models.TextField(max_length=4096, verbose_name='О себе', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub')

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Профиль'
        # для множественного числа
        verbose_name_plural = 'Профили'
        ordering = ['id']


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


class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # class PostImage(models.Model):
    #     # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    #     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    #     images = models.ImageField(null=True, blank=True, verbose_name='Фото')
    #     image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    #     title = models.CharField(max_length=256)
    #
    #     def __str__(self):
    #         return self.post

