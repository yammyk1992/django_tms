from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from .models import *
from .forms import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class PostHome(ListView):
    model = Post
    template_name = 'publication_app/main_page.html'
    context_object_name = 'posts'

    # создаём динамический контекст чтобы передать меню
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['category_selected'] = 0
        return context

    # создаём функцию которая будет отображать публикации только которые отмечены галочкой is_public
    def get_queryset(self):
        return Post.objects.filter(is_public=True)


# def main_page(request):
#     posts = Post.objects.all()
#     context = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0, }
#
#     # наполнение шаблона данными - render
#     return render(request, 'publication_app/main_page.html', context=context)


def about(request):
    return render(request, 'publication_app/about.html', {'menu': menu, 'title': 'О сайте'})


# Создание класса представлений вместо функций
class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'publication_app/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


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


def login(request):
    return HttpResponse('Авторизация')


class ShowPost(DetailView):
    model = Post
    template_name = 'publication_app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.category_id,
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


class PostCategory(ListView):
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
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        context['menu'] = menu
        context['category_selected'] = context['posts'][0].category_id
        return context
