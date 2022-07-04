from django.shortcuts import render, redirect
from django.views import View

from profile_app.forms.forms import ProfileEditForm, UserEditForm


class ProfileEdit(View):
    """Редактирование пользователя """

    @staticmethod
    def get(request):
        # параметр 'instance' берет все данные пользователя, если в бд есть
        # Получаем информацию пользователя из модели user & profile
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
            'title': 'Редактирование профиля',
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(
            request,
            'profile_app/user_update.html',
            context
        )

    @staticmethod
    def post(request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
