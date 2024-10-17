from django.apps import AppConfig


class BaseSharedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_shared'
