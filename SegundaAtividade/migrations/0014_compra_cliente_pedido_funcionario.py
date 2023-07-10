# Generated by Django 4.1.7 on 2023-06-30 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SegundaAtividade', '0013_cliente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SegundaAtividade.cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SegundaAtividade.funcionario'),
        ),
    ]
