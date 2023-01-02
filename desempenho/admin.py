from django.contrib import admin
from . import models

class DesempenhoPermissions(admin.ModelAdmin):
    list_display = ['fator', 'visibilidade']
    list_filter = ['visivel']

    # forma de display dos dados (sobrescreve como esta no models)
    @admin.display(description='Visibilidade')
    def visibilidade(self, obj):
        visivel_para = obj.visivel.upper()
        return f"Fator visível para {visivel_para}"

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
