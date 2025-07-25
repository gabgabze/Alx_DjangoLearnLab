from django.conf import settings
from django.db.models.signals import post_save  # acts when saving is on db
from django.conf import settings
from django.dispatch import receiver #  listen for the signal and "receive" it when it fires
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

