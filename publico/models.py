from django.db import models
from geral.models import Base
from produto.models import Produto


class ItemCarrinhoManager(models.Manager):

    def adicionar_item(self, key_carrinho, produto):
        if self.filter(key_carrinho=key_carrinho, produto=produto).exists():
            criado = False
            item_carrinho = self.get(key_carrinho=key_carrinho, produto=produto)
            item_carrinho.quantidade = item_carrinho.quantidade + 1
            item_carrinho.save()
        else:
            criado = True
            item_carrinho = ItemCarrinho.objects.create(
                key_carrinho=key_carrinho,
                produto=produto,
                valor=produto.valor_unitario
            )
        return item_carrinho, criado


class ItemCarrinho(Base):
    key_carrinho = models.CharField('Chave do carrinho', max_length=40, db_index=True)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=4)
    quantidade = models.PositiveIntegerField(default=1)
    total_por_item = models.DecimalField(max_digits=15, decimal_places=4)

    objects = ItemCarrinhoManager()

    class Meta:
        verbose_name = 'Item do'
        verbose_name_plural = 'Itens dos carrinhos'
        db_table = 'item_carrinho'
        unique_together = (('key_carrinho', 'produto'),)

    def __str__(self):
        return 'Key: {}, Item: {}, Quantidade: {}, Total: {}'.format(self.key_carrinho, self.produto, self.quantidade,
                                                                     self.total_por_item)
