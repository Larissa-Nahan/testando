# Generated by Django 4.1.4 on 2022-12-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterio', models.CharField(max_length=50, unique=True)),
                ('definicao', models.TextField()),
                ('visivel', models.CharField(choices=[('chefes', 'Chefes'), ('colaboradores', 'Colaboradores'), ('todos', 'Todos')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.TextField()),
                ('escala', models.CharField(choices=[('o', 'Otimo'), ('b', 'Bom'), ('r', 'Ruim'), ('i', 'Insuficiente')], max_length=20)),
                ('criterio_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacao.criterio')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
    ]
