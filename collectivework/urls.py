"""collectivework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import static
from django.conf.urls import url, include
from django.contrib import admin
from postman import urls as postman_urls

from collectivework import settings
from collectivework.views import site_rules, help
from ticket import urls as ticket_urls
from  userprofile import urls as userprofile_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', include(postman_urls, namespace='postman', app_name='postman')),
    url(r'^user/', include(userprofile_urls, namespace='userprofile', app_name='userprofile')),
    url(r'^site_rules/$', site_rules, name='site_rules'),
    url(r'^help/$', help, name='help'),
    url(r'^', include(ticket_urls, namespace="collectivework", app_name="ticket"), name="index"),
]

if settings.DEBUG is True:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
