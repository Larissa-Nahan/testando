from django.db import models

TIPO = (
    ('chefe', "Chefe"),
    ('colaborador', "Colaborador"),
)

class FatorDesempenhoMerito(models.Model):
    fator = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO)

    class Meta:
        verbose_name = "Meritório"

    def __str__(self) -> str:
        return self.fator

class FatorDesempenhoDemerito(models.Model):
    fator = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO)

    class Meta:
        verbose_name = "Demeritório"

    def __str__(self) -> str:
        return self.fator