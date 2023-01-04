from django.contrib import admin
from .models import AdicionarEdital
from django.db import models
from django.forms import CheckboxSelectMultiple

class AdicionarEditalAdmin(admin.ModelAdmin):
    model = AdicionarEdital
    list_display = (
                    'edital', 
                    'data_inicio', 
                    'data_termino',
                    # 'andamento',
                    )
    fields = ( 
            'edital',
            'data_inicio', 
            'data_termino',
            'arquivo',
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
            #   '/static/admin/js/calc_performance.js',  # calcula os meritos e demeritos
              )

admin.site.register(AdicionarEdital, AdicionarEditalAdmin)