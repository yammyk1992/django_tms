from django.http import HttpResponse


# Create your views here.
def show_profile(request):
    return HttpResponse('Профиль')
