# Generated by Django 4.1.3 on 2022-12-13 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0031_remove_carro_img_alter_emprestimo_data_emprestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_carro'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestado',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 8, 21, 44, 55799)),
        ),
    ]
