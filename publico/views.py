from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, RedirectView
from produto.models import Categoria, Produto, ProdutoImagem
from publico.models import ItemCarrinho


class LoginAcessoView(LoginView):
	template_name = 'registration/login.html'


class LoginRecuperarSenhaView(TemplateView):
	template_name = 'registration/recuperar_senha.html'


class LoginCadastroView(TemplateView):
	template_name = 'registration/cadastro.html'


class PublicoIndexView(TemplateView):
	template_name = 'publico/index.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs


class PublicoCategoriaView(TemplateView):
	template_name = 'publico/produto_listagem.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		categoria_id = Categoria.objects.get(slug=kwargs['slug']).pk
		self.kwargs['categoria_nome'] = Categoria.objects.get(
			slug=kwargs['slug']).nome
		self.kwargs['produtos'] = Produto.objects.filter(
			categoria=categoria_id, ativo=True)
		self.kwargs['produtos_imagens'] = ProdutoImagem.objects.filter(
			padrao=True)
		return self.kwargs


class PublicoProdutoDetalheView(TemplateView):
	template_name = 'publico/produto_detalhe.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		produto = Produto.objects.get(slug=kwargs['slug'])
		print("PRINT AQUI >>>>>>>>>> " + str(produto.pk))
		self.kwargs['produto'] = produto
		self.kwargs['produtos_imagens'] = ProdutoImagem.objects.filter(
			produto=produto.pk, ativo=True)
		return self.kwargs


class CarrinhoItemCreateView(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
		if self.request.session.session_key is None:
			self.request.session.save()
		item_carrinho, criado = ItemCarrinho.objects.add.item(
			self.request.session.session_key, produto
		)
		if criado:
			messages.success(self.request, 'Produto adicionado com sucesso.')
		else:
			messages.success(self.request, 'Produto atualizado com sucesso.')
		return reverse('publico_carrinho')


class CarrinhoView(TemplateView):
	template_name = 'publico/carrinho.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs


class PublicoContatoView(TemplateView):
	template_name = 'publico/contato.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs


class PublicoSobreAEmpresaView(TemplateView):
	template_name = 'publico/sobre_a_empresa.html'

	def get_context_data(self, context=None, **kwargs):
		self.kwargs['categorias'] = Categoria.objects.filter(
			ativo=True)  # Navbar
		return self.kwargs
