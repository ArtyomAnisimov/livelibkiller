from apps.books.models import Book
from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    class Meta:
        app_label = 'bookmarks'
        ordering = ['created']
        verbose_name_plural = 'Закладки'
        verbose_name = 'Закладка'

    user = models.ForeignKey(User, verbose_name="Пользователь")
    book = models.ForeignKey(Book, verbose_name="Книга")
    content = models.TextField(verbose_name="Содержание цитаты")
    page = models.PositiveIntegerField(verbose_name="Номер страницы с цитатой", blank=True)
    created = models.DateTimeField(verbose_name="Дата создания закладки", auto_now=True, blank=True)

    def __str__(self):
        return "Закладка от {} по книге {}".format(self.user, self.book)
