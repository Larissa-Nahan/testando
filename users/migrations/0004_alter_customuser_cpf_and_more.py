# Generated by Django 4.1.5 on 2023-01-02 14:12

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('diretoria_e_gerencia', '0002_alter_gerencia_gerencia'),
        ('users', '0003_alter_customuser_data_criacao_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='data_admissao_usuario',
            field=models.DateField(blank=True, null=True, verbose_name='Data Admissão Usuário'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='data_criacao_usuario',
            field=models.DateField(auto_now_add=True, verbose_name='Data Criação Usuário'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='funcao',
            field=models.CharField(choices=[('presidente', 'Presidente'), ('diretor', 'Diretor'), ('gerente', 'Gerente'), ('chefe', 'Chefe'), ('colaborador', 'Colaborador'), ('cedido', 'Cedido a outro orgão'), ('recursos_humanos', 'Recursos Humanos'), ('admin', 'Administrador')], max_length=20, verbose_name='Função'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gerencia',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='diretoria', chained_model_field='diretoria', null=True, on_delete=django.db.models.deletion.CASCADE, to='diretoria_e_gerencia.gerencia', verbose_name='Gerência'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='matricula',
            field=models.CharField(blank=True, max_length=8, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nivel',
            field=models.CharField(blank=True, choices=[('i', 'I'), ('ii', 'II'), ('iii', 'III'), ('iv', 'IV'), ('v', 'V'), ('vi', 'VI'), ('vii', 'VII'), ('viii', 'VIII'), ('ix', 'IX'), ('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], max_length=5, null=True, verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='usuario',
            field=models.CharField(max_length=150, unique=True, verbose_name='Usuário'),
        ),
    ]
