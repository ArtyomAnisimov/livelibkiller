from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, FormView


class HomeView(TemplateView):
    template_name = "/home/index.html"


class LoginFormView(FormView):
    template_name = "/home/login.html"
    form_class = AuthenticationForm
    success_url = '/'
