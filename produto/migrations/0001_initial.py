# Generated by Django 4.0.3 on 2022-04-21 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_ultima_modificacao', models.DateTimeField(auto_now=True, null=True)),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Nome')),
                ('url', models.SlugField(unique=True, verbose_name='URL')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('imagem_destaque', models.ImageField(blank=True, max_length=250, null=True, upload_to='produto/categoria/', verbose_name='Imagem de destaque')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'produto_categoria',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_ultima_modificacao', models.DateTimeField(auto_now=True, null=True)),
                ('ativo', models.BooleanField(default=False)),
                ('url', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.CharField(blank=True, max_length=2000, null=True)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('altura', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('largura', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('comprimento', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='produto.categoria')),
                ('unidade_medida', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='geral.unidademedida')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'produto',
            },
        ),
        migrations.CreateModel(
            name='ProdutoImagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_ultima_modificacao', models.DateTimeField(auto_now=True, null=True)),
                ('padrao', models.BooleanField(default=False)),
                ('imagem', models.ImageField(max_length=255, upload_to='produto/produto')),
                ('alt', models.CharField(blank=True, default='Imagem de produto', max_length=150, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'verbose_name': 'Imagem do produto',
                'verbose_name_plural': 'Imagens dos produtos',
                'db_table': 'produto_imagem',
            },
        ),
    ]
