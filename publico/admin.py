from django.contrib import admin

from publico.models import ItemCarrinhoManager, ItemCarrinho


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    pass
