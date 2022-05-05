from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('created_at', 'id', ).all()

    contex = {'title': 'HI ALL', 'posts': posts}
    # наполнение шаблона данными - render
    return render(request, 'main_page.html', contex)


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1> Статьи по категориям </h1><p> {catid} </p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect("/")

    return HttpResponse(f"<h1> Архив по годам </h1><p> {year} </p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")
