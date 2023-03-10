# Generated by Django 4.1.4 on 2022-12-15 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diretoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diretoria', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerencia', models.CharField(max_length=100)),
                ('diretoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diretoria_e_gerencia.diretoria')),
            ],
            options={
                'verbose_name': 'Gerência',
            },
        ),
    ]
