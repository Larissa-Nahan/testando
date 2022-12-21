from django.utils import timezone
from django.db import models
from users.models import CustomUser
from avaliacao.models import Avaliacao
from django.db.models import Q


class AvaliarColaborador(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avaliado = models.BooleanField(default=False)
    calculo = models.FloatField(default=0.00)
    avaliacao_chefes = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_chefes', limit_choices_to=Q(visivel='chefes') | Q(visivel='todos'))
    avaliacao_colaboradores = models.ManyToManyField(Avaliacao, blank=True, related_name='avaliacao_colaboradores',  limit_choices_to=Q(visivel='colaboradores') | Q(visivel='todos'))
    data_avaliacao_usuario = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Avaliação do usuário {self.usuario}"

    def save(self, *args, **kwargs):
        super(Avaliacao, self).save(*args, **kwargs)
        self.avaliado = True
        self.data_avaliacao_usuario = timezone.now()
        super(Avaliacao, self).save(*args, **kwargs) 
