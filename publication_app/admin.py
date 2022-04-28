from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # колонки в админке
    list_display = ('id', 'created_at', 'title')
    # cортировка
    ordering = ('created_at', 'id',)
    readonly_fields = ('created_at',)
