# Generated by Django 4.1.5 on 2023-01-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterio',
            options={'verbose_name': 'Critério'},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliacao',
            field=models.TextField(unique=True, verbose_name='Avaliação'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='criterio_avaliacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacao.criterio', verbose_name='Critério'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='escala',
            field=models.CharField(choices=[('o', 'Ótimo'), ('b', 'Bom'), ('r', 'Ruim'), ('i', 'Insuficiente')], max_length=20),
        ),
        migrations.AlterField(
            model_name='criterio',
            name='criterio',
            field=models.CharField(max_length=50, unique=True, verbose_name='Critério'),
        ),
        migrations.AlterField(
            model_name='criterio',
            name='definicao',
            field=models.TextField(verbose_name='Definição'),
        ),
        migrations.AlterField(
            model_name='criterio',
            name='visivel',
            field=models.CharField(choices=[('chefes', 'Chefes'), ('colaboradores', 'Colaboradores'), ('todos', 'Todos')], max_length=20, verbose_name='Visibilidade'),
        ),
    ]
