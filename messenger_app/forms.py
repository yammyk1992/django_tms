from django.forms import ModelForm

from messenger_app.models import Messenger


class MessageForm(ModelForm):
    class Meta:
        model = Messenger
        fields = ['text']
        labels = {'text': ""}