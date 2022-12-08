from django.contrib.auth.models import User
from django.db import models


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='follow_user_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='follow_follower_set', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} follow {self.followed.username}'