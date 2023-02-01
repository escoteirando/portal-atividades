from django.db import models


class Associacao(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=50)
    alias = models.CharField(verbose_name='Apelido',
                             max_length=10, primary_key=True)

    class Meta:
        verbose_name = 'Associação'
        verbose_name_plural = 'Associações'

    def __str__(self):
        return f'{self.name} ({self.alias})'
