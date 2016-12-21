class NotificateRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, *models):
        for model in models:
            if not model in self._registry.values():
                self._registry[repr(model).split('.')[-1].split('\'')[0]] = model

    def apply_models(self, query):
        """
        Gets query - registered models. On django start it should be empty.
        Otherwise, it needs to be cleared
        """
        for k, v in self._registry.items():
            print("Applying {} model...".format(k))
            print(v.__module__)

