from django.contrib import admin
from .models import CustomUser
from avaliar_usuario.models import AvaliarUsuario
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

class AvaliarUsuarioInline(admin.TabularInline):
    model = AvaliarUsuario
    fields = ['liberar_avaliacao']
    can_delete = False

class UserAdminConfig(UserAdmin):
    inlines = [AvaliarUsuarioInline,]
    list_display = ('usuario', 'cpf', 'funcao', 'diretoria', 'gerencia')
    ordering = ['usuario', '-data_admissao_usuario',]
    search_fields = ('usuario', 'email')
    list_filter = ('usuario', 'email', 'efetivo', 'inativo')
    readonly_fields = ["data_criacao_usuario"]
    fieldsets = (
        (None, {'fields': ('usuario', 'cpf', 'matricula', 'email', 'inativo',)}),
        ('Dados do Usuário', {'fields': (
            'data_criacao_usuario',
            'data_admissao_usuario',
            ('efetivo', 'nivel', ),
            ('diretoria', 'gerencia',),
            'funcao',
            'classe',
            'setor',
            'cargo',

        )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'email', 'cpf', 'funcao', 'password1', 'password2'),
        }),
    )   
    
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.funcao == 'admin' or request.user.funcao == 'recursos_humanos':
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.funcao == 'admin' or request.user.funcao == 'recursos_humanos':
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.funcao == 'admin' or request.user.funcao == 'recursos_humanos':
            return True
        else:
            return False

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              '/static/admin/js/hide_attribute.js',
              '/static/admin/js/disable_on_inativo.js',
              '/static/admin/js/aval_usuario.js',
              '/static/admin/js/remove_delete.js',
              )


admin.site.register(CustomUser, UserAdminConfig)

admin.site.unregister(Group)
