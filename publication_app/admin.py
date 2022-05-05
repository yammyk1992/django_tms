from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # колонки в админке
    list_display = ('id', 'title', 'nationality', 'created_at', 'image', 'is_public')
    # cортировка
    ordering = ('created_at', 'id',)
    readonly_fields = ('created_at',)
    # поиск по заголовку
    search_fields = ('title', 'nationality')
    # редактирование полей непосредственно в админке
    list_editable = ('is_public', )
    # фильтр списка статей
    list_filter = ('is_public', 'created_at')

