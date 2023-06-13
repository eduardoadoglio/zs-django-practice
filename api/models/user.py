from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    password_updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(pre_save, sender=User)
def username_equals_email(sender, instance, **kwargs):
    user = instance
    user.email = user.email.lower().strip()
    user.username = user.email