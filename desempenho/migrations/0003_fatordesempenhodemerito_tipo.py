# Generated by Django 4.1.4 on 2022-12-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desempenho', '0002_fatordesempenhomerito_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatordesempenhodemerito',
            name='tipo',
            field=models.CharField(choices=[('chefe', 'Chefe'), ('colaborador', 'Colaborador')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
