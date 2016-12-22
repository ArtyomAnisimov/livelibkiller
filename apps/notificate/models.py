from django.contrib.auth.models import User
from django.db import models


class NotificationSubscribes(models.Model):
    class Meta:
        app_label = 'notificate'
        verbose_name_plural = 'Подписки на уведомления'
        verbose_name = 'Подписка на уведомление'
        db_table = "subscriptions"

    user = models.ForeignKey(User, verbose_name="Пользователь")
    model = models.CharField(verbose_name="Пользователь", max_length=255)
    event = models.CharField(verbose_name="Событие", max_length=100)

    def __str__(self):
        return "{} - {}".format(self.model, self.event)


class NotificationModel(models.Model):
    class Meta:
        db_table = "registry_models"
        verbose_name_plural = 'Зарегистрированные модели'
        verbose_name = 'Зарегистрированная модель'

    model = models.CharField(verbose_name="Зарегистрированная модель", max_length=255, editable=False)
    module = models.CharField(verbose_name="Модуль", max_length=255, editable=False)

    def __str__(self):
        return "{}.{}".format(self.module, self.model)
