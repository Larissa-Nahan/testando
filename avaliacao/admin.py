from django.contrib import admin
from .models import Avaliacao, Criterio

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao

class CriterioAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline,]
    # list_display = ['avaliacao']

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

admin.site.register(Criterio, CriterioAdmin)
admin.site.register(Avaliacao)