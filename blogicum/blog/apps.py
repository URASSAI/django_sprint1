from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Регистрация приложения blog."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
