# Generated by Django 4.1.3 on 2022-12-11 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0012_alter_emprestimo_data_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestado',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 18, 4, 54, 304272)),
        ),
    ]
