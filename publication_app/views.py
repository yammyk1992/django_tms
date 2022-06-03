from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

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


# def tags(request, tag_slug):
#     tag = get_object_or_404(Tag, slug=tag_slug)
#     posts = Post.objects.filter(tags=tag).order_by('-posted')
#
#     template = loader.get_template('tag.html')
#
#     context = {
#         'posts': posts,
#         'tag': tag,
#     }
#
#     return HttpResponse(template.render(context, request))


# class ImageView(generic.ListView):
#     template_name = 'publication_app/main_page.html'
#     context_object_name = 'case_list'
#
#     def get_queryset(self):
#         return PostImage.objects.all()


# def main_page(request):
#     posts = Post.objects.all()
#     context = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0, }
#
#     # наполнение шаблона данными - render
#     return render(request, 'publication_app/main_page.html', context=context)

# декоратор для того что-бы страницу about смотрели только зарегистрированные пользователи
# @login_required
def about(request):
    return render(request, 'publication_app/about.html', {'menu': menu, 'title': 'О сайте'})


# Создание класса представлений вместо функций
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'publication_app/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'publication_app/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи '})


def contact(request):
    return HttpResponse('Обратная связь')


# def login(request):
#     return HttpResponse('Авторизация')


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


# def show_category(request, category_id):
#     posts = Post.objects.filter(category_id=category_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'posts': posts, 'menu': menu, 'title': 'Отображение по категориям', 'cat_selected': category_id, }
#
#     # наполнение шаблона данными - render
#     return render(request, 'publication_app/main_page.html', context=context)


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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'publication_app/register.html'
    success_url = reverse_lazy('login')

    # при успешной регистрации будем сразу авторизовывать
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


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
