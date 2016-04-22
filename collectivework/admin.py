#!-*- coding:utf-8 -*-

from django.contrib import admin
from collectivework.models import Ticket, TicketTag

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(TicketTag)
class TicketTagsAdmin(admin.ModelAdmin):
    pass
