# Generated by Django 4.1.3 on 2022-12-11 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('carros', '0005_categoria_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='data_alugado',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='nome_alugado',
        ),
        migrations.RemoveField(
            model_name='carro',
            name='tempo_aluguel',
        ),
        migrations.AlterField(
            model_name='carro',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carros.categoria'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario'),
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestado', models.DateField(blank=True, null=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('avalicao', models.CharField(choices=[('P', 'Péssimo'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carros.carro')),
                ('nome_emprestado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
    ]
