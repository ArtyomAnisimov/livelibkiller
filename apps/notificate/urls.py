from django.conf.urls import url
from .views import NotificateSubscribe

urlpatterns = [
    url(r'^$', NotificateSubscribe.as_view(), name='subcribe'),
]