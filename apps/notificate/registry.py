from django.db.models.signals import post_save, post_delete
from .signal_handlers import save_handler, delete_handler


class NotificateRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, *models):
        for model in models:
            self._registry[model.__name__] = model

    def apply_models(self):
        """
            When app init, registered models should be re-registered again, because
            it rather simplier than checking for existing registered models, removing non-existing registered models,
            adding new registered models, etc...
        """
        from .models import NotificationModel
        if NotificationModel.objects.exists():
            NotificationModel.objects.all().delete()

        NotificationModel.objects.bulk_create(
            [NotificationModel(model=model_str, module=model.__module__)
             for model_str, model in self._registry.items()])

    def apply_signals(self):
        for model in self._registry.values():
            post_save.connect(save_handler, sender=model)
            post_delete.connect(delete_handler, sender=model)
