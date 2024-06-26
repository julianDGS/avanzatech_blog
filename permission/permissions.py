from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import APIException

from user.models import User
from .models import CategoryName, PermissionName, PostPermission

class RetrieveNotAccessException(APIException):
    status_code = 404
    default_detail = {'error': 'Cannot access to this post.'}
    

class AuthenticateAndPostEdit(BasePermission):

    def __init__(self, like_comment_view_set=False):
        self.like_comment_view_set = like_comment_view_set

    def has_permission(self, request, view):
        if not (view.action == 'create' or view.action == 'partial_update' or (self.like_comment_view_set and view.action == 'destroy')):
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['HEAD', 'OPTIONS']:
            return True
        user: User = request.user
        author: User = User.objects.get(id=obj.author.id)
        post_permissions = PostPermission.objects.filter(post_id=obj.id)
        post_permissions_dict = {permission.category.name: permission.permission.name for permission in post_permissions}
        if self.like_comment_view_set or request.method == 'GET':
            if not user.is_authenticated:
                if post_permissions_dict[str(CategoryName.PUBLIC)] != str(PermissionName.NONE):
                    return True
                else:
                    raise RetrieveNotAccessException()
            if user.is_admin:
                return True
            if user.id == author.id:
                if post_permissions_dict[str(CategoryName.AUTHOR)] != str(PermissionName.NONE):
                    return True
                elif self.like_comment_view_set:
                    return False
                else:
                    raise RetrieveNotAccessException()
            if user.team.id == author.team.id:
                if post_permissions_dict[str(CategoryName.TEAM)] != str(PermissionName.NONE):
                    return True
                elif self.like_comment_view_set:
                    return False
                else:
                    raise RetrieveNotAccessException()
            if post_permissions_dict[str(CategoryName.AUTHENTICATE)] != str(PermissionName.NONE):
                return True
            elif self.like_comment_view_set:
                return False
            else:
                raise RetrieveNotAccessException()
        else:
            if not user.is_authenticated:
                if post_permissions_dict[str(CategoryName.PUBLIC)] == str(PermissionName.EDIT):
                    return True
                else:
                    return False 
            if user.is_admin:
                return True
            if user.id == author.id:
                if post_permissions_dict[str(CategoryName.AUTHOR)] == str(PermissionName.EDIT):
                    return True
                else:
                    return False
            if user.team.id == author.team.id:
                if post_permissions_dict[str(CategoryName.TEAM)] == str(PermissionName.EDIT):
                    return True
                else:
                    return False
            if post_permissions_dict[str(CategoryName.AUTHENTICATE)] == str(PermissionName.EDIT):
                return True
        return False


class AuthenticateAndLikePermission(AuthenticateAndPostEdit):
    def __init__(self):
        super().__init__(like_comment_view_set=True)

class AuthenticateAndCommentPermission(AuthenticateAndPostEdit):
    def __init__(self):
        super().__init__(like_comment_view_set=True)