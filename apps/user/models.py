from django.db import models
from apps.books.models import Book
from django.contrib.auth.models import User


class UsersBook(models.Model):
    book_name = "/apps/books/models.py"


class UserProfile(models.Model):
    user_profile= "/apps/templates/user/index.html
