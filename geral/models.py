from django.db import models


class Base(models.Model):
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_ultima_modificacao = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class Pais(Base):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        db_table = 'pais'

    def __str__(self):
        return self.nome + '(' + self.sigla + ')'


class Estado(Base):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estado'

    def __str__(self):
        return self.nome + ' - ' + self.pais.sigla


class Cidade(Base):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        db_table = 'cidade'

    def __str__(self):
        return self.nome + ' - ' + self.estado.sigla


class UnidadeMedida(Base):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Unidade de medida'
        verbose_name_plural = 'Unidades de medidas'
        db_table = 'unidade_medida'

    def __str__(self):
        return self.nome + ' - ' + self.sigla


class Endereco(Base):
    padrao = models.BooleanField(verbose_name='Padrão', default=False)
    rua = models.CharField(verbose_name='Rua', max_length=255, null=False, blank=False)
    numero = models.CharField(verbose_name='Número', max_length=10, null=False, blank=False)
    complemento = models.CharField(verbose_name='Complemento', max_length=255, null=True, blank=True)
    referencia = models.CharField(verbose_name='Referência', max_length=255, null=True, blank=True)
    cep = models.CharField(verbose_name='CEP', max_length=10, null=False, blank=False)
    bairro = models.CharField(verbose_name='Bairro', max_length=200, null=False, blank=False)
    cidade = models.ForeignKey(Cidade, verbose_name='Cidade', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
        abstract = True
