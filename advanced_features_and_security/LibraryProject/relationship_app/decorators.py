def is_admin(user):
    if not user.is_authenticated:
        return False
    userprofile = getattr(user, 'userprofile', None)
    return userprofile and userprofile.role == 'admin'

    #eturn user.is_authenticated and hasattr(user, 'userprofile', None) and userprofile.role =='Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile', None) and profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile', None) and profile.role == 'Member'