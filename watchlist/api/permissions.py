from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """Allow admin access to edit permissions | Others view only"""
    def has_permission(self, request, view): 
        return super().has_permission(request, view) or request.method == "GET"
    
class ReviewUserOrReadOnly(permissions.BasePermission): 
    """Only the user who created the review is allowed to update and modify"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user