# Generated by Django 4.1.5 on 2023-02-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atv', '0006_atividade_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='tipo',
            field=models.CharField(choices=[('A', 'Atividade'), ('C', 'Cerimônia'), ('Q', 'Quebra-gelo'), ('T', 'Intervalo'), ('I', 'Instrução'), ('J', 'Jogo'), ('H', 'História'), ('R', 'Refeição')], default='A', max_length=1, verbose_name='Tipo'),
        ),
    ]
