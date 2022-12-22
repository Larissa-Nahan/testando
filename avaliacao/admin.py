from django.contrib import admin
from .models import Avaliacao, Criterio
from django.db import models

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['criterio', 'escala_avaliacao']
    search_fields = ['criterio_avaliacao__criterio']

    @admin.display(description='Avaliacao')
    def criterio(self, obj):
        criterio = obj.criterio_avaliacao
        return f"Avaliação do {criterio}"

    @admin.display(description='Escala')
    def escala_avaliacao(self, obj):
        escala = obj.get_escala_display().upper()
        return f"{escala}"

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 4
    max_num = 4
    can_delete = False

class CriterioAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline,]
    model = Avaliacao
    list_display = ['criterio', 'visibilidade']
    list_filter = ['visivel']
    search_fields = ['criterio']

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
              '/static/admin/js/remove_delete.js',
              '/static/admin/js/set_escala.js',
              )

admin.site.register(Criterio, CriterioAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)