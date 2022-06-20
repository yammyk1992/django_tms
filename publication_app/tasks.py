from publication_app.celery import app
from publication_app.views import *


@app.task
def send_my_mail(user_email):
    send_mail(user_email)
