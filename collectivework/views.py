from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# from django.template.context import RequestContext


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'all_ticket_list.html')


@login_required(login_url='/')
def create_ticket(request):
    return render(request, 'create_ticket.html')


@login_required(login_url='/')
def list_my_tickets(request):
    return render(request, 'list_my_tickets.html')


def help(request):
    return render(request, 'help.html')


def siterules(request):
    return render(request, 'siterules.html')


def about(request):
    return render(request, 'about.html')


@staff_member_required(login_url='/')
def listmoderationrequests(request):
    data = {}
    return render(request, 'listmoderationrequests.html', data)


def logout(request):
    auth_logout(request)
    return redirect('/')
