from rest_framework.permissions import BasePermission
from rest_framework.exceptions  import NotAcceptable


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
UPDATE_METHODS = ['PUT', 'PATCH']
CREATE_METHODS = ['POST', ]
DELETE_METHODS = ['DELETE', ]


class EventPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in CREATE_METHODS and request.data:
            # raise NotAcceptable('Solo puedes crear tus propios eventos')
            return request.user.id == request.data['owner']
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in UPDATE_METHODS + DELETE_METHODS:
            return obj.owner.id == request.user.id
        return True