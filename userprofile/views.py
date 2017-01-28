from django.contrib.auth import authenticate
from django.contrib.auth import logout as user_logout, login as user_login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    data = {}
    note = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
            return HttpResponseRedirect("/")
        note = "Giriş Başarısız"
    data['note'] = note
    return render(request, "login.html", data)


def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/")
