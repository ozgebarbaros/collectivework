# -*- coding:utf-8 -*-
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def login(request):
    return HttpResponseRedirect("/ticket/")


def help(request):
    return render(request, 'help.html')


def site_rules(request):
    return render(request, 'site_rules.html')


def about(request):
    return render(request, 'about.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
