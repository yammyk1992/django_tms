from django.apps import AppConfig


class PublicationAppConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'publication_app'
    verbose_name = 'Проект'

    # применяем сигнал
    def ready(self):
        from . import signals

