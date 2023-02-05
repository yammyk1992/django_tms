from django.contrib import admin

# Register your models here.
from likes_app.models import PostLikes


@admin.register(PostLikes)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post_id', 'like')
    ordering = ('-created_time', '-id')
    readonly_fields = ('created_time',)
