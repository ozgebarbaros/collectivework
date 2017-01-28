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
from django.conf.urls import url

from ticket.views import list_ticket, create_ticket, list_my_ticket, list_moderation_requests, show_ticket

urlpatterns = [
    url(r'^$', list_ticket, name='list_ticket'),
    url(r'^create/$', create_ticket, name='create_ticket'),
    url(r'^my/$', list_my_ticket, name='list_my_ticket'),
    url(r'^list_moderation_request/$', list_moderation_requests, name='list_moderation_requests'),
    url(r'^(?P<id>\w+)/$', show_ticket, name='show_ticket'),
]