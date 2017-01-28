"""collectivework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from collectivework.views import login, logout, site_rules, help

from postman import urls as postman_urls
from ticket import urls as ticket_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^messages/', include(postman_urls, namespace='postman', app_name='postman')),
    url(r'^ticket/', include(ticket_urls)),
    url(r'^logout/$', logout, name='logout'),
    url(r'^site_rules/$', site_rules, name='site_rules'),
    url(r'^help/$', help, name='help'),
    url(r'^$', login, name='login'),
]
