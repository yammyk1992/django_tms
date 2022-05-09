from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def main_page(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0, }

    # наполнение шаблона данными - render
    return render(request, 'publication_app/main_page.html', context=context)


def about(request):
    return render(request, 'publication_app/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.category_id,
    }
    return render(request, 'publication_app/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


def show_category(request, category_id):

    posts = Post.objects.filter(category_id=category_id)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts, 'menu': menu, 'title': 'Отображение по категориям', 'cat_selected': category_id, }

    # наполнение шаблона данными - render
    return render(request, 'publication_app/main_page.html', context=context)
