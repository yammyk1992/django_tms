from time import sleep
from celery import shared_task


@shared_task
def send_email_task():
    """Отправка писем с таймингом"""
    sleep(1)

    return None
