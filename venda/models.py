from django.db import models
from geral.models import Endereco, Base
from produto.models import Produto


class Venda(Base):
    desconto_total = models.DecimalField(max_digits=15, decimal_places=4)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=4)
    valor_compra = models.DecimalField(max_digits=15, decimal_places=4)
    valor_frete = models.DecimalField(max_digits=15, decimal_places=4)
    valor_total = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
        db_table = 'venda'

    def __str__(self):
        return str(self.pk) + ': R$' + str(self.valor_total)


class ItemVenda(Base):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=4)
    quantidade = models.PositiveIntegerField(default=1)
    total_por_item = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        verbose_name = 'Item da venda'
        verbose_name_plural = 'Itens das vendas'
        db_table = 'item_venda'

    def __str__(self):
        return str(self.venda)


class Entrega(Endereco):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    data_agendada = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
        db_table = 'entregas'

    def __str__(self):
        return 'Entrega: {}, Venda: {}'.format(self.pk, self.venda)
