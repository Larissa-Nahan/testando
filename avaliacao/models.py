from django.db import models
from django import forms

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nome_categoria

class Avaliacao(models.Model):
    avaliacao_otima = models.TextField()
    avaliacao_boa = models.TextField()
    avaliacao_regular = models.TextField()
    avaliacao_insuficiente = models.TextField()
    categoria_avaliacao = models.OneToOneField(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"Avaliação da {self.categoria_avaliacao}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    # class Meta:
    #     widgets = {
    #         'avaliacao_otima': forms.RadioSelect(),
    #         'avaliacao_boa': forms.RadioSelect(),
    #         'avaliacao_regular': forms.RadioSelect(),
    #         'avaliacao_insuficiente': forms.RadioSelect(),
    #     }