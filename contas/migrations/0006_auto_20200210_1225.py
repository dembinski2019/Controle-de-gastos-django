# Generated by Django 3.0.3 on 2020-02-10 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_auto_20200209_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria'),
        ),
    ]
