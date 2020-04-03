from rest_framework import permissions
from django.contrib.auth.models import Group

class GarantizarPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        gs = Group.objects.filter(name="Garantizar")
        if gs.exists():
            g = gs.first()
            return request.user in g.user_set.all()
        return False