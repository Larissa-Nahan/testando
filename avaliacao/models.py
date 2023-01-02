from django.db import models

# visibilidade dos criterios      
class Criterio(models.Model):
    VISIVEL = (
        ('chefes', "Chefes"),
        ('colaboradores', "Colaboradores"),
        ('todos', "Todos"),
    )

    criterio = models.CharField('Critério', max_length=50, unique=True)
    definicao = models.TextField('Definição')
    visivel = models.CharField('Visibilidade', max_length=20, choices=VISIVEL)

    def __str__(self):
        return self.criterio

    # ?
    # def get_avaliacoes(self):
    #     return self.avaliacao_set.all()

    class Meta:
        verbose_name = "Critério"

class Avaliacao(models.Model):
    ESCALA = (
        ('o', "Ótimo"),
        ('b', "Bom"),
        ('r', "Ruim"),
        ('i', "Insuficiente"),
    )

    avaliacao = models.TextField('Avaliação', null=False, blank=False, unique=True)
    criterio_avaliacao = models.ForeignKey(Criterio, on_delete=models.CASCADE, verbose_name='Critério')
    escala = models.CharField(max_length=20, choices=ESCALA)

    # usar dessa forma para poder fazer a exibicao dos dados necessarios na avaliacao
    def __str__(self) -> str:
        return f'{self.escala} - {self.avaliacao} - {self.criterio_avaliacao}'

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"