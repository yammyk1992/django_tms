from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User


# создание моделей не связанных с БД
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок')
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 68, 'rows': 10}), label='Контент')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории',
#                                       empty_label='Категория не выбрана')

# создание моделей связанных с БД
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'is_public', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 68, 'rows': 10}),
        }

    # создаём собственную валидацию данных по заголовку
    def clean_title(self):
        # метод
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(RegisterUserForm, self).save(commit=False)
    #     user = set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #
    #     return user
