from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    """Allow user to update their own profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id