from django.db import models
from users.models import CustomUser
from avaliacao.models import Avaliacao


class AvaliarColaborador(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avaliado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Avaliação do usuário {self.usuario}"
