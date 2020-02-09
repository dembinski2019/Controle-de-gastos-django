# Generated by Django 3.0.3 on 2020-02-09 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
