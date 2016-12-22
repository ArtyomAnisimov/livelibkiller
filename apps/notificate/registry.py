class NotificateRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, *models):
        for model in models:
            if not model in self._registry.values():
                self._registry[repr(model).split('.')[-1].split('\'')[0]] = model

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
            [NotificationModel(model=model, module=module.__module__)
             for model, module in self._registry.items()])

