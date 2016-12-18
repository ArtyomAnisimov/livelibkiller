from django.forms import ModelForm
from apps.books.models import Book


class BookCreateForm(ModelForm):
    class Meta:
         model = Book
         fields = ['title', 'cover', 'name', 'author', 'genre', 'date_published',
                       'editor', 'publish', 'description', 'where_buy', 'film'
         ]
