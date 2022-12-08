from django.contrib.auth.models import User

from following.models import Follow


def _get_follow(user: User):
    return Follow.objects.filter(user=user)


def _get_followed(user: User):
    return Follow.objects.filter(followed=user)


def get_friends(user):
    follow_q = _get_follow(user)
    followed_q = _get_followed(user)
    return follow_q.filter(followed__username__in=followed_q.values_list('user__username'))


def get_fans(user):
    follow_q = _get_follow(user)
    followed_q = _get_followed(user)
    return followed_q.exclude(user__username__in=follow_q.values_list('followed__username'))


def get_eyes_on(user):
    follow_q = _get_follow(user)
    followed_q = _get_followed(user)
    return follow_q.exclude(followed__username__in=followed_q.values_list('user__username'))