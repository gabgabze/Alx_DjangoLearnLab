def is_admin(user):
    if not user.is_authenticated:
        return False
    userprofile = getattr(user, 'userprofile', None)
    return userprofile and userprofile.role == 'admin'

    r#eturn user.is_authenticated and hasattr(user, 'userprofile', None) and userprofile.role =='Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile', None) and userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile', None) and userprofile.role == 'Member'