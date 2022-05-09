
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from accounts.models import Profile
from django.contrib.auth.models import User


def post_save_user(sender, created, instance, **kwargs):
    if created:
        user = instance
        owner = Blog.objects.created(user=user, username=user.username)
        print('User was saved!')

post_save.connect(post_save_user, sender=User)

