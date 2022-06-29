import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, request
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.mail import send_mail

# Create your views here.
from .forms import *
from .utils import *
from .models import *


class PostHome(DataMixin, ListView):
    # количество отображаемых постов на странице...
    # paginate_by = 3
    model = Post
    template_name = 'publication_app/main_page.html'
    context_object_name = 'posts'

    # создаём динамический контекст чтобы передать меню
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    # создаём функцию которая будет отображать публикации только которые отмечены галочкой is_public
    def get_queryset(self):
        return Post.objects.filter(is_public=True).select_related('category')


def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag)

    template = loader.get_template('about.html')

    context = {
        'posts': posts,
        'tag': tag,
    }

    return HttpResponse(template.render(context, request))


# декоратор для того что-бы страницу about смотрели только зарегистрированные пользователи
@login_required
def about(request):
    return render(request, 'publication_app/about.html', {'menu': menu, 'title': 'О сайте'})


# Создание класса представлений вместо функций
# class AddPage(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddPostForm
#     template_name = 'publication_app/addpage.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('home')
#     raise_exception = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Добавление статьи')
#         return dict(list(context.items()) + list(c_def.items()))

class AddPage(View):
    @staticmethod
    def get(request):
        form = ImagePostForm()

        context = {
            'form': form,
        }

        return render(request, 'publication_app/addpage.html', context)

    @staticmethod
    def post(request):
        form = ImagePostForm(request.POST, request.FILES)
        image = request.FILES.getlist('image')
        tag = request.POST.getlist('tag')

        if len(image) > 4:
            context = {
                "title": "Добавление нового поста",
                "form": form,
                "error": "Максимальное количество фотографии - 4"
            }
            return render(request, "publication_app/addpage.html", context)

        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                is_public=form.cleaned_data['is_public'],
                slug=form.cleaned_data['slug'],
                category=form.cleaned_data['category'],

            )

            for images in image:
                ImagePost.objects.create(
                    post=post,
                    image=images
                )

            for tag in tag:
                post.tag.add(tag)

            return redirect('home')

        else:
            context = {
                'title': 'Добавление нового поста',
                'form': form,
            }
            return render(request, 'publication_app/addpage.html', context)


def contact(request):
    return HttpResponse('Обратная связь')


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'publication_app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def post_view(request):
#     posts = Post.objects.all()
#     return render(request, 'publication_app/main_page.html', {'posts': posts})


# def show_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     photos = PostImage.objects.filter(post=post)
#
#     context = {
#         'post': post,
#         'photos': photos,
#         # 'menu': menu,
#         # 'title': post.title,
#         # 'cat_selected': post.category_id,
#     }
#     return render(request, 'publication_app/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'publication_app/main_page.html'
    context_object_name = 'posts'
    allow_empty = False

    # создаём функцию которая будет отображать публикации только которые отмечены галочкой is_public
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'], is_public=True)

    # создаём динамический контекст чтобы передать меню
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].category),
                                      cat_selected=context['posts'][0].category_id)
        return dict(list(context.items()) + list(c_def.items()))


# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'publication_app/register.html'
#     success_url = reverse_lazy('login')
#
#     # при успешной регистрации будем сразу авторизовывать
#     def form_valid(self, form):
#         user = form.save()
#         send_mail(
#             'Спасибо за регистрацию',
#             'Мы будем присылать вам много спама, но не долго!!!',
#             from_email=str(os.getenv('EMAIL_HOST_USER')),
#             recipient_list=[user.email],
#             fail_silently=False)
#
#         return super().form_valid(form)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Регистрация')
#         return dict(list(context.items()) + list(c_def.items()))

class Register(View):
    """Класс регистрации пользователя"""

    @staticmethod
    def get(request):

        if request.user.is_authenticated:
            return redirect('posts')

        form = RegisterUserForm()

        context = {
            'title': 'Регистрация ',
            'form': form
        }
        return render(request, 'publication_app/register.html', context)

    @staticmethod
    def post(request):
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.save()
            send_mail(
                'Спасибо за регистрацию',
                'Мы будем присылать вам много спама, но не долго!!!',
                str(os.getenv('EMAIL_HOST_USER')),
                [user.email],
                fail_silently=False)
            login(request, user)
            return redirect('/')
        context = {
            'title': 'Registration',
            'form': form,
            }

        return render(request, 'publication_app/register.html', context)


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'publication_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
