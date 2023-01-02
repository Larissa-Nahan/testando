from django.db import models

VISIVEL = (
    ('chefes', "Chefes"),
    ('colaboradores', "Colaboradores"),
    ('todos', "Todos"),
)

class FatorDesempenhoMerito(models.Model):
    fator = models.TextField(blank=True, null=True)
    visivel = models.CharField('Visibilidade', max_length=20, choices=VISIVEL)

    class Meta:
        verbose_name = "Fator Meritório"
        verbose_name_plural = "Fatores Meritórios"
    
    def __str__(self) -> str:
        return f"Mérito {self.fator}"


class FatorDesempenhoDemerito(models.Model):
    fator = models.TextField(null=True, blank=True)
    visivel = models.CharField('Visibilidade', max_length=20, choices=VISIVEL)

    class Meta:
        verbose_name = "Fator Demeritório"
        verbose_name_plural = "Fatores Demeritórios"
    
    def __str__(self) -> str:
        return f"Demérito {self.fator}"