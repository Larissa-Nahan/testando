# Generated by Django 4.1.4 on 2022-12-16 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliar_colaborador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliarcolaborador',
            name='avaliacao',
        ),
    ]
