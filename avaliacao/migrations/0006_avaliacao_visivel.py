# Generated by Django 4.1.4 on 2022-12-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0005_alter_avaliacao_avaliacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='visivel',
            field=models.CharField(choices=[('chefes', 'Chefes'), ('colaboradores', 'Colaboradores'), ('todos', 'Todos')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
