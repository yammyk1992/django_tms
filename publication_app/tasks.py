from celery import shared_task


@shared_task
def send_my_mail():
    """Рассылка писем о новых записях"""
    return None

