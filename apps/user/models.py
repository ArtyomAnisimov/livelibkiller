from django.db import models
from apps.books.models import Book
from django.contrib.auth.models import User


class UsersBook(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=30)
    rating = models.CharField (max_length=30)


class UserProfile(models.Model):
    nickname = models.CharField(max_length=30)
    date_of_registration = models.DateField()
    age = models.PositiveIntegerField()
    rating = models.CharField (max_length=30)
    status = models.CharField (max_length=160)
    
