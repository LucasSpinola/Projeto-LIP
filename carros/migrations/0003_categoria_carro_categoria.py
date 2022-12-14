# Generated by Django 4.1.3 on 2022-11-25 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0002_alter_carro_data_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='carros.categoria'),
            preserve_default=False,
        ),
    ]
