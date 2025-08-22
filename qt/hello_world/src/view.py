from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from presenter import Presenter
from src.model import Person


class View(QMainWindow):
    def __init__(self, presenter: Presenter) -> None:
        super().__init__()
        self.presenter = presenter
        self.presenter.add_observer(self)
        self.setup_ui()

    def setup_ui(self) -> None:
        """Configure the user interface."""
        self.setWindowTitle("Hello World MVP")
        self.setMinimumSize(400, 300)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        # Welcome label
        self.welcome_label = QLabel("Welcome !")
        self.welcome_label.setObjectName("welcome-label")
        layout.addWidget(self.welcome_label)

        # Input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setObjectName("input-field")
        layout.addWidget(self.name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Enter your last name")
        self.last_name_input.setObjectName("input-field")
        layout.addWidget(self.last_name_input)

        # Update button
        update_button = QPushButton("Update")
        update_button.setObjectName("update-button")
        update_button.clicked.connect(self.update_personne)
        layout.addWidget(update_button)

        # Label d'affichage
        self.display_label = QLabel()
        self.display_label.setObjectName("display-label")
        layout.addWidget(self.display_label)

    def update_personne(self) -> None:
        self.presenter.set_name(self.name_input.text())
        self.presenter.set_last_name(self.last_name_input.text())

    def update(self, person: Person) -> None:
        if person.name and person.last_name:
            self.display_label.setText(f"Hello {person.last_name} {person.name} !")
        else:
            self.display_label.setText("")
