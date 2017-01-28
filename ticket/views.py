from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from ticket.forms import CreateTicketForm
from ticket.models import Ticket


def list_ticket(request):
    tickets = []
    if request.user:
        if request.user.is_staff:
            tickets = Ticket.objects.all().order_by('-creation_date')
        elif request.user.is_authenticated():
            tickets = Ticket.objects.filter(accepted=True).order_by('-creation_date')
        else:
            tickets = Ticket.objects.filter(accepted=True, completed=False, assigned_user=None).order_by(
                '-creation_date')

    return render(request, 'list_ticket.html', {'tickets': tickets})


@login_required(login_url='/')
def create_ticket(request):
    if request.POST:
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.request_in_user = request.user
            ticket.save()
            return HttpResponseRedirect('/ticket/')
    else:
        form = CreateTicketForm()
    return render(request, 'detail_ticket.html', {'form': form, 'title': "Yeni İstek Oluştur", 'creation': True})


@login_required(login_url='/')
def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    form = CreateTicketForm(instance=ticket)
    return render(request, 'detail_ticket.html',
                  {'form': form, 'title': "İstek Numarası: %s" % ticket.pk, 'creation': False})


@login_required(login_url='/')
def list_my_ticket(request):
    tickets = Ticket.objects.filter(assigned_user=request.user).order_by('-creation_date')
    return render(request, 'list_ticket.html', {'tickets': tickets})


@staff_member_required
def list_moderation_requests(request):
    tickets = Ticket.objects.filter(accepted=False, rejected=False, completed=False).order_by('-creation_date')
    return render(request, 'list_ticket.html', {'tickets': tickets})