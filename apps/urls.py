from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.home.urls', namespace='index')),
    url(r'^notificate/', include('apps.notificate.urls', namespace='notificate')),
]
