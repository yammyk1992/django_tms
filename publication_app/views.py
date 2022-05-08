from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def main_page(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts, 'cats': cats, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0, }

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


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


def show_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts, 'cats': cats, 'menu': menu, 'title': 'Главная страница', 'cat_selected': category_id, }

    # наполнение шаблона данными - render
    return render(request, 'publication_app/main_page.html', context=context)
