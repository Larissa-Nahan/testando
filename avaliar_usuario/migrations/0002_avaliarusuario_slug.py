# Generated by Django 4.1.4 on 2022-12-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliar_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliarusuario',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
