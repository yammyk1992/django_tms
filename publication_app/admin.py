from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# admin.site.unregister(User)


# регистрация модели Tag
# admin.site.register(Tag)
# @admin.register(Tag)
# class TegAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'tags': ('title',)}
#

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'avatar', 'phone', 'about', 'github_link')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # колонки в админке
    list_display = ('id', 'name')
    # поиск по заголовку
    search_fields = ('name',)
    list_display_links = ('id', 'name')


class PostImageAdmin(admin.StackedInline):
    model = ImagePost
    # readonly_fields = ('image_preview',)
    verbose_name = "Фотография к посту"
    list_display = ('id', 'image_preview', 'post_id')
    verbose_name_plural = "Фотографии к посту"
    ordering = ('-post_id',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_preview.short_description = 'Фото к посту'
    image_preview.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        PostImageAdmin,
    )
    list_display = ('id', 'created_at', 'title', 'is_public')
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at',)
    # изменять не заходя в пост
    list_editable = ('is_public',)
    # фильтровать по чем
    list_filter = ('is_public',)

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('title',)}