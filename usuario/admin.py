from tokenize import group
from django.contrib import admin
from usuario.forms import UserAdminCreationForm, UserAdminForm
from usuario.models import Usuario, UsuarioEndereco
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UsuarioEnderecoInline(admin.TabularInline):
    model = UsuarioEndereco


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
	form = UserAdminForm
	fieldsets = (
		("Usuário", {
			"fields": (
				('is_active', 'is_staff', 'is_superuser', 'is_trusty', 'is_anonymous'),
				'username', ('password'), 'groups', 'user_permissions'
			),
		}),
		("Informações básicas", {
			"fields": (
				'tipo',
				('nome_fantasia', 'razao_social'), 
				'cpf_cnpj', 'data_nascimento', 'sexo',
				('telefone', 'email'), 'last_login'
			),
		}),
	)
	add_form = UserAdminCreationForm
	add_fieldsets = (
		("Usuário", {
			"fields": (
				('is_active', 'is_staff', 'is_superuser', 'is_trusty', 'is_anonymous'),
				'username', ('password1', 'password2'), 'groups', 'user_permissions'
			),
		}),
		("Informações básicas", {
			"fields": (
				'tipo',
				('nome_fantasia', 'razao_social'), 
				'cpf_cnpj', 'data_nascimento', 'sexo',
				('telefone', 'email')
			)
		})
	)
	
	list_display = [
		'username', 'is_staff', 'is_active', 'nome_fantasia', 'cpf_cnpj', 'telefone', 'email', 'data_cadastro'
	]

	inlines = [
		UsuarioEnderecoInline,
	]


@admin.register(UsuarioEndereco)
class UsuarioEnderecoAdmin(admin.ModelAdmin):
	pass
