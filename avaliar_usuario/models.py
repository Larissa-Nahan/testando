from datetime import datetime
from django.db import models
from desempenho.models import FatorDesempenhoMerito, FatorDesempenhoDemerito
from users.models import CustomUser


class AvaliarUsuario(models.Model):
    data_avaliacao_usuario = models.DateField(default=datetime.now, blank=True, null=True)
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    meritos = models.ManyToManyField(FatorDesempenhoMerito, blank=True)
    demeritos = models.ManyToManyField(FatorDesempenhoDemerito, blank=True)
    avaliado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Avaliação do usuário {self.usuario}"
