def admin(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Admin'

def librarian(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Librarian'

def member(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'Member'