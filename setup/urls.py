from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from publico.views import CarrinhoItemCreateView, PublicoIndexView, PublicoCategoriaView, PublicoProdutoDetalheView, PublicoContatoView, \
	PublicoSobreAEmpresaView, LoginRecuperarSenhaView, LoginCadastroView, CarrinhoView

router = routers.DefaultRouter()

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	# LOGIN
	path('login/', LoginView.as_view(), name='publico_login_sm'),
	path('accounts/login/', LoginView.as_view(), name='publico_login'),
	path('accounts/recuperar-senha/', LoginRecuperarSenhaView.as_view(), name='publico_recuperar_senha'),
	path('accounts/cadastro/', LoginCadastroView.as_view(), name='publico_cadastro'),
	path('accounts/logout/', LogoutView.as_view(), name='publico_logout'),
	# PUBLICO
	path('', PublicoIndexView.as_view(), name='publico_index'),
	path('categoria/<slug:slug>/', PublicoCategoriaView.as_view(), name='publico_categoria'),
	path('produto/<slug:slug>/', PublicoProdutoDetalheView.as_view(), name='publico_produto'),
	# path('carrinho/', CarrinhoView.as_view(), name='publico_carrinho'),
	path('carrinho/', include('publico.urls'), name='publico_carrinho'),
	path('contato/', PublicoContatoView.as_view(), name='publico_contato'),
	path('sobre-a-empresa/', PublicoSobreAEmpresaView.as_view(), name='publico_sobre_a_empresa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)