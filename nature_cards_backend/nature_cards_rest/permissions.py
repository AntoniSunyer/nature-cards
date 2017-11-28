from rest_framework import permissions

class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff
 
    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read&edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read&Write permissions are only allowed to the owner of the card.
        return obj.owner == request.user
    
class IsCardOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read&edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read&Write permissions are only allowed to the owner of the card related to the image.
        return obj.card.owner == request.user