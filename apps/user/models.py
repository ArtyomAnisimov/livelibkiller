# -*- coding: utf-8 -*-
from apps.books.models import Book
from django.contrib.auth.models import User
from django.db import models


class UsersBook(models.Model):
    book = models.ForeignKey(Book, verbose_name=u'Название')
    comment = models.TextField(verbose_name=u'Комментарий')
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    fav = models.BooleanField(verbose_name=u'Любимая', default=False)
    read = models.BooleanField(verbose_name=u'Прочитана', default=False)
    wish = models.BooleanField(verbose_name=u'Хочу прочитаь', default=False)

    def __str__(self):
        return self.book.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    nickname = models.CharField(verbose_name='Имя', max_length=100)
    date_joined = models.DateField(verbose_name='Дата регистрации')
    email = models.EmailField(verbose_name='Email', max_length=200)
    rating = models.IntegerField(verbose_name='Рейтинг')
    status = models.CharField(verbose_name='Статус', max_length=160)
    about = models.TextField(verbose_name='О себе', max_length=160)
