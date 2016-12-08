from django.conf.urls import url, include
from .views import (HomeView, LoginFormView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
]
