import os

from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.charity'

    def ready(self):
        # Any code here runs ONCE when Django loads this app
        if os.environ.get("RUN_MAIN") != "true":
            return

        from apps.charity.options import create_default_options
        create_default_options()
