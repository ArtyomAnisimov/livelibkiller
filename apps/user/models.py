# -*- coding: utf-8 -*-

from django.db import models
from apps.books.models import Book
from django.contrib.auth.models import User


class UsersBook(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(verbose_name=u'Название',max_length=200)
	comment = models.CharField(verbose_name=u'Комментарий',max_length=200)
	user = models.ForeignKey('auth.User',verbose_name=u'Пользователь')
	fav = models.BooleanField()
	read = models.BooleanField()
	wish = models.BooleanField()
	def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    pass
