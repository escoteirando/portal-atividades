import logging

from atv.models.atividade import Atividade
from atv.models.escotista import Escotista


class ComunidadeService:

    log = logging.getLogger('AuthService')

    @classmethod
    def get_escotistas_count(cls) -> int:
        return Escotista.objects.count()

    @classmethod
    def get_last_escotista(cls) -> Escotista:
        return Escotista.objects.earliest('subscribe_date')

    @classmethod
    def get_last_atividade(cls) -> Atividade | None:
        try:
            return Atividade.objects.earliest('creation_date')
        except:
            return None

    @classmethod
    def get_atividades_count(cls) -> int:
        return Atividade.objects.count()
