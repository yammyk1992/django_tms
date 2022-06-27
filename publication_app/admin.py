from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, ImagePost


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

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('name',)}


class PostImageAdmin(admin.StackedInline):
    model = ImagePost
    readonly_fields = ('image_preview',)
    verbose_name = "Фотография к посту"
    list_display = ('id', 'image_preview', 'post_id')
    verbose_name_plural = "Фотографии к посту"

    def image_preview(self, object):
        # ex. the name of column is "images"
        if object.file:
            return mark_safe('<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(object.image.image.url))
        else:
            return 'Нет картинки'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        PostImageAdmin,
    )
    # колонки в админке
    list_display = ('id', 'title', 'category', 'file', 'created_at', 'is_public')
    # cортировка
    ordering = ('id',)
    readonly_fields = ('created_at',)
    # поиск по заголовку
    search_fields = ('title',)
    # редактирование полей непосредственно в админке
    list_editable = ('is_public', 'file')
    # фильтр списка статей
    list_filter = ('is_public', 'created_at')

    # заполняется слаг автоматически
    prepopulated_fields = {'slug': ('title',)}

    def preview_photo(self, object):
        if object.file:
            return mark_safe(f"<img src='{object.file.file.url}' width=50")

    preview_photo.short_description = 'Превью картинки'
