from PySide6.QtCore import Signal
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from src.domain.models.building import BuildingType


class ColorLegendItem(QFrame):
    """Widget pour afficher un élément de légende avec une couleur."""

    def __init__(self, color: QColor, text: str, parent=None):
        """Initialise un élément de légende."""
        super().__init__(parent)

        self.color = color
        self.text = text

        # Définir une taille fixe
        self.setMinimumSize(20, 20)
        self.setMaximumSize(20, 20)

        # Définir le style pour le contour
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(1)

        # Définir la couleur de fond
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), self.color)
        self.setPalette(palette)


class BuildingPanel(QWidget):
    """Panneau de contrôle pour la construction de bâtiments."""

    # Signal émis lorsqu'un type de bâtiment est sélectionné
    building_type_selected = Signal(BuildingType)

    # Signal émis lorsque le mode suppression est activé/désactivé
    remove_mode_toggled = Signal(bool)

    def __init__(self, parent=None):
        """Initialise le panneau de bâtiments."""
        super().__init__(parent)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(8)  # Espacement modéré
        main_layout.setContentsMargins(10, 10, 10, 10)  # Marges normales

        # Groupe pour les contrôles des bâtiments
        building_group = QGroupBox("Bâtiments")
        building_layout = QVBoxLayout(building_group)
        building_layout.setSpacing(8)

        # Titre
        title_label = QLabel("Sélectionnez un type de bâtiment:")
        title_label.setFont(QFont("Arial", 10, QFont.Bold))
        building_layout.addWidget(title_label)

        # Légende des couleurs en ligne (plus discret mais toujours visible)
        legend_layout = QHBoxLayout()

        # Couleurs des bâtiments
        building_colors = [
            (BuildingType.HOUSE, QColor(255, 100, 100), "Maison"),
            (BuildingType.COMMERCE, QColor(0, 200, 0), "Commerce"),
            (BuildingType.INDUSTRY, QColor(100, 100, 100), "Industrie"),
            (BuildingType.LEISURE, QColor(255, 200, 0), "Loisirs"),
        ]

        # Ajouter les éléments de légende dans une ligne
        for building_type, color, name in building_colors:
            item_layout = QHBoxLayout()
            color_box = ColorLegendItem(color, name)
            color_box.setMinimumSize(12, 12)  # Plus petit
            color_box.setMaximumSize(12, 12)
            item_layout.addWidget(color_box)
            item_layout.addWidget(QLabel(name), 1)
            legend_layout.addLayout(item_layout)

        building_layout.addLayout(legend_layout)

        # Ajouter un petit espace
        building_layout.addSpacing(5)

        # Boutons radio pour les types de bâtiments
        self.building_buttons = {}

        building_types = [
            (BuildingType.HOUSE, "Maison (100 €)", "Loger les habitants"),
            (
                BuildingType.COMMERCE,
                "Commerce (200 €)",
                "Créer des emplois et générer des revenus",
            ),
            (
                BuildingType.INDUSTRY,
                "Industrie (500 €)",
                "Créer beaucoup d'emplois et de revenus",
            ),
            (BuildingType.LEISURE, "Loisirs (300 €)", "Améliorer la satisfaction"),
        ]

        for building_type, name, description in building_types:
            radio = QRadioButton(name)  # Nom complet avec prix
            radio.setToolTip(description)
            radio.setFont(QFont("Arial", 10))
            radio.toggled.connect(
                lambda checked, bt=building_type: self._on_building_selected(
                    checked, bt
                )
            )
            building_layout.addWidget(radio)
            self.building_buttons[building_type] = radio

        # Groupe pour les actions
        actions_group = QGroupBox("Actions")
        actions_layout = QVBoxLayout(actions_group)

        # Bouton pour la suppression
        self.remove_button = QPushButton("Supprimer un bâtiment")
        self.remove_button.setCheckable(True)
        self.remove_button.toggled.connect(self._on_remove_toggled)

        # Bouton pour annuler la sélection
        self.cancel_button = QPushButton("Annuler la sélection")
        self.cancel_button.clicked.connect(self._on_cancel_clicked)

        # Ajouter les boutons au layout
        actions_layout.addWidget(self.remove_button)
        actions_layout.addWidget(self.cancel_button)

        # Ajouter les groupes au layout principal
        main_layout.addWidget(building_group)
        main_layout.addWidget(actions_group)

        # Ajouter un espace extensible pour pousser les widgets vers le haut
        main_layout.addStretch(1)

        # Définir une taille minimale
        self.setMinimumWidth(300)

    def _on_building_selected(self, checked: bool, building_type: BuildingType) -> None:
        """
        Appelé lorsqu'un type de bâtiment est sélectionné.

        Parameters
        ----------
        checked : bool
            True si le bouton est coché, False sinon
        building_type : BuildingType
            Le type de bâtiment sélectionné
        """
        if checked:
            # Désactiver le mode suppression
            self.remove_button.setChecked(False)

            # Émettre le signal
            self.building_type_selected.emit(building_type)

    def _on_remove_toggled(self, checked: bool) -> None:
        """
        Appelé lorsque le bouton de suppression est activé/désactivé.

        Parameters
        ----------
        checked : bool
            True si le bouton est coché, False sinon
        """
        if checked:
            # Désélectionner tous les boutons de bâtiments
            for button in self.building_buttons.values():
                button.setChecked(False)

        # Émettre le signal
        self.remove_mode_toggled.emit(checked)

    def _on_cancel_clicked(self) -> None:
        """Appelé lorsque le bouton d'annulation est cliqué."""
        # Désélectionner tous les boutons de bâtiments
        for button in self.building_buttons.values():
            button.setChecked(False)

        # Désactiver le mode suppression
        self.remove_button.setChecked(False)

        # Émettre les signaux
        self.building_type_selected.emit(None)
        self.remove_mode_toggled.emit(False)
