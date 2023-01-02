from django.db import models
from users.models import CustomUser
from avaliacao.models import Avaliacao, Criterio


class AvaliarColaborador(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Usuário')
    avaliado = models.BooleanField(default=False)
    calculo = models.FloatField(default=0.00, verbose_name='Cálculo')
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE, null=True, blank=True, related_name='avaliacao_colaboradores', verbose_name='Critério')
    data_avaliacao_colaborador = models.DateField(blank=True, null=True, verbose_name='Data da última avaliação')
    liberar_avaliacao = models.BooleanField(default=False)  # campo usado na criacao do usuario - rever estrategia
    # precisa fazer como avaliar_usuario
    # [limit_choices_to=Q(visivel="")] limita os campos exibidos a partir da visibilidade
    avaliacao_chefes = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_chefes', verbose_name='')
    avaliacao_colaboradores = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_colaboradores', verbose_name='')

    def __str__(self) -> str:
        return f"{self.usuario}"
    
    class Meta:
        verbose_name_plural = "Avaliar Colaboradores"