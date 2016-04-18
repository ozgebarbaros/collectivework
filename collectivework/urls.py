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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'collectivework.views.login',name='login'),
    #url(r'^home/$', 'collectivework.views.home', name='home'),
    url(r'^logout/$', 'collectivework.views.logout', name='logout'),
    url(r'^list_moderation_request/$', 'collectivework.views.listmoderationrequests', name='listmoderationrequests'),
    url(r'^create_ticket/$', 'collectivework.views.create_ticket', name='create_ticket'),
    url(r'^list_my_ticket/$', 'collectivework.views.list_my_tickets', name='list_my_ticket'),
    #url(r'^all_ticket_list/$', 'collectivework.views.all_ticket_list', name='all_ticket_list'),
    url(r'^siterules/$', 'collectivework.views.siterules', name='siterules'),
    url(r'^help/$', 'collectivework.views.help', name='help'),

]
