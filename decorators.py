# decorators.py
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def user_is_admin(user):
    if user.is_authenticated and user.is_superuser:
        return True
    raise PermissionDenied


def user_is_not_admin(user):
    if user.is_authenticated and not user.is_superuser:
        return True
    raise PermissionDenied
