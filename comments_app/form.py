from django import forms
from comments_app.models import Comments


class CommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

    class Meta:
        model = Comments
        fields = ('body',)
