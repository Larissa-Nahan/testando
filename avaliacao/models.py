from django.db import models
from django import forms
      
class Criterio(models.Model):
    VISIVEL = (
        ('chefes', "Chefes"),
        ('colaboradores', "Colaboradores"),
        ('todos', "Todos"),
    )

    criterio = models.CharField(max_length=50, unique=True)
    definicao = models.TextField()
    visivel = models.CharField(max_length=20, choices=VISIVEL)

    def __str__(self):
        return self.criterio

    def get_avaliacoes(self):
        return self.avaliacao_set.all()

class Avaliacao(models.Model):
    ESCALA = (
        ('o', "Otimo"),
        ('b', "Bom"),
        ('r', "Ruim"),
        ('i', "Insuficiente"),
    )

    avaliacao = models.TextField(null=False, blank=False)
    criterio_avaliacao = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    escala = models.CharField(max_length=20, choices=ESCALA)

    # def __str__(self):
    #     return self.get_escala_display()
    def __str__(self) -> str:
        return f'{self.escala} - {self.avaliacao} - {self.criterio_avaliacao}'

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"