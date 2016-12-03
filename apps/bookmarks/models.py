from apps.books.models import Book
from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь")
    book = models.ForeignKey(Book, verbose_name="Книга")
    content = models.TextField(verbose_name="Содержание цитаты")
    page = models.PositiveIntegerField(verbose_name="Номер страницы с цитатой", blank=True)
    created = models.DateTimeField(verbose_name="Дата создания закладки", auto_now=True, blank=True)
