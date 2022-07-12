from django.contrib import admin

# Register your models here.
from friend_app.models import Friend, FollowRequest


@admin.register(Friend)
class FriendshipAdmin(admin.ModelAdmin):
    """Вывод полей дружбы в админке"""
    list_display = ('user', 'user_invite', 'friendship_result', 'created_at')
    list_editable = ('friendship_result',)
    search_fields = ('user__username', 'user_invite__username')


@admin.register(FollowRequest)
class FollowAdmin(admin.ModelAdmin):
    """Вывод полей подписки в админке"""
    list_display = ('user', 'user_follow', 'created_at')
    search_fields = ('user__username', 'user_follow__username')
