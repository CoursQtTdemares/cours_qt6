import sys

from PySide6.QtWidgets import QApplication

from constants import WORKSPACE_PATH
from presenter import Presenter
from src.model import Person
from view import View


def _load_stylesheet() -> str:
    with open(WORKSPACE_PATH / "src" / "style.css", "r") as file:
        return file.read()


def main() -> None:
    """Entry point of the application."""
    app = QApplication(sys.argv)

    app.setStyleSheet(_load_stylesheet())

    person = Person()
    presenter = Presenter(person)
    view = View(presenter)
    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
