# Create your views here.
# def show_profile(request):
#     return HttpResponse('Профиль')
from django.shortcuts import render, redirect
from django.views import View

from profile_app.forms.forms import ProfileEditForm, UserEditForm

# def profile_edit_view(request):
#     if request.method == "POST" and request.FILES['file']:
#         form = ProfileEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             your_file = request.FILES['file']
#             new_username = form.cleaned_data.get('username')
#             new_password = form.cleaned_data.get('password')
#             user = Profile.objects.get(username=request.user.username)
#             all_user = user.objects.get(user=user)
#             user.username = new_username
#             user.set_password(new_password)
#             user.save()
#             user.avatar = your_file
#             user.save()
#             return render(request, template_name='profile_edit_view.html')
#         return HttpResponse('home')
#
# class UpdateProfile(UpdateView):
#     model = Profile
#     fields = ['first_name', 'last_name', 'avatar', 'about']  # Keep listing whatever fields
#     # the combined UserProfile and User exposes.
#     template_name = 'user_update.html'
from publication_app.forms import RegisterUserForm


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

        if profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')

