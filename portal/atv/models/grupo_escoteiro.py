from django.db import models

from .associacao import Associacao


class GrupoEscoteiro(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=80)
    associacao = models.ForeignKey(Associacao, on_delete=models.PROTECT)
    number = models.IntegerField(verbose_name='Número')
    region = models.CharField(verbose_name='Região', max_length=20)

    def __str__(self):
        return f'{self.number}/{self.region} : {self.name} [{self.associacao.alias}]'
