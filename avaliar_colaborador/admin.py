from django.contrib import admin
from .models import AvaliarColaborador

from django.db import models
from django.forms import CheckboxSelectMultiple

class AvaliarColaboradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_avaliacao_usuario', 'avaliado')
    ordering = ('-data_avaliacao_usuario',)
    search_fields = (['usuario'])
    list_filter = ('usuario', 'data_avaliacao_usuario')
    readonly_fields = ["data_avaliacao_usuario"]

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('', {'fields': ['usuario', 'data_avaliacao_usuario', 'calculo']}),
            ]
        
        if obj:
            if obj.usuario.funcao == 'chefe':
                fieldsets[0][1]['fields'].append('avaliacao_chefes')
                fieldsets[0][1]['fields'].append('avaliacao_chefes')
            else:
                fieldsets[0][1]['fields'].append('avaliacao_colaboradores')
                fieldsets[0][1]['fields'].append('avaliacao_colaboradores')
            
        return fieldsets

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.funcao == 'admin' or request.user.funcao == 'recursos_humanos':
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

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              '/static/admin/js/hide_attribute.js',
              '/static/admin/js/disable_on_inativo.js',
              )


admin.site.register(AvaliarColaborador, AvaliarColaboradorAdmin)
