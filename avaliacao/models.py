from django.db import models
from django import forms
      
class Criterio(models.Model):
    criterio = models.CharField(max_length=50, unique=True)
    definicao = models.TextField()

    def __str__(self):
        return self.criterio

    def get_avaliacoes(self):
        return self.avaliacao_set.all()

class Avaliacao(models.Model):
    VISIVEL = (
        ('chefes', "Chefes"),
        ('colaboradores', "Colaboradores"),
        ('todos', "Todos"),
    )
    ESCALA = (
        ('o', "Otimo"),
        ('b', "Bom"),
        ('r', "Ruim"),
        ('i', "Insuficiente"),
    )

    avaliacao = models.TextField()
    criterio_avaliacao = models.OneToOneField(Criterio, on_delete=models.CASCADE)
    escala = models.CharField(max_length=20, choices=ESCALA)

    # visivel = models.CharField(max_length=20, choices=VISIVEL)

    def __str__(self) -> str:
        return f"Avaliação do {self.criterio_avaliacao.criterio}, escala: {self.escala}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"