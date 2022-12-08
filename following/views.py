from django.contrib.auth.models import User
from django.shortcuts import render
from .func import get_fans, get_friends, get_eyes_on


def index(request):
    return render(request, 'base.html')


def user_list(request):
    user = User.objects.exclude(username=request.user)
    return render(request, 'user_list.html', {'users': user})


def user_page(request, pk):
    user = User.objects.get(username=pk)
    return render(
        request,
        "user.html",
        {
            'user': user,
            "eyes_on": get_eyes_on(user),
            "fans": get_fans(user),
            "friends": get_friends(user),
        }
    )