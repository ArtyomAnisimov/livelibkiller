from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    cover = models.ImageField(verbose_name="Обложка", blank=True)
    name = models.CharField(verbose_name="Название", max_length=255)
    author = models.CharField(verbose_name="Автор", max_length=255)
    genre = models.CharField(verbose_name="Жанр", max_length=50)
    data_creation = models.DateField(verbose_name="Дата создания", blank=True)
    editor = models.CharField(verbose_name="Редактор", max_length=255, blank=True)
    publish = models.CharField(verbose_name="Издательство", max_length=100, blank=True)
    description = models.TextField(verbose_name="Описание")
    where_buy = models.CharField(verbose_name="Где купить", max_length=255, blank=True)
    film = models.CharField(verbose_name="По ней снят фильм", max_length=100, blank=True)
