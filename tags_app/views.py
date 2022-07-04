from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from publication_app.models import Post
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
        t_def = self.get_user_context(title='Тэги - ' + str(context['tags'][0].tag),
                                      tag_selected=context['tags'][0].tag)
        return dict(list(context.items()) + list(t_def.items()))


class GetTag(ListView):
    queryset = Post.objects.all()
    template_name = 'profile_app/main_page.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tag__tag=self.kwargs['tag'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = f"Посты по тегу {self.kwargs['tag']}"
        context['name_text'] = context['title']
        context['tag'] = Tag.objects.all()
        return context
