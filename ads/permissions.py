from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            user = obj.owner
        elif hasattr(obj, 'author'):
            user = obj.author
        else:
            return False
        if request.user == user:
            return True
        return False


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.ROLES in ['admin', 'moderator']:
            return True
        return False
