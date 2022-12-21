from django.db import models
from desempenho.models import FatorDesempenhoMerito, FatorDesempenhoDemerito
from users.models import CustomUser
from django.db.models import Q

def folder_upload(self, filename):
    extension = filename.split(".")[-1]
    return (
        f"arquivos/{self.usuario}/{self.file}.{extension}"
)

class AvaliarUsuario(models.Model):
    data_avaliacao_usuario = models.DateField(blank=True, null=True)
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="nome")
    meritos_chefes = models.ManyToManyField(FatorDesempenhoMerito, blank=True, related_name='meritos_chefes', limit_choices_to=Q(visivel='chefes') | Q(visivel='todos'))
    meritos_colaboradores = models.ManyToManyField(FatorDesempenhoMerito, blank=True, related_name='meritos_colaboradores',  limit_choices_to=Q(visivel='colaboradores') | Q(visivel='todos'))
    demeritos_chefes = models.ManyToManyField(FatorDesempenhoDemerito, blank=True, related_name='demeritos_chefes',  limit_choices_to=Q(visivel='chefes') | Q(visivel='todos'))
    demeritos_colaboradores = models.ManyToManyField(FatorDesempenhoDemerito, blank=True, related_name='demeritos_colaboradores',  limit_choices_to=Q(visivel='colaboradores') | Q(visivel='todos'))
    avaliado = models.BooleanField(default=False)
    liberar_avaliacao = models.BooleanField(default=False)
    calculo = models.FloatField(default=0.00)

    def __str__(self) -> str:
        return f"{self.usuario}"

class Arquivo(models.Model):
    usuario = models.ForeignKey(AvaliarUsuario, on_delete=models.CASCADE)
    file = models.FileField(upload_to=folder_upload, blank=True)

    def __str__(self) -> str:
        return f"{self.file}"