from django.db.models.signals import post_save  # acts when saving is on db
from django.contrib.auth.models import User
from django.dispatch import receiver #  listen for the signal and "receive" it when it fires
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

