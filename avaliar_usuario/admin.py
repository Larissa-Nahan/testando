from django.utils import timezone
from django.contrib import admin
from .models import AvaliarUsuario, Arquivo
from django.db import models
from django.forms import CheckboxSelectMultiple

class ArquivoInline(admin.StackedInline):
    model = Arquivo
    extra = 1


class AvaliarUsuarioAdmin(admin.ModelAdmin):
    inlines = [ArquivoInline]
    model = AvaliarUsuario
    list_display = ('usuario', 'data_avaliacao_usuario', 'avaliado')
    ordering = ['usuario__usuario',]
    search_fields = ['usuario__usuario']
    list_filter = ('usuario__usuario', 'data_avaliacao_usuario')
    readonly_fields = ['usuario', 'data_avaliacao_usuario']

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('', {'fields': ['usuario', 'data_avaliacao_usuario', 'calculo',]}),
            ]
        
        if obj:
            if obj.usuario.funcao == 'chefe':
                fieldsets[0][1]['fields'].append('meritos_chefes')
                fieldsets[0][1]['fields'].append('demeritos_chefes')
            else:
                fieldsets[0][1]['fields'].append('meritos_colaboradores')
                fieldsets[0][1]['fields'].append('demeritos_colaboradores')
            
        return fieldsets
    
    def save_model(self, request, obj, form, change):
        obj.avaliado = True
        obj.data_avaliacao_usuario = timezone.now()
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.funcao == 'admin':
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.funcao == 'admin' or request.user.funcao == 'recursos_humanos':
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
              '/static/admin/js/calc_performance.js',
              )

admin.site.register(AvaliarUsuario, AvaliarUsuarioAdmin)