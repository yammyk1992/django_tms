from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


# class PostImageAdmin(admin.TabularInline):
#     readonly_fields = ('image_preview',)
#     model = PostImage
#     extra = 4
#     verbose_name = "Фотография"
#     verbose_name_plural = "Фотографии"
#
#     def image_preview(self, obj):
<<<<<<< HEAD
#         # ex. the name of column is "images"
#         if obj.images:
#             return mark_safe(
#                 '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.images.url))
=======
#         # ex. the name of column is "image"
#         if obj.image:
#             return mark_safe(
#                 '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
>>>>>>> f1cc4431d0109fc20c497aae3b6fddbc0f2fb4de
#         else:
#             return 'Нет картинки'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # inlines = [PostImageAdmin]
    # колонки в админке
    list_display = ('id', 'title', 'nationality', 'preview_photo', 'created_at', 'is_public')
    # cортировка
    ordering = ('id',)
    readonly_fields = ('created_at',)
    # поиск по заголовку
    search_fields = ('title', 'nationality')
    # редактирование полей непосредственно в админке
    list_editable = ('is_public',)
    # фильтр списка статей
    list_filter = ('is_public', 'created_at')

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('title',)}

    def preview_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50")

    preview_photo.short_description = 'Превью'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # колонки в админке
    list_display = ('id', 'name')
    # поиск по заголовку
    search_fields = ('name',)
    list_display_links = ('id', 'name')

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('name',)}
