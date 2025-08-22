from PySide6.QtCore import QRect, QSize, Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget

from src.domain.models.building import Building, BuildingType


class CityGrid(QWidget):
    """Widget pour afficher la grille de la ville."""

    # Signal émis lorsqu'une cellule est cliquée, avec la position x, y
    cell_clicked = Signal(int, int)

    # Couleurs des différents types de bâtiments
    BUILDING_COLORS = {
        BuildingType.HOUSE: QColor(255, 100, 100),  # Rouge (maisons)
        BuildingType.COMMERCE: QColor(0, 200, 0),  # Vert (commerces)
        BuildingType.INDUSTRY: QColor(100, 100, 100),  # Gris (industries)
        BuildingType.LEISURE: QColor(255, 200, 0),  # Jaune (loisirs)
    }

    # Noms simples pour les types de bâtiments (pour les tooltips)
    BUILDING_NAMES = {
        BuildingType.HOUSE: "Maison",
        BuildingType.COMMERCE: "Commerce",
        BuildingType.INDUSTRY: "Industrie",
        BuildingType.LEISURE: "Loisirs",
    }

    def __init__(self, parent=None):
        """Initialise une nouvelle grille de ville."""
        super().__init__(parent)

        # Dimensions de la grille
        self.grid_width = 20
        self.grid_height = 15

        # Taille des cellules (en pixels) - augmentée pour une meilleure visibilité
        self.cell_size = 35

        # Données de la grille (None si pas de bâtiment)
        self.grid_data = [
            [None for _ in range(self.grid_width)] for _ in range(self.grid_height)
        ]

        # Mode d'interaction
        self.selected_building_type = (
            None  # Type de bâtiment sélectionné pour construction
        )
        self.is_remove_mode = False  # Mode suppression

        # Couleur de fond
        self.background_color = QColor(200, 230, 200)  # Vert clair

        # S'assurer que le widget peut recevoir les événements de souris
        self.setMouseTracking(True)

        # Définir une taille minimale
        self.setMinimumSize(
            self.grid_width * self.cell_size, self.grid_height * self.cell_size
        )

    def set_grid_size(self, width: int, height: int) -> None:
        """
        Définit la taille de la grille.

        Parameters
        ----------
        width : int
            Nombre de cellules en largeur
        height : int
            Nombre de cellules en hauteur
        """
        self.grid_width = width
        self.grid_height = height
        self.grid_data = [[None for _ in range(width)] for _ in range(height)]

        # Mettre à jour la taille minimale
        self.setMinimumSize(
            self.grid_width * self.cell_size, self.grid_height * self.cell_size
        )

        # Redessiner
        self.update()

    def set_cell_size(self, size: int) -> None:
        """
        Définit la taille des cellules.

        Parameters
        ----------
        size : int
            Taille des cellules en pixels
        """
        self.cell_size = max(10, size)  # Minimum 10 pixels

        # Mettre à jour la taille minimale
        self.setMinimumSize(
            self.grid_width * self.cell_size, self.grid_height * self.cell_size
        )

        # Redessiner
        self.update()

    def set_building(self, x: int, y: int, building: Building) -> None:
        """
        Définit un bâtiment à la position spécifiée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y
        building : Building
            Bâtiment à placer
        """
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            self.grid_data[y][x] = building
            self.update()

    def remove_building(self, x: int, y: int) -> None:
        """
        Supprime un bâtiment de la position spécifiée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y
        """
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            self.grid_data[y][x] = None
            self.update()

    def set_selected_building_type(self, building_type: BuildingType = None) -> None:
        """
        Définit le type de bâtiment sélectionné pour construction.

        Parameters
        ----------
        building_type : BuildingType, optional
            Type de bâtiment sélectionné, ou None pour désactiver
        """
        self.selected_building_type = building_type
        self.is_remove_mode = False

    def set_remove_mode(self, enabled: bool) -> None:
        """
        Active ou désactive le mode suppression.

        Parameters
        ----------
        enabled : bool
            True pour activer le mode suppression, False sinon
        """
        self.is_remove_mode = enabled
        if enabled:
            self.selected_building_type = None

    def paintEvent(self, event):
        """
        Dessine la grille et les bâtiments.

        Parameters
        ----------
        event : QPaintEvent
            Événement de peinture
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fond
        painter.fillRect(event.rect(), self.background_color)

        # Dessiner la grille
        pen = QPen(QColor(150, 150, 150))
        pen.setWidth(1)
        painter.setPen(pen)

        # Lignes horizontales
        for y in range(self.grid_height + 1):
            painter.drawLine(
                0,
                y * self.cell_size,
                self.grid_width * self.cell_size,
                y * self.cell_size,
            )

        # Lignes verticales
        for x in range(self.grid_width + 1):
            painter.drawLine(
                x * self.cell_size,
                0,
                x * self.cell_size,
                self.grid_height * self.cell_size,
            )

        # Dessiner les bâtiments
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                building = self.grid_data[y][x]
                if building:
                    self._draw_building(painter, x, y, building)

        # Terminer explicitement le QPainter
        painter.end()

    def _draw_building(
        self, painter: QPainter, x: int, y: int, building: Building
    ) -> None:
        """
        Dessine un bâtiment à la position spécifiée.

        Parameters
        ----------
        painter : QPainter
            Contexte de dessin
        x : int
            Position X
        y : int
            Position Y
        building : Building
            Bâtiment à dessiner
        """
        # Récupérer la couleur du bâtiment
        color = self.BUILDING_COLORS.get(building.building_type, QColor(150, 150, 150))

        # Dessiner le bâtiment
        rect = QRect(
            x * self.cell_size + 2,
            y * self.cell_size + 2,
            self.cell_size - 4,
            self.cell_size - 4,
        )

        # Remplir avec la couleur
        painter.fillRect(rect, color)

        # Bordure
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(rect)

        # Dessiner le texte de type de bâtiment au centre, plus grand et visible
        center_x = x * self.cell_size + self.cell_size // 2
        center_y = y * self.cell_size + self.cell_size // 2

        # Définir une police plus grande
        font = painter.font()
        font.setPointSize(10)
        font.setBold(True)
        painter.setFont(font)

        # Sélectionner la lettre selon le type de bâtiment
        if building.building_type == BuildingType.HOUSE:
            letter = "M"  # Maison
        elif building.building_type == BuildingType.COMMERCE:
            letter = "C"  # Commerce
        elif building.building_type == BuildingType.INDUSTRY:
            letter = "I"  # Industrie
        elif building.building_type == BuildingType.LEISURE:
            letter = "L"  # Loisirs
        else:
            letter = "?"

        # Dessiner le texte avec un contraste suffisant
        text_color = Qt.black if color.lightness() > 128 else Qt.white
        painter.setPen(text_color)

        # Centrer la lettre dans la cellule
        painter.drawText(rect, Qt.AlignCenter, letter)

    def mousePressEvent(self, event):
        """
        Gère les clics de souris sur la grille.

        Parameters
        ----------
        event : QMouseEvent
            Événement de souris
        """
        if event.button() == Qt.LeftButton:
            # Convertir la position en coordonnées de grille
            x = event.position().x() // self.cell_size
            y = event.position().y() // self.cell_size

            # Vérifier si les coordonnées sont dans la grille
            if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
                # Émettre le signal avec les coordonnées
                self.cell_clicked.emit(int(x), int(y))

    def sizeHint(self) -> QSize:
        """
        Taille suggérée pour le widget.

        Returns
        -------
        QSize
            Taille suggérée
        """
        return QSize(
            self.grid_width * self.cell_size, self.grid_height * self.cell_size
        )
