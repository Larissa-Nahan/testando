from django.utils import timezone
from django.contrib import admin
from .models import AvaliarColaborador
from avaliacao.models import Avaliacao, Criterio
from django.db import models
from django.forms import CheckboxSelectMultiple

class AvaliarColaboradorAdmin(admin.ModelAdmin):
    model = AvaliarColaborador
    list_display = ['usuario', 'data_avaliacao_colaborador', 'avaliado']
    ordering = ['-data_avaliacao_colaborador',]
    search_fields = ['usuario']
    list_filter = ['usuario', 'data_avaliacao_colaborador']
    readonly_fields = ["usuario", "data_avaliacao_colaborador"]

    # fazer os campos ManyToManyField serem exibidos como checkbox
    # deixar assim e mudar com css/js ou conseguir uma forma de fazer o radio funcionar
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('', {'fields': ['usuario', 'data_avaliacao_colaborador', 'calculo', 'criterio']}),
            ('Critérios', {'fields': ['avaliacao_chefes',]}),
            ]
        # necessita fazer o mesmo que foi feito com avaliar_usuario
        # a partir do tipo do usuario selecionado, os campos sao exibidos
        # if obj:
            # if obj.usuario.funcao == 'chefe':
            #     fieldsets[0][1]['fields'].append('avaliacao_chefes')
            # else:
            #     fieldsets[0][1]['fields'].append('avaliacao_colaboradores')
            
        return fieldsets

    # ao salvar a data de avaliacao eh definida de o status muda para avaliado
    def save_model(self, request, obj, form, change):
        obj.avaliado = True
        obj.data_avaliacao_colaborador = timezone.now()
        super().save_model(request, obj, form, change)

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
              '/static/admin/js/perguntas.js',  # exibe o conteudo dos criterios a partir do dropdown
              )


admin.site.register(AvaliarColaborador, AvaliarColaboradorAdmin)
