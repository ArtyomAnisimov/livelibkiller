from django.forms import ModelForm
from apps.books.models import Book, Author
from django import forms

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['film' ,'title', 'name',  'author', 'genre', 'cover', 'date_published',
                      'editor', 'publish', 'description', 'where_buy'
        ]
