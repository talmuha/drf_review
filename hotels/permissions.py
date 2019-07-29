from rest_framework.permissions import BasePermission
import datetime

class Booker(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False

class BackToTheFuture(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.check_in >= datetime.date.today():
            return True
        else:
            return False
