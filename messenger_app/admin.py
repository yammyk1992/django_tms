from django.contrib import admin


# Register your models here.
from messenger_app.models import Messenger


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'recipient', ]
    list_display = ['sender', 'recipient', ]
    search_fields = ['sender', 'recipient', ]

    class Meta:
        model = Messenger
