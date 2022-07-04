from django import template

from tags_app.models import Tag

register = template.Library()


@register.simple_tag()
def get_tags(filter=None):
    if not filter:
        return Tag.objects.all()
    else:
        return Tag.objects.filter(pk=filter)


@register.inclusion_tag('publication_app/base.html')
def show_tags(sort=None):
    if not sort:
        tags = Tag.objects.all()
    else:
        tags = Tag.objects.order_by(sort)

    return {'tags': tags}
