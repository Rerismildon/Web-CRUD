# Generated by Django 4.1.7 on 2023-06-30 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SegundaAtividade', '0011_remove_cliente_endereco_endereco_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SegundaAtividade.pedido'),
        ),
    ]
