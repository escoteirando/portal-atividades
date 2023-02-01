from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..services.comunidade_service import ComunidadeService


@login_required
def comunidade_view(request):

    context = dict(
        escotistas_count=ComunidadeService.get_escotistas_count(),
        last_escotista=ComunidadeService.get_last_escotista(),
        last_atividade=ComunidadeService.get_last_atividade(),
        atividades_count=ComunidadeService.get_atividades_count()
    )

    return render(request, f'comunidade.html', context)
