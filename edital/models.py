from datetime import date
from django.db import models
from django import forms

# salvar o documento do edital no path designado
def folder_upload(self, filename):
    return (
        f"editais/{self.edital}/{self.arquivo}"
)

class AdicionarEdital(models.Model):
    edital = models.CharField('Nome do Edital', max_length=150, unique=False)
    data_inicio = models.DateField(blank=True, null=True, verbose_name='Data de início')
    data_termino = models.DateField(blank=True, null=True, verbose_name='Data de término')
    andamento = models.BooleanField('Em andamento', default=False)
    arquivo = models.FileField(blank=True, null=True, upload_to=folder_upload)

    def save(self, *args, **kwargs):
        # valida se o edital foi criado durante o periodo selecionado
        # necessita mudar a estrategia para atualizar automaticamente apartir da data
        if (self.data_inicio <= date.today() and self.data_termino > date.today()):
            self.andamento = True
        super().save()

    def clean(self):
        # validar se ja ha um edital no periodo inserido
        if self.data_inicio and self.data_termino:
            if self.__class__.objects.filter(
                models.Q(data_termino__gte=self.data_inicio, data_inicio__lt=self.data_inicio) | models.Q(data_termino__gte=self.data_termino, data_inicio__lt=self.data_termino) | models.Q(data_inicio__gt=self.data_inicio, data_termino__lt=self.data_termino)
            ).exists():
                raise forms.ValidationError('Já há um edital nesse período')
        # validar se a data inicial eh antes da final
        if self.data_termino <= self.data_inicio:
            raise forms.ValidationError("Data de início deve ser anterior à data de término")

    def __str__(self) -> str:
        return f"{self.edital}"

    class Meta:
        verbose_name='Edital'
        verbose_name_plural='Editais'


