from django.contrib.auth.models import User
from django.db import models

from .associacao import Associacao
from .grupo_escoteiro import GrupoEscoteiro


class Escotista(models.Model):

    name = models.CharField('Nome', max_length=80, null=False)
    association = models.ForeignKey(Associacao, on_delete=models.PROTECT)
    external_id = models.CharField('Id', max_length=16)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    scout_group = models.ForeignKey(
        GrupoEscoteiro, on_delete=models.PROTECT, blank=True)
    subscribe_date = models.DateTimeField(
        verbose_name='Data do cadastro', auto_now=True)

    def __str__(self):
        return f'{self.name} {self.scout_group}'
