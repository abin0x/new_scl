
from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # return request.user.is_authenticated and request.user.is_teacher
        return request.user.is_authenticated and getattr(request.user, 'user_type', '') == 'teacher'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.teacher == request.user
