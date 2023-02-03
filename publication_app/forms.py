from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import *
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
class AddPageForm(forms.ModelForm):
    title = forms.CharField(label='Введите название поста*')
    content = forms.CharField(
        label='Введите тест к посту*',
        widget=forms.Textarea()
    )
    is_public = forms.BooleanField(
        label='Делаем видимой?',
        initial=True,
        required=False
    )

    tag = forms.ModelMultipleChoiceField(
        label='Тэги',
        required=False,
        queryset=Tag.objects.all(),
    )
    category = forms.ModelChoiceField(label='Выберите категорию поста*', required=False,
                                      queryset=Category.objects.all(), )
    slug = forms.SlugField(label='Введите уникальный слаг*')

    class Meta:
        model = Post
        fields = ['title', 'content', 'is_public', 'category', 'tag', 'slug']
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


class ImagePostForm(AddPageForm):
    """Класс формы добавление изображение к посту"""
    image = forms.ImageField(
        label='Выберите фотографии(Не более 4)',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(AddPageForm.Meta):
        fields = AddPageForm.Meta.fields + ['image', ]


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        """Сохраняем нового пользователя и хешируем пароль"""
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user
