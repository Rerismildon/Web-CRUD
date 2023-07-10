# Generated by Django 4.1.7 on 2023-06-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SegundaAtividade', '0010_itenspedidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SegundaAtividade.cliente'),
        ),
    ]