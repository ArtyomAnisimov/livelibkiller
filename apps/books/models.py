from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=50)   
    cover = models.ImageField(verbose_name="Обложка", upload_to=name_of_cover(), blank=True, null=True)
    name = models.CharField(verbose_name="Название", max_length=50)
    author = models.CharField(verbose_name="Автор", max_length=50)
    genre = models.CharField(verbose_name="Жанр", max_length=50)
    writing_data = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    editor = models.CharField(verbose_name="Редактор", max_length=50, blank=True, null = True)
    publish = models.CharField(verbose_name="Издательство", max_length=50, blank=True, null=True)
    description = models.TextField(verbose_name="Описание")
    where_buy =  models.CharField(verbose_name="Где купить", blank=True, null=True)
    if_have_film =  models.CharField(verbose_name="По ней снят фильм", blank=True, null=True)
