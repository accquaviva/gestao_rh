# Generated by Django 2.1.3 on 2018-11-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20181127_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome Funcionario'),
        ),
    ]
