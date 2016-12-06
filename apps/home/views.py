from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from app.requests.forms import RequestForm
from app.requests.models import Request
from django.http import HttpResponseRedirect
from django.views.generic import FormView
#Кажется, выше импорты нужны
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class HomeView(TemplateView):
    template_name = "/home/index.html"

class LoginFormView(FormView):
    template_name = "/home/login.html"

    form_class = AuthenticationForm

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return next
        return '/home/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        if self.request.user.is_authenticated:
            return super(LoginFormView, self).form_valid(form)
        return super(LoginFormView, self).form_invalid(form)

