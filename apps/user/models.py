# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class UsersBook(models.Model):
    book_name = models.CharField(verbose_name=u'Название', max_length=200)
    comment = models.CharField(verbose_name=u'Комментарий', max_length=200)
    user = models.ForeignKey('auth.User', verbose_name=u'Пользователь')
    fav = models.BooleanField()
    read = models.BooleanField()
    wish = models.BooleanField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    nickname = models.CharField(verbose_name='Имя', max_length=100)
    date_joined = models.DateField(verbose_name='Дата регистрации')
    email = models.EmailField(verbose_name='Email', max_length=200)
    rating = models.IntegerField(verbose_name='Рейтинг')
    status = models.CharField(verbose_name='Статус', max_length=160)
    about = models.TextField(verbose_name='О себе', max_length=160)
