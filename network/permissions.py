from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """
    Разрешение для проверки, что пользователь активен.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active
