from django.contrib.auth.models import User
from django.db import models


class NotificationSubscribes(models.Model):
    class Meta:
        app_label = 'notificate'
        verbose_name_plural = 'Уведомления'
        verbose_name = 'Уведомления'
        db_table = "subscriptions"

    user = models.ForeignKey(User, verbose_name="Пользователь")
    model = models.CharField(verbose_name="Пользователь", max_length=255)
    event = models.CharField(verbose_name="Событие", max_length=100)

    def __str__(self):
        return "{} - {}".format(self.model, self.event)


class NotificationModel(models.Model):
    model = models.CharField(verbose_name="Зарегистрированная модель", max_length=255, editable=False)
    module = models.CharField(verbose_name="Модуль", max_length=255, editable=False)

    class Meta:
        db_table = "registry_models"
