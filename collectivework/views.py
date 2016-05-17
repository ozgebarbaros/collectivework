# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from collectivework.models import Ticket
from collectivework.forms import CreateTicketForm

# from django.template.context import RequestContext


def login(request):
    all_tickets = None
    if request.user:
        if request.user.is_staff:
            all_tickets = Ticket.objects.all()
        elif request.user.is_authenticated():
            all_tickets = Ticket.objects.filter(accepted=True)
        else:
            all_tickets = Ticket.objects.filter(accepted=True, completed=False, assigneduser=None)
    
    return render(request, 'all_ticket_list.html', {'ticketlist': all_tickets})


@login_required(login_url='/')
def create_ticket(request):
    form = CreateTicketForm()
    if request.POST:
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            return HttpResponse("OK")
        else:
            return HttpResponse("NOK")
    return render(request, 'create_ticket.html',{'form':form})


@login_required(login_url='/')
def list_my_tickets(request):
    ticketlist = Ticket.objects.filter(assigneduser=request.user)
    return render(request, 'list_my_tickets.html',{'ticketlist': ticketlist})


def help(request):
    return render(request, 'help.html')


def siterules(request):
    return render(request, 'siterules.html')


def about(request):
    return render(request, 'about.html')


@staff_member_required
def listmoderationrequests(request):
    data = {}
    data['ticketlist']= Ticket.objects.filter(accepted=False, rejected=False, completed=False)
    return render(request, 'listmoderationrequests.html', data)


def logout(request):
    auth_logout(request)
    return redirect('/')
