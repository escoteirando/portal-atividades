from typing import Protocol

from atv.models.escotista import Escotista


class AuthProvider(Protocol):

    def name(self) -> str:
        ...

    def alias(self) -> str:
        ...

    def login(self, username: str, password: str) -> Escotista:
        ...
