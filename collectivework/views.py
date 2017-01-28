from django.shortcuts import render


def help(request):
    return render(request, 'help.html')


def site_rules(request):
    return render(request, 'site_rules.html')


def about(request):
    return render(request, 'about.html')
