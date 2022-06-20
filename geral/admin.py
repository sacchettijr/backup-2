from django.contrib import admin
from geral.models import Pais, Estado, Cidade, UnidadeMedida


class PaisAdmin(admin.ModelAdmin):
    ordering = ['pk']
    list_display = ['pk', 'nome', 'sigla']
    list_display_links = ['pk', 'nome']


admin.site.register(Pais, PaisAdmin)


class EstadoAdmin(admin.ModelAdmin):
    ordering = ['pais', 'nome']
    list_display = ['pk', 'nome', 'sigla', 'pais']
    list_display_links = ['pk', 'nome']


admin.site.register(Estado, EstadoAdmin)


class CidadeAdmin(admin.ModelAdmin):
    model = Cidade
    ordering = ['pk']
    list_display = ['pk', 'nome', 'estado']
    list_display_links = ['pk', 'nome']
    list_filter = ('estado',)


admin.site.register(Cidade, CidadeAdmin)


class UnidadeMedidaAdmin(admin.ModelAdmin):
    ordering = ['pk']
    list_display = ['pk', 'nome', 'sigla']
    list_display_links = ['pk', 'nome']


admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)
