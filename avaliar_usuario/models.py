from django.db import models
from desempenho.models import FatorDesempenhoMerito, FatorDesempenhoDemerito
from users.models import CustomUser
from django.db.models import Q
import os

# salvar o documento comprovatorio no path designado
def folder_upload(self, filename):
    return (
        f"arquivos/{self.usuario}/{self.file}"
)

class AvaliarUsuario(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="nome", verbose_name='Usuário')
    avaliado = models.BooleanField(default=False)
    calculo = models.FloatField(default=0.00, verbose_name='Cálculo')
    data_avaliacao_usuario = models.DateField(blank=True, null=True, verbose_name='Data da última avaliação')
    liberar_avaliacao = models.BooleanField(default=False)  # campo usado na criacao do usuario - rever estrategia
    # [limit_choices_to=Q(visivel="")] limita os campos exibidos a partir da visibilidade
    meritos_chefes = models.ManyToManyField(FatorDesempenhoMerito, blank=True, related_name='meritos_chefes', limit_choices_to=Q(visivel='chefes') | Q(visivel='todos'), verbose_name='Méritos')
    meritos_colaboradores = models.ManyToManyField(FatorDesempenhoMerito, blank=True, related_name='meritos_colaboradores',  limit_choices_to=Q(visivel='colaboradores') | Q(visivel='todos'), verbose_name='Méritos')
    demeritos_chefes = models.ManyToManyField(FatorDesempenhoDemerito, blank=True, related_name='demeritos_chefes',  limit_choices_to=Q(visivel='chefes') | Q(visivel='todos'), verbose_name='Deméritos')
    demeritos_colaboradores = models.ManyToManyField(FatorDesempenhoDemerito, blank=True, related_name='demeritos_colaboradores',  limit_choices_to=Q(visivel='colaboradores') | Q(visivel='todos'), verbose_name='Deméritos')

    def __str__(self) -> str:
        return f"{self.usuario}"

    class Meta:
        verbose_name='Avaliar Usuário'

class Arquivo(models.Model):
    usuario = models.ForeignKey(AvaliarUsuario, on_delete=models.CASCADE)
    file = models.FileField(upload_to=folder_upload)

    def __str__(self) -> str:
        # retorna somente o nome do documento, sem a extensao
        basename, extension = os.path.splitext(os.path.basename(self.file.name)) 
        return basename