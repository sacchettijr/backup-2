import re
from datetime import date
from django.db import models
from django.core import validators
from geral.models import Endereco
# from usuario.Manager import UsuarioManager
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class Usuario(AbstractBaseUser, PermissionsMixin):
	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'cpf_cnpj']

	# USUÁRIO
	username = models.CharField(
		'Usuário', max_length=50, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um usuário válido.'
				'Este valor deve conter apenas letras e números '
				'e os caracteres @/./+/-/_.',
				'invalid'
			)
		], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
	)
	is_staff = models.BooleanField('Equipe', default=False)
	is_active = models.BooleanField('Ativo', default=True)
	is_superuser  = models.BooleanField('Superusuário', default=False)
	is_anonymous = models.BooleanField('Anonimo', default=False)
	is_trusty = models.BooleanField('E-Mail confirmado', default=False)
	# PESSOAL
	TIPO_CHOICE = (
		('F', 'Física'),
		('J', 'Jurídica')
	)
	tipo = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICE, default='F')
	nome_fantasia = models.CharField('Nome Fantasia', max_length=255, blank=True, null=True)
	razao_social = models.CharField('Razão Social', max_length=255, blank=True, null=True)
	cpf_cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True)
	data_nascimento = models.DateField('Data de Nascimento', default=date.today, null=True, blank=True)
	SEXO_CHOICES = (
		("M", "Masculino"),
		("F", "Feminino"),
		("N", "Nenhuma das opções")
    )
	sexo = models.CharField('Sexo', max_length=1, null=True, blank=True, choices=SEXO_CHOICES, default='N')
	# CONTATO
	telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
	email = models.EmailField('E-Mail', unique=True)
	# LOG
	data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True, null=True, blank=True)
	data_ultima_modificacao = models.DateTimeField('Data da ultima modificação', auto_now=True, null=True, blank=True)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		db_table = 'usuario'

	def __str__(self):
		return self.username or self.get_short_name()

	def get_full_name(self):
		return str(self.nome_fantasia)

	def get_short_name(self):
		return str(self.nome_fantasia).split(" ")[0]

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])


class UsuarioEndereco(Endereco):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	padrao = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Endereço do usuário'
		verbose_name_plural = 'Endereços dos usuários'
		db_table = 'usuario_endereco'

	def __str__(self):
		informacao = 'Usuário: ' + str(
			self.usuario) + ' - Endereço: ' + self.rua + ', nº ' + self.numero + ', ' + self.bairro + ', CEP ' + self.cep
		if self.complemento:
			informacao = informacao + ', ' + self.complemento
		if self.referencia:
			informacao = informacao + ', ' + self.referencia
		return informacao

	def save(self):
		#  SÓ UM ENDEREÇO COMO PADRÃO
		if self.padrao:
			usuarios_enderecos = UsuarioEndereco.objects.filter(padrao=True, produto=self.endereco.pk)
			for usuario_endereco in usuarios_enderecos:
				usuario_endereco.padrao = False
				usuario_endereco.save()
		super().save()
