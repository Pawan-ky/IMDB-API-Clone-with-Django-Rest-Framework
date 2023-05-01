from rest_framework import permissions

class IsAdminorReadOnly(permissions.IsAdminUser):

    def has_permission(self,request,view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method=='GET' or admin_permission


class IsReviewUserorReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            # for get request only
            return True
        else:
            # check if review user is or not
            return obj.review_user==request.user or request.user.is_staff