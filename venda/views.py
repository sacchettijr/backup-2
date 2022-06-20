from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from produto.models import Produto
from venda.models import ItemCarrinho


class ItemCarrinhoCreateView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        item_carrinho, created = ItemCarrinho.objects.add.item(self.request.session.session_key, produto)

        if created:
            messages.success(self.request, 'Produto adicionado com sucesso.')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso.')
        return produto.get_absolute.url()
