
from django.urls import path
from publico.views import CarrinhoView


urlpatterns = [
	path('carrinho/', CarrinhoView.as_view(), name='publico_carrinho'),
]
