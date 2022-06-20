from django.contrib import admin
from venda.models import Venda, ItemVenda, Entrega


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [
        ItemVendaInline,
    ]


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    pass
