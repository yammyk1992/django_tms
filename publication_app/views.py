from django.shortcuts import render


# Create your views here.
from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id',).all()

    contex = {'title': 'HI ALL', 'posts': posts}
    return render(request, 'main_page.html', contex)