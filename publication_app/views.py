from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('created_at', 'id', ).all()

    # contex = {'title': 'HI ALL', 'posts': posts}
    # contex = {'title': 'HI ALL'}
    # наполнение шаблона данными - render
    return render(request, 'publication_app/main_page.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'publication_app/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1> Статьи по категориям </h1><p> {catid} </p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect("home", permanent=True)

    return HttpResponse(f"<h1> Архив по годам </h1><p> {year} </p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")
