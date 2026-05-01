from rest_framework import permissions

class IsShopOwner(permissions.BasePermission):
    """
    Allow access only to users with is_shop_owner=True
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_shop_owner
    
class IsAdminOrReadOnly(permissions.BasePermission):
    """Safe methods for anyone, write/delete only for shop owner"""
    def has_permission(self, request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_shop_onwer