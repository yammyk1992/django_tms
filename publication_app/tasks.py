from datetime import datetime, timedelta
from celery import shared_task
from publication_app.views import *


@shared_task
def send_my_mail():
    # время за последние сутки
    start_date = datetime.now() - timedelta(days=1)
    # время сейчас
    end_date = datetime.now()
    # делаем список, с функцией map() возвращающая объект map (итератор), который мы можем
    # использовать в других частях нашей программы.
    new_posts = list(map(lambda p: p.content, Post.objects.filter(created_at__range=[start_date,
                                                                                     end_date])))
    # добавляем lambda с аргументом text поста, фильтруем посты сделаные за сутки.
    if len(new_posts) > 0:
        for spam in User.objects.all():
            send_mail(
                'New Posts!',
                'Posts:\n' + '\n'.join(
                    new_posts) + '\n\nNew and bright posts only on our website. '
                                 'https://yammyk-django-heroku.herokuapp.com/',
                # преобразовываем список в строку с помощью join()
                str(os.getenv('EMAIL_HOST_USER')),
                [spam.email]
            )
    return None
