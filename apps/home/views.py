from django.shortcuts import render
from .models import Post

def home_view(request):
    return render(request, '/home/index.html')
