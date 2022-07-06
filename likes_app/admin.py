from django.contrib import admin

# Register your models here.
from likes_app.models import Likes


@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id',)
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)
