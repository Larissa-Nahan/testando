# Generated by Django 4.1.4 on 2022-12-21 14:43

import avaliar_usuario.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desempenho', '0007_alter_fatordesempenhodemerito_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao_usuario', models.DateField(blank=True, null=True)),
                ('avaliado', models.BooleanField(default=False)),
                ('liberar_avaliacao', models.BooleanField(default=False)),
                ('calculo', models.FloatField(default=0.0)),
                ('demeritos_chefes', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('visivel', 'chefes'), ('visivel', 'todos'), _connector='OR'), related_name='demeritos_chefes', to='desempenho.fatordesempenhodemerito')),
                ('demeritos_colaboradores', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('visivel', 'colaboradores'), ('visivel', 'todos'), _connector='OR'), related_name='demeritos_colaboradores', to='desempenho.fatordesempenhodemerito')),
                ('meritos_chefes', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('visivel', 'chefes'), ('visivel', 'todos'), _connector='OR'), related_name='meritos_chefes', to='desempenho.fatordesempenhomerito')),
                ('meritos_colaboradores', models.ManyToManyField(blank=True, limit_choices_to=models.Q(('visivel', 'colaboradores'), ('visivel', 'todos'), _connector='OR'), related_name='meritos_colaboradores', to='desempenho.fatordesempenhomerito')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nome', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliar_usuario.avaliarusuario')),
            ],
        ),
    ]
