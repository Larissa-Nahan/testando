from django.contrib import admin
from .models import Avaliacao, Criterio
from django.db import models

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['criterio', 'escala_avaliacao']
    search_fields = ['criterio_avaliacao__criterio']

    # forma de display dos dados (sobrescreve como esta no models)
    @admin.display(description='Avaliacao')
    def criterio(self, obj):
        criterio = obj.criterio_avaliacao
        return f"Avaliação do Critério {criterio}"

    @admin.display(description='Escala')
    def escala_avaliacao(self, obj):
        escala = obj.get_escala_display().upper()
        return f"{escala}"

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

# exibir o conteudo da avaliacao na hora de cadastrar um criterio
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 4  # inicia com 4 campos (usa js para ja defini-los, mas podem ser mudados... - repensar)
    max_num = 4  # limita a 4 campos [o, b, r, i]
    can_delete = False  # nao funciona??? necessario usar js para conseguir impedir a delecao

class CriterioAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline,]
    model = Avaliacao
    list_display = ['criterio', 'visibilidade']
    list_filter = ['visivel']
    search_fields = ['criterio']

    # forma de display dos dados (sobrescreve como esta no models)
    @admin.display(description='Visibilidade')
    def visibilidade(self, obj):
        visivel_para = obj.visivel.upper()
        return f"Critério visível para {visivel_para}"

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

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              '/static/admin/js/remove_delete.js',  # remove a capacidade de deletar os campos do inline
              '/static/admin/js/set_escala.js',  # insere as escalas nos dropdowns [o, b, r, i]
              )

admin.site.register(Criterio, CriterioAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)