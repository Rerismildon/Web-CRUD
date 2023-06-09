# Generated by Django 4.1.7 on 2023-06-26 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SegundaAtividade', '0008_pedido_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SegundaAtividade.categoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SegundaAtividade.fornecedor'),
        ),
    ]
