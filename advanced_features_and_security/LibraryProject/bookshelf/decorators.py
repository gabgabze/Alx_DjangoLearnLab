"""create the decorated function for groups"""
from django.contrib.auth import user_logged_in


def is_admin(user):
    if user.is_superuser:
        return True

def is_viewer(user):
    if user_logged_in:
        return True

def is_editor(user):
    if user_logged_in:
        return True