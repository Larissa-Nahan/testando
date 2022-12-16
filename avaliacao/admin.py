from django.contrib import admin
from . import models

class AvaliacaoPermissions(admin.ModelAdmin):
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


admin.site.register(models.Categoria, AvaliacaoPermissions)
admin.site.register(models.Avaliacao, AvaliacaoPermissions)