from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from publication_app.utils import DataMixin
from tags_app.models import Tag


class TagsView(DataMixin, ListView):
    model = Tag
    template_name = 'publication_app/tag.html'
    context_object_name = 'tags'
    allow_empty = False
    pk_url_kwarg = 'pk'

    # создаём динамический контекст чтобы передать меню
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        t_def = self.get_user_context(title='Тэг - ' + str(context['tags'][0].tag))
        return dict(list(context.items()) + list(t_def.items()))
