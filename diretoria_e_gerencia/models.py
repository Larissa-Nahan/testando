from django.db import models

class Diretoria(models.Model):
    diretoria = models.CharField(max_length=100, blank=False, null=False)
    sigla = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.diretoria

class Gerencia(models.Model):
    gerencia = models.CharField(max_length=100, blank=False, null=False)
    diretoria = models.ForeignKey(Diretoria, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = "Gerência"

    def __str__(self) -> str:
        return self.gerencia
