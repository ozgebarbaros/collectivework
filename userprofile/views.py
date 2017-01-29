from django.contrib.auth import authenticate
from django.contrib.auth import logout as user_logout, login as user_login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from collectivework import settings
from userprofile.forms import UserProfileForm, UserForm, UserUpdateForm


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
            return HttpResponseRedirect(request.GET['next'])
        note = "Giriş Başarısız"
    data['note'] = note
    return render(request, "login.html", data)

def signup(request):
    if request.POST:
        userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form')
        user_form = UserForm(request.POST, request.FILES, prefix='user_form')
        if all([userprofile_form.is_valid(), user_form.is_valid()]):
            user = user_form.save()
            profile = userprofile_form.save(commit=False)
            profile.user = user
            profile.save()
            user_login(request, user)
            return HttpResponseRedirect(reverse("userprofile:login"))
    else:
        userprofile_form = UserProfileForm(prefix='userprofile_form')
        user_form = UserForm(prefix='user_form')
    return render(request, "signup.html", {
        'userprofile_form': userprofile_form,
        'user_form': user_form
    })

@login_required(login_url=settings.LOGIN_URL)
def update(request):
    data = {}
    if request.POST:
        try:
            userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form', instance=request.user.userprofile)
        except ObjectDoesNotExist:
            userprofile_form = UserProfileForm(request.POST, request.FILES, prefix='userprofile_form')
        user_form = UserUpdateForm(request.POST, request.FILES, prefix='user_form', instance=request.user)
        if all([userprofile_form.is_valid(), user_form.is_valid()]):
            user = user_form.save()
            profile = userprofile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse("userprofile:update"))
    else:
        user_form = UserUpdateForm(instance=request.user, prefix='user_form')
        try:
            userprofile_form = UserProfileForm(prefix='userprofile_form', instance=request.user.userprofile)
        except ObjectDoesNotExist:
            userprofile_form = UserProfileForm(prefix='userprofile_form')
    data['userprofile_form'] = userprofile_form
    data['user_form'] = user_form
    return render(request, "update.html", data)

def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/")
