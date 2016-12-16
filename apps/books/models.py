from apps.books.models import Book
from apps.user.models import User
from django.db import models


class Genre(models.Model):
    class Meta:
        app_label = 'books'
        ordering = ['title']
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'

    title = models.CharField(verbose_name="Название жанра", max_length=50)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        app_label = 'books'
        ordering = ['?']
        verbose_name_plural = 'Рецензии'
        verbose_name = 'Рецензия'

    content = models.TextField(verbose_name="Содержание рецензии")
    user = models.ForeignKey(User, verbose_name="Пользователь")
    book = models.ForeignKey(Book, verbose_name="К какой книге рецензия")
    created = models.DateTimeField(verbose_name="Дата создания", auto_now=True, blank=True)

    def __str__(self):
        return "Рецензия от {} к книге {}".format(self.user, self.book)


class Collection(models.Model):
    class Meta:
        app_label = 'books'
        ordering = ['name']
        verbose_name_plural = 'Подборки'
        verbose_name = 'Подборка'

    name = models.CharField(verbose_name="Название подборки", max_length=150)
    books = models.ManyToManyField(Book, verbose_name="Книги")


class Autor(models.Model):
    class Meta:
        app_label = 'books'
        ordering = ['name']
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

    name = models.CharField(verbose_name='Автор', max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        app_label = 'books'
        ordering = ['title']
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'

    title = models.CharField(verbose_name="Заголовок", max_length=50)
    cover = models.ImageField(verbose_name="Обложка", blank=True)
    name = models.CharField(verbose_name="Название", max_length=255)
    author = models.CharField(verbose_name="Автор", max_length=255)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр(ы)")
    data_creation = models.DateField(verbose_name="Дата создания", blank=True)
    editor = models.CharField(verbose_name="Редактор", max_length=255, blank=True)
    publish = models.CharField(verbose_name="Издательство", max_length=100, blank=True)
    description = models.TextField(verbose_name="Описание")
    where_buy = models.CharField(verbose_name="Где купить", max_length=255, blank=True)
    film = models.CharField(verbose_name="По ней снят фильм", max_length=100, blank=True)

    def __str__(self):
        return self.title
