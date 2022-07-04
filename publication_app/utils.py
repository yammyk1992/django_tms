from django.db.models import Count

from tags_app.models import Tag
from .models import Category

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Профиль", 'url_name': 'profile_account'}
        ]


# создаём класс (миксин) для убирания дублирования кода
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        tags = Tag.objects.all()
        count_tags = Tag.objects.annotate(count=Count('tag_post')).order_by('-count')
        context['tag_selected'] = 0
        context['tags'] = tags
        context['count_tags'] = count_tags
        # если юзер не авторизован то на сайте он не видит поля Добавить статью
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context



