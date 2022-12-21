from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from smart_selects.db_fields import ChainedForeignKey
from diretoria_e_gerencia.models import Diretoria, Gerencia


class CustomAccountManager(BaseUserManager):
    def create_user(self, cpf, email, usuario, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, usuario=usuario, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, cpf, email, usuario, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('inativo', False)
        other_fields.setdefault('funcao', 'admin')

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_superuser=True'))

        return self.create_user(cpf, email, usuario, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    FUNCAO = (
        ('presidente', "Presidente"),
        ('diretor', "Diretor"),
        ('gerente', "Gerente"),
        ('chefe', "Chefe"),
        ('colaborador', "Colaborador"),
        ('cedido', "Cedido a outro orgão"),
        ('recursos_humanos', "Recursos Humanos"),
        ('admin', "Administrador"),
    )

    CLASSE = (
        ('classe1', "Classe 1"),
        ('classe2', "Classe 2"),
        ('classe3', "Classe 3"),
    )

    NIVEL = (
        ('i', "I"),
        ('ii', "II"),
        ('iii', "III"),
        ('iv', "IV"),
        ('v', "V"),
        ('vi', "VI"),
        ('vii', "VII"),
        ('viii', "VIII"),
        ('ix', "IX"),
        ('x', "X"),
        ('xi', "XI"),
        ('xii', "XII"),
    )
    
    usuario = models.CharField(max_length=150, unique=True)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)
    matricula = models.CharField(max_length=8, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    
    funcao = models.CharField(max_length=20, choices=FUNCAO)
    classe = models.CharField(max_length=20, choices=CLASSE, blank=True, null=True)
    nivel = models.CharField(max_length=5, choices=NIVEL, blank=True, null=True)
    setor = models.CharField(max_length=50, blank=True)
    cargo = models.CharField(max_length=50, blank=True)


    data_criacao_usuario = models.DateField(auto_now_add=True)
    data_admissao_usuario = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    inativo = models.BooleanField(default=False)
    efetivo = models.BooleanField(default=False)

    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE, null=True)
    gerencia = ChainedForeignKey(
        Gerencia,
        chained_field="diretoria",
        chained_model_field="diretoria",
        show_all=False,
        auto_choose=False,
        sort=True, 
        null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'usuario']

    def __str__(self):
        return self.usuario

    def get_usuarios(self):
        return self.nome.all()
