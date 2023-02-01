from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from martor.models import MartorField
from multiselectfield import MultiSelectField

from .enum_enfase import ENFASE
from .enum_ramo import RAMO
from .enum_tipo_atividade import TIPO_ATV
from .escotista import Escotista


def validate_ramos(value):
    if len(value) == 0:
        raise ValidationError(
            'É necessário informar ao menos um ramo para a atividade')


class Atividade(models.Model):

    titulo = models.CharField(verbose_name='Título',
                              max_length=60, blank=False)
    ramos = MultiSelectField(choices=RAMO,
                             max_length=len(RAMO)*2-1,
                             verbose_name='Ramos',
                             validators=[validate_ramos])
    enfases = MultiSelectField(choices=ENFASE,
                               max_length=len(ENFASE)*2-1,
                               verbose_name='Ênfases')
    tipo = models.CharField(verbose_name='Tipo',
                            max_length=1,
                            choices=TIPO_ATV,
                            default='A')
    editor = models.ForeignKey(Escotista, on_delete=models.PROTECT)


    autor_url = models.URLField(
        verbose_name='URL Autor', null=True)

    descricao = MartorField(verbose_name='Descrição', blank=False)

    creation_date = models.DateTimeField(
        verbose_name='Data de criação', auto_now=True)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return f'{self.titulo}'
