from django.apps import AppConfig


class PublicationAppConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'publication_app'
    verbose_name = 'Проект'

<<<<<<< HEAD

=======
    # применяем сигнал
    def ready(self):
        pass
>>>>>>> master/master

