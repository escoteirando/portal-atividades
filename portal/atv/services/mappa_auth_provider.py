from atv.models.associacao import Associacao
from atv.models.grupo_escoteiro import GrupoEscoteiro
from atv.models.escotista import Escotista
from .auth_provider import AuthProvider
from .mappa.mappa_api import MappaApi
from .mappa.mappa_models import MappaGrupoResponse, MappaDadosEscotista
import logging
from django.contrib.auth.models import User


class AuthError(Exception):
    ...


class MappaAuthProvider(AuthProvider):

    def __init__(self):
        self.api = MappaApi()
        self._associacao = self._assert_associacao()
        self._logger = logging.getLogger(self.__class__.__name__)

    def name(self) -> str:
        return 'União dos Escoteiros do Brasil'

    def alias(self) -> str:
        return 'UEB'

    def _assert_associacao(self) -> Associacao:
        try:
            associacao = Associacao.objects.get(pk=self.alias())
        except:
            associacao = None
        if associacao is None:
            associacao = Associacao.objects.create(
                alias=self.alias(), name=self.name())
        return associacao

    def _assert_grupo_escoteiro(self, mappa_grupo: MappaGrupoResponse) -> GrupoEscoteiro:
        grupo = GrupoEscoteiro.objects.filter(
            associacao=self._associacao,
            number=mappa_grupo.codigo,
            region=mappa_grupo.codigoRegiao).first()
        if grupo is None:
            grupo = GrupoEscoteiro.objects.create(
                name=mappa_grupo.nome,
                associacao=self._associacao,
                number=mappa_grupo.codigo,
                region=mappa_grupo.codigoRegiao
            )
        return grupo

    def _assert_escotista(self, mappa_escotista: MappaDadosEscotista, grupo: GrupoEscoteiro) -> Escotista:
        escotistas = Escotista.objects.filter(
            association=self._associacao,
            # TODO: Identificar o campo UserId
            external_id=mappa_escotista.associado.username,
        )
        if escotistas:
            escotista = escotistas[0]
        else:
            escotista = Escotista(
                association=self._associacao,
                external_id=mappa_escotista.associado.username,
            )
        escotista.name = mappa_escotista.escotista.nomeCompleto or mappa_escotista.escotista.username
        escotista.scout_group = grupo        
        escotista.save()
        return escotista

    def login(self, username: str, password: str) -> Escotista:
        try:
            # TODO: Implementar tratamento de erros
            login = self.api.login(username, password)
            if not login.user_id:
                raise AuthError()

            mappa_escotista = self.api.get_escotista(login.user_id, login.auth)

            grupo = self._assert_grupo_escoteiro(mappa_escotista.grupo)
            escotista = self._assert_escotista(mappa_escotista, grupo)

            return escotista
        except Exception as exc:
            self._logger.error('LOGIN EXCEPTION: %s', exc)
            raise
