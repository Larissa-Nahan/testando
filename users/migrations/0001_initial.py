# Generated by Django 4.1.4 on 2022-12-15 14:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('diretoria_e_gerencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuario', models.CharField(max_length=150, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('matricula', models.CharField(blank=True, max_length=8)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('funcao', models.CharField(choices=[('presidente', 'Presidente'), ('diretor', 'Diretor'), ('gerente', 'Gerente'), ('chefe', 'Chefe'), ('colaborador', 'Colaborador'), ('cedido', 'Cedido a outro orgão'), ('recursos_humanos', 'Recursos Humanos'), ('admin', 'Administrador')], max_length=20)),
                ('classe', models.CharField(blank=True, choices=[('classe1', 'Classe 1'), ('classe2', 'Classe 2'), ('classe3', 'Classe 3')], max_length=20, null=True)),
                ('nivel', models.CharField(blank=True, choices=[('i', 'I'), ('ii', 'II'), ('iii', 'III'), ('iv', 'IV'), ('v', 'V'), ('vi', 'VI'), ('vii', 'VII'), ('viii', 'VIII'), ('ix', 'IX'), ('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], max_length=5, null=True)),
                ('setor', models.CharField(blank=True, max_length=50)),
                ('cargo', models.CharField(blank=True, max_length=50)),
                ('data_criacao_usuario', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('data_admissao_usuario', models.DateField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('inativo', models.BooleanField(default=False)),
                ('efetivo', models.BooleanField(default=False)),
                ('diretoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diretoria_e_gerencia.diretoria')),
                ('gerencia', smart_selects.db_fields.ChainedForeignKey(chained_field='diretoria', chained_model_field='diretoria', null=True, on_delete=django.db.models.deletion.CASCADE, to='diretoria_e_gerencia.gerencia')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
