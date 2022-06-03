from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Post, Profile, Category, Tag


class ProfileInline(admin.StackedInline):
    model = Profile


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # inlines = [PostImageAdmin]
    # колонки в админке
    list_display = ('id', 'title', 'file', 'preview_photo', 'category', 'created_at', 'is_public')
    # cортировка
    ordering = ('id',)
    readonly_fields = ('created_at', 'tags')
    # поиск по заголовку
    search_fields = ('title',)
    # редактирование полей непосредственно в админке
    list_editable = ('is_public',)
    # фильтр списка статей
    list_filter = ('is_public', 'created_at')

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('title',)}

    def preview_photo(self, object):
        if object.file:
            return mark_safe(f"<img src='{object.file.url}' width=50")

    preview_photo.short_description = 'Превью'


# регистрация модели Tag
# admin.site.register(Tag)
@admin.register(Tag)
class TegAdmin(admin.ModelAdmin):
    prepopulated_fields = {'tags': ('title',)}


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # колонки в админке
    list_display = ('id', 'name')
    # поиск по заголовку
    search_fields = ('name',)
    list_display_links = ('id', 'name')

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('name',)}

# class PostImageAdmin(admin.TabularInline):
#     readonly_fields = ('image_preview',)
#     model = PostImage
#     extra = 4
#     verbose_name = "Фотография"
#     verbose_name_plural = "Фотографии"
#
#     def image_preview(self, obj):
#         # ex. the name of column is "images"
#         if obj.images:
#             return mark_safe(
#                 '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.images.url))
#         # ex. the name of column is "image"
#         if obj.image:
#             return mark_safe(
#                 '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
#         else:
#             return 'Нет картинки'
