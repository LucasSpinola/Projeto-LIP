# Generated by Django 4.1.3 on 2022-12-12 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0018_alter_emprestimo_data_emprestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestado',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 15, 16, 15, 170659)),
        ),
    ]
