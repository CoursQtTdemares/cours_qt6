from observer import Observer
from src.model import Person


class Presenter:
    def __init__(self, person: Person) -> None:
        self._person = person
        self._observers: list[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._person)

    def set_name(self, name: str) -> None:
        self._person.name = name
        self.notify_observers()

    def set_last_name(self, last_name: str) -> None:
        self._person.last_name = last_name
        self.notify_observers()
