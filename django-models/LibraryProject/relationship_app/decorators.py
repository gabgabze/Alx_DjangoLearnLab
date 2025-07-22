from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Admin'

def is_librarian(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Librarian'

def is_member(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Member'