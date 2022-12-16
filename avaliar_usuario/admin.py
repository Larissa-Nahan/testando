from django.contrib import admin
from .models import AvaliarUsuario

class AvaliarUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'avaliado')
    ordering = ('-data_avaliacao_usuario',)
    search_fields = (['usuario'])
    list_filter = ('usuario', 'data_avaliacao_usuario')
    readonly_fields = ["data_avaliacao_usuario"]
    fieldsets = (
        (None, {'fields': ('usuario', 
                            'meritos', 
                            'demeritos', 
                            'data_avaliacao_usuario',
                            'avaliado')}),
    )

    filter_horizontal = ('meritos', 'demeritos')

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

admin.site.register(AvaliarUsuario, AvaliarUsuarioAdmin)