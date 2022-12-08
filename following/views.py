from itertools import chain

from django.contrib.auth.models import User
from django.shortcuts import render
from .func import get_fans, get_friends, get_eyes_on, follow, unfollow


def index(request):
    return render(request, 'base.html')


def user_list(request):
    user = User.objects.exclude(username=request.user)
    return render(request, 'user_list.html', {'users': user})


def user_page(request, pk):
    cur_user = request.user
    user = User.objects.get(username=pk)
    tab_action = request.GET.get('tab_action', 'eye_on')

    if request.method == "POST":
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            follow(cur_user, user)
        elif action == "unfollow":
            unfollow(cur_user, user)

    return render(
        request,
        "user.html",
        {
            'is_follow': cur_user.username in [u.fan_name() for u in get_fans(user)],
            'is_friends': cur_user.username in [u.friend_name() for u in get_friends(user)],
            'cur_user': cur_user,
            'user': user,
            "eyes_on": get_eyes_on(user),
            "fans": get_fans(user),
            "friends": get_friends(user),
            "tab_action": tab_action,
        }
    )