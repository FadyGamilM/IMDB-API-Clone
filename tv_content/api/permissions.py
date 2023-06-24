from rest_framework import permissions
from rest_framework.request import Request
from ..models import Review


class AdminOrReadOnly(permissions.IsAdminUser):
    '''
        + Admin can have full access to the routes
        + Regular users can perform GET requests only 
    '''

    def has_permission(self, request, view) -> bool:
        is_admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or is_admin_permission


class ReviewerOrReadOnly(permissions.BasePermission):
    '''
        only review owner can have acess to GET, PUT, DELETE 
        other users can perform GET only
    '''

    def has_object_permission(self, request: Request, view, obj: Review):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.reviewer
