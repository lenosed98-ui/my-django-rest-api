from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrAdmin(BasePermission):
    """
    Read: آزاد
    Write: فقط نویسندهٔ شیء یا ادمین
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not user.is_authenticated:
            return False
        return getattr(obj, 'author', None) == user or user.is_staff
