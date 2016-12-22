from django.apps import AppConfig
from django.db.utils import OperationalError

class NotificationConfig(AppConfig):
    name = 'apps.notificate'
    verbose_name = "Уведомления"

    def ready(self):
        try:
            from . import notificate
            notificate.apply_models()
        except OperationalError:
            pass
        from . import signals
