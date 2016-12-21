from django.apps import AppConfig
from django.db.utils import OperationalError

class NotificationConfig(AppConfig):
    name = 'apps.notificate'
    verbose_name = "Уведомления"

    def ready(self):
        from .models import NotificationModel
        from . import notificate
        try:
            registry_models = NotificationModel.objects
            notificate.apply_models(registry_models)
        except OperationalError:
            pass
