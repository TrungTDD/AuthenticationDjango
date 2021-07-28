from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    print(not request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "users/index.html")


def registration(request):
    pass


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        return render(request, "users/login.html", {
            "message": "Login faield, check your username or password"
        })

    if not request.user.is_authenticated:
        return render(request, "users/login.html")
    else:
        return HttpResponseRedirect(reverse("index"))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required(login_url="/users/login/")
def detail_user(request, username):
    print(username)
    return render(request, "users/detail.html")
