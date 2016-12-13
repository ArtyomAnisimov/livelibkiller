from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['User'] = User
        return context


class LoginFormView(FormView):
    template_name = "home/login.html"
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        print(form.get_user())
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
