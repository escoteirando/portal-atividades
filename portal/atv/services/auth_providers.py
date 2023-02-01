from typing import Dict, List

from ..models.associacao import Associacao
from .auth_provider import AuthProvider
from .mappa_auth_provider import MappaAuthProvider


class AuthProviders():

    providers: Dict[str, AuthProvider] = dict()

    @classmethod
    def register(cls, provider: AuthProvider):
        cls.providers[provider.name()] = provider

    @classmethod
    def providers_names(cls) -> List[str]:
        return sorted([str(k) for k in cls.providers.keys()])

    @classmethod
    def provider_by_alias(cls, alias: str) -> AuthProvider | None:
        for (_, provider) in cls.providers.items():
            if provider.alias() == alias:
                return provider


_providers: AuthProviders | None = None


def get_auth_providers() -> AuthProviders:
    global _providers
    if not _providers:

        _providers = AuthProviders()
        _providers.register(MappaAuthProvider())

    return _providers


def update_associacoes():
    """Atualiza a tabela de associações com os providers"""
    for (_, provider) in get_auth_providers().providers.items():
        if associacao := Associacao.objects.get(alias=provider.alias):
            continue
        associacao = Associacao(name=provider.name, alias=provider.alias)
        associacao.save()
