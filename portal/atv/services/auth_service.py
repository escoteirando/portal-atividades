import logging

from atv.models.associacao import Associacao
from atv.models.escotista import Escotista
from atv.services.auth_providers import get_auth_providers
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import User


class AuthServiceError(Exception):

    def __init__(self, message: str, level: str = 'warning'):
        super().__init__(self, message)
        self._msg = message
        self._lvl = level

    @property
    def message(self): return self._msg
    
    @property
    def level(self): return self._lvl


class AuthService:

    log = logging.getLogger('AuthService')
    auth_providers = get_auth_providers()

    @classmethod
    def get_user_by_email(cls, email: str) -> User | None:
        return User.objects.filter(email=email).first()

    @classmethod
    def get_escotista_by_email(cls, email: str) -> Escotista | None:
        user = cls.get_user_by_email(email)
        if not user:
            return None

        return Escotista.objects.filter(user=user).first()

    @classmethod
    def get_escotista_by_user(cls, assoc_alias: str, assoc_user: str) -> Escotista | None:
        return Escotista.objects.filter(association=assoc_alias, external_id=assoc_user).first()

    @classmethod
    def subscribe_user(cls, email: str, password: str, assoc_alias: str, assoc_user: str, assoc_pass: str) -> dict:
        password_validation.validate_password(password)
        if escotista := cls.get_escotista_by_user(assoc_alias, assoc_user):
            raise AuthServiceError(
                f'Escotista já está cadastrado com o e-mail {escotista.user.email}')
        if escotista := cls.get_escotista_by_email(email):
            raise AuthServiceError('Email já está em uso')

        associacao = Associacao.objects.get(pk=assoc_alias)
        provider = cls.auth_providers.provider_by_alias(associacao.alias)
        if not provider:
            raise AuthServiceError(
                'Não há um provedor de autenticação para esta associação')

        if not (escotista := provider.login(assoc_user, assoc_pass)):
            raise AuthServiceError("Login na associação não foi autorizado")

        user = cls.get_user_by_email(email)
        if user is None:
            user = User.objects.create_user(
                email, email, password)

        escotista.user = user
        escotista.save()

        return dict(
            escotista=escotista
        )

    @classmethod
    def login(cls, email: str, password: str) -> User | None:
        if user := authenticate(username=email, password=password):
            if escotista := cls.get_escotista_by_email(email):
                if escotista.user.get_username() == user.get_username():
                    return user
