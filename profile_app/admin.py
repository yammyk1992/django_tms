# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'about', 'github_link')

    def preview_photo(self, object):
        if object.file:
            return mark_safe(f"<img src='{object.avatar.avatar.url}' width=50")

    preview_photo.short_description = 'Превью'
