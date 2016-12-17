from apps.books.models import Book
from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    class Meta:
        app_label = 'reviews'
        ordering = ['date_created']
        verbose_name_plural = 'Рецензии'
        verbose_name = 'Рецензия'

    content = models.TextField(verbose_name="Содержание рецензии")
    user = models.ForeignKey(User, verbose_name="Пользователь")
    book = models.ForeignKey(Book, verbose_name="К какой книге рецензия")
    date_created = models.DateTimeField(verbose_name="Дата создания", auto_now=True)

    def __str__(self):
        return "Рецензия от {} к книге {}".format(self.user, self.book)
