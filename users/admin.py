from django.contrib import admin
from .models import CustomUser
from avaliar_usuario.models import AvaliarUsuario
from avaliar_colaborador.models import AvaliarColaborador
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

# exibir o campo de avaliar usuario [checkbox] ao cadastrar um usuario
class AvaliarUsuarioInline(admin.TabularInline):
    model = AvaliarUsuario
    fields = ['liberar_avaliacao', 'avaliado']
    readonly_fields = ['avaliado']
    can_delete = False  # nao funciona??? necessario usar js para conseguir impedir a delecao

# exibir o campo de avaliar colaborador [checkbox] ao cadastrar um usuario
class AvaliarColaboradorInline(admin.TabularInline):
    model = AvaliarColaborador
    fields = ['liberar_avaliacao', 'avaliado']
    readonly_fields = ['avaliado']
    can_delete = False  # nao funciona??? necessario usar js para conseguir impedir a delecao

class UserAdminConfig(UserAdmin):
    inlines = [AvaliarUsuarioInline, AvaliarColaboradorInline]
    list_display = ('usuario', 'cpf', 'funcao', 'diretoria', 'gerencia')
    ordering = ['usuario', '-data_admissao_usuario',]
    search_fields = ('usuario', 'email')
    list_filter = ('usuario', 'email', 'efetivo', 'inativo')
    readonly_fields = ["data_criacao_usuario"]

    # campos exibidos ao editar um usuario  
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

    # campos exibidos ao criar um usuario
    add_fieldsets = (
        (None, {'fields': ('usuario', 'cpf', 'matricula', 'email',)}),
        ('Dados do Usuário', {
            'classes': ('wide',),
            'fields': (
                        # 'data_admissao_usuario',
                        # ('efetivo', 'nivel', ),
                        # ('diretoria', 'gerencia',),
                        'funcao',  
                        # 'classe',
                        # 'setor',
                        # 'cargo',
                        'password1', 
                        'password2'),
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
              '/static/admin/js/hide_attribute.js',  # habilitar campo nivel se efetivo selecionado
              '/static/admin/js/disable_on_inativo.js',  # inativar campos se inativo for selecionado
              '/static/admin/js/aval_usuario.js',  # check os checkboxes [liberar_avaliacao] ao salvar o usuario - rever estrategia
              '/static/admin/js/remove_delete.js',  # remove a capacidade de deletar os campos do inline
              )


admin.site.register(CustomUser, UserAdminConfig)

admin.site.unregister(Group)
