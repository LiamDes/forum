from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'auth'
    name = 'backend.auth'
    label = 'backend_auth'
