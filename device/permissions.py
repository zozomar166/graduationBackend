from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # for anyone
        if request.method in ['GET', 'HEAD', 'PUT', 'PATCH', 'OPTIONS']:
            return True

        # for admin
        return bool(request.user and request.user.is_staff)


class CustomerBlindPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        # for anyone
        if request.method in ['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']:
            return True


class BlindDevicesPermissions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        # for anyone
        if request.method in ['GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']:
            return True
