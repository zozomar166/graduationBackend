from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # for admin
        return bool(request.user and request.user.is_staff)


class CustomerBlindPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        # for anyone
        if request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']:
            return True
        return bool(request.user and request.user.is_staff)


class BlindDevicePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # for anyone
        if request.method in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']:
            return True
        return bool(request.user and request.user.is_staff)

