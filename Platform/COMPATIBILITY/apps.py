from django.apps import AppConfig


class CompatibilityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'COMPATIBILITY'
