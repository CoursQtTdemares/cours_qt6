from typing import Protocol

from src.model import Person


class Observer(Protocol):
    def update(self, person: Person) -> None:
        pass
