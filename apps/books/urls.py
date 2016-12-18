from django.conf.urls import url, include
from apps.books.views import CreateFormView

urlpatterns = [
    url(r'^create/$', CreateFormView.as_view(), name='create'),
 ]
