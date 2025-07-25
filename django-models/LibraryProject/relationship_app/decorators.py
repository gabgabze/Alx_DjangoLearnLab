def is_admin(user, profile=None):
    if not user.is_authenticated:
        return False
    userprofile = getattr(user, 'userprofile', None)
    return profile and profile.role == 'admin'

    #eturn user.is_authenticated and hasattr(user, 'userprofile', None) and userprofile.role =='Admin'

def is_librarian(user, profile=None):
    return user.is_authenticated and hasattr(user, 'profile') and profile.role == 'Librarian'

def is_member(user, profile=None):
    return user.is_authenticated and hasattr(user, 'profile') and profile.role == 'Member'