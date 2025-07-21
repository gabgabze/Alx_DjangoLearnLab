from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'role', None) == 'admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'role', None) == 'librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'role', None) == 'member'