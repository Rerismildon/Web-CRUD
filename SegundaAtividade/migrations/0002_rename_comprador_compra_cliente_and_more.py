# Generated by Django 4.2.5 on 2023-09-11 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SegundaAtividade', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='comprador',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='data_compra',
            new_name='dataCompra',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='produto',
            new_name='idProduto',
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='preco_unitario',
            new_name='precoUnitario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8, 'Minimo de 8 digitos.'), django.core.validators.MaxLengthValidator(50, 'Maximo de 100 digitos.')]),
        ),
    ]
