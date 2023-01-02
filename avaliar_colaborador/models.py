from django.db import models
from users.models import CustomUser
from avaliacao.models import Avaliacao, Criterio


class AvaliarColaborador(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avaliado = models.BooleanField(default=False)
    calculo = models.FloatField(default=0.00)
    avaliacao_chefes = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_chefes')
    avaliacao_colaboradores = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_colaboradores')
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE, null=True, blank=True)
    data_avaliacao_colaborador = models.DateField(blank=True, null=True)
    liberar_avaliacao = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.usuario}"
    
    class Meta:
        verbose_name_plural = "Avaliar Colaboradores"