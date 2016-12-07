from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from app.requests.forms import RequestForm
from app.requests.models import Request
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from myapp.forms import ContactForm
#Кажется, выше импорты нужны
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class HomeView(TemplateView):
    template_name = "/home/index.html"

class LoginFormView(FormView):
    template_name = "/home/login.html"
    login_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)
    

