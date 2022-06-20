from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_profile(request):
    return HttpResponse('Профиль')

