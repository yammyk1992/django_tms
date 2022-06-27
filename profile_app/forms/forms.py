from django import forms
from django.contrib.auth.models import User

from profile_app.models import Profile


class UserEditForm(forms.ModelForm):
    """Класс форма редактирование User"""
    first_name = forms.CharField(
        label='Имя'
    )
    last_name = forms.CharField(
        label='Фамилия'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    """Класс форма редактирование Profile"""
    about = forms.TextInput()

    class Meta:
        model = Profile
        fields = ['about', 'photo']
