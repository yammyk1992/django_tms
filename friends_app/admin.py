from django.contrib import admin
from friends_app.models import Friends, FriendRequest


# Register your models here.
class FriendsAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    read_only_fields = ['user']

    class Meta:
        model = Friends


admin.site.register(Friends, FriendsAdmin)


class FriendsRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender', 'receiver']

