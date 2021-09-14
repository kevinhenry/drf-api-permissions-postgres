from rest_framework import permissions
# import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # return super().has_object_permission(request, view, obj)
            return True

        if obj.author is None:
            return True

        return obj.author == request.user