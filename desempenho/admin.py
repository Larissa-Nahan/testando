from django.contrib import admin
from . import models

class DesempenhoPermissions(admin.ModelAdmin):
    list_display = ('fator', 'tipo')
    list_filter = ['tipo']

    def has_view_permission(self, request, obj=None):
        if request.user.funcao == 'admin':
            return True
        else:
            return False

    def has_add_permission(self, request, obj=None):
        if request.user.funcao == 'admin':
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.funcao == 'admin':
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.funcao == 'admin':
            return True
        else:
            return False

admin.site.register(models.FatorDesempenhoMerito, DesempenhoPermissions)
admin.site.register(models.FatorDesempenhoDemerito, DesempenhoPermissions)
