from PySide6.QtCore import QSize, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QVBoxLayout,
    QWidget,
)

from src.domain.controllers.city_controller import CityController
from src.domain.models.building import BuildingType
from src.gui.widgets.building_panel import BuildingPanel
from src.gui.widgets.city_grid import CityGrid
from src.gui.widgets.stats_panel import StatsPanel


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application."""

    def __init__(self):
        """Initialise la fenêtre principale."""
        super().__init__()

        self.setWindowTitle("Simulateur de Ville")
        self.setMinimumSize(QSize(1024, 768))

        # Initialiser le contrôleur (MVC)
        self.controller = CityController()

        # Configurer l'interface utilisateur
        self._setup_ui()

        # Connecter les signaux
        self._connect_signals()

        # Démarrer la simulation
        self.controller.start_simulation()

        # Mettre à jour la barre d'état
        self.statusBar().showMessage(
            "Bienvenue dans le Simulateur de Ville ! Commencez à construire votre ville !"
        )

    def _setup_ui(self):
        """Configure l'interface utilisateur."""
        # Widget central et layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical avec panel gauche pour les contrôles et le reste pour la grille et les stats
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(5)  # Réduire l'espacement pour gagner de la place
        main_layout.setContentsMargins(5, 5, 5, 5)  # Réduire les marges

        # Layout horizontal pour la partie supérieure (contrôles à gauche, grille à droite)
        top_layout = QHBoxLayout()
        top_layout.setSpacing(5)

        # Panneau de bâtiments (à gauche)
        self.building_panel = BuildingPanel()
        self.building_panel.setMinimumWidth(
            320
        )  # Un peu plus large pour les boutons avec prix
        self.building_panel.setMaximumWidth(380)

        # Grille de la ville (au centre-droit)
        self.city_grid = CityGrid()

        # Ajouter les widgets au layout supérieur
        top_layout.addWidget(self.building_panel, 3)  # Donner une proportion adéquate
        top_layout.addWidget(self.city_grid, 7)  # La grille prend plus d'espace

        # Layout pour la partie inférieure (statistiques et graphiques en bas)
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(5)

        # Panneau de statistiques
        self.stats_panel = StatsPanel()
        bottom_layout.addWidget(self.stats_panel)

        # Ajouter les layouts au layout principal
        main_layout.addLayout(top_layout, 4)  # La partie supérieure prend plus d'espace
        main_layout.addLayout(
            bottom_layout, 2
        )  # La partie inférieure prend moins d'espace

        # Barre d'état
        self.statusBar().showMessage("Prêt")

        # Barre de menu
        self._create_menus()

        # Barre d'outils
        self._create_toolbar()

        # Redimensionner la fenêtre
        self.resize(1280, 800)

    def _create_menus(self):
        """Crée les menus de l'application."""
        # Menu Fichier
        file_menu = self.menuBar().addMenu("&Fichier")

        # Action Nouvelle ville
        new_action = QAction("&Nouvelle ville", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._on_new_city)
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        # Action Quitter
        exit_action = QAction("&Quitter", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Menu Simulation
        sim_menu = self.menuBar().addMenu("&Simulation")

        # Action Démarrer/Arrêter la simulation
        self.play_action = QAction("&Pause", self)
        self.play_action.setShortcut("Space")
        self.play_action.triggered.connect(self._on_toggle_simulation)
        sim_menu.addAction(self.play_action)

        # Menu Aide
        help_menu = self.menuBar().addMenu("&Aide")

        # Action À propos
        about_action = QAction("À &propos", self)
        about_action.triggered.connect(self._on_about)
        help_menu.addAction(about_action)

    def _create_toolbar(self):
        """Crée la barre d'outils de l'application."""
        toolbar = self.addToolBar("Simulation")
        toolbar.setMovable(False)

        # Action Démarrer/Arrêter la simulation
        toolbar.addAction(self.play_action)

        # Action Vitesse de simulation
        speed_menu = QMenu("Vitesse", self)

        speeds = [
            ("Lente", 2000),
            ("Normale", 1000),
            ("Rapide", 500),
            ("Très rapide", 200),
        ]

        for name, speed in speeds:
            action = QAction(name, self)
            action.triggered.connect(lambda checked, s=speed: self._on_speed_changed(s))
            speed_menu.addAction(action)

        speed_button = QAction("Vitesse: Normale", self)
        speed_button.setMenu(speed_menu)
        toolbar.addAction(speed_button)

    def _connect_signals(self):
        """Connecte les signaux et les slots."""
        # Signaux du modèle
        self.controller.city.building_added.connect(self._on_building_added)
        self.controller.city.building_removed.connect(self._on_building_removed)
        self.controller.city.stats_updated.connect(self.stats_panel.update_stats)

        # Signaux du contrôleur
        self.controller.simulation_started.connect(self._on_simulation_started)
        self.controller.simulation_stopped.connect(self._on_simulation_stopped)

        # Signaux de l'interface utilisateur
        self.building_panel.building_type_selected.connect(
            self._on_building_type_selected
        )
        self.building_panel.remove_mode_toggled.connect(self._on_remove_mode_toggled)
        self.city_grid.cell_clicked.connect(self._on_cell_clicked)
        self.stats_panel.get_tax_rate_signal().connect(self._on_tax_rate_changed)

    @Slot()
    def _on_new_city(self):
        """Crée une nouvelle ville."""
        self.controller.create_new_city()
        self.city_grid.set_grid_size(
            self.controller.city.width, self.controller.city.height
        )
        self.statusBar().showMessage("Nouvelle ville créée")

    @Slot()
    def _on_toggle_simulation(self):
        """Démarre ou arrête la simulation."""
        self.controller.toggle_simulation()

    @Slot()
    def _on_about(self):
        """Affiche la boîte de dialogue À propos."""
        self.statusBar().showMessage(
            "Simulateur de Ville - Créé avec PySide6 et Python"
        )

    @Slot(int)
    def _on_speed_changed(self, speed: int):
        """
        Change la vitesse de simulation.

        Parameters
        ----------
        speed : int
            Nouvelle vitesse en millisecondes
        """
        self.controller.set_simulation_speed(speed)

        # Mettre à jour le texte du bouton
        if speed > 1500:
            speed_text = "Lente"
        elif speed > 750:
            speed_text = "Normale"
        elif speed > 350:
            speed_text = "Rapide"
        else:
            speed_text = "Très rapide"

        self.statusBar().showMessage(f"Vitesse de simulation: {speed_text}")

    @Slot()
    def _on_simulation_started(self):
        """Appelé lorsque la simulation démarre."""
        self.play_action.setText("&Pause")
        self.statusBar().showMessage("Simulation en cours")

    @Slot()
    def _on_simulation_stopped(self):
        """Appelé lorsque la simulation s'arrête."""
        self.play_action.setText("&Démarrer")
        self.statusBar().showMessage("Simulation en pause")

    @Slot(BuildingType)
    def _on_building_type_selected(self, building_type: BuildingType):
        """
        Appelé lorsqu'un type de bâtiment est sélectionné.

        Parameters
        ----------
        building_type : BuildingType
            Le type de bâtiment sélectionné, ou None si aucun
        """
        self.city_grid.set_selected_building_type(building_type)

        if building_type:
            name = building_type.name.lower().capitalize()
            self.statusBar().showMessage(f"Type de bâtiment sélectionné: {name}")
        else:
            self.statusBar().showMessage("Aucun type de bâtiment sélectionné")

    @Slot(bool)
    def _on_remove_mode_toggled(self, enabled: bool):
        """
        Appelé lorsque le mode suppression est activé/désactivé.

        Parameters
        ----------
        enabled : bool
            True si le mode suppression est activé, False sinon
        """
        self.city_grid.set_remove_mode(enabled)

        if enabled:
            self.statusBar().showMessage("Mode suppression activé")
        else:
            self.statusBar().showMessage("Mode suppression désactivé")

    @Slot(int, int)
    def _on_cell_clicked(self, x: int, y: int):
        """
        Appelé lorsqu'une cellule de la grille est cliquée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y
        """
        # Mode suppression
        if self.city_grid.is_remove_mode:
            if self.controller.remove_building(x, y):
                self.statusBar().showMessage(f"Bâtiment supprimé en ({x}, {y})")
            else:
                self.statusBar().showMessage(
                    f"Aucun bâtiment à supprimer en ({x}, {y})"
                )

        # Mode construction
        elif self.city_grid.selected_building_type:
            if self.controller.add_building(
                x, y, self.city_grid.selected_building_type
            ):
                building_type = (
                    self.city_grid.selected_building_type.name.lower().capitalize()
                )
                self.statusBar().showMessage(f"{building_type} construit en ({x}, {y})")
            else:
                self.statusBar().showMessage(f"Impossible de construire en ({x}, {y})")

    @Slot(int)
    def _on_tax_rate_changed(self, value: int):
        """
        Appelé lorsque le taux d'imposition est modifié.

        Parameters
        ----------
        value : int
            Nouveau taux d'imposition en pourcentage
        """
        tax_rate = value / 100.0
        self.controller.set_tax_rate(tax_rate)

        self.statusBar().showMessage(f"Taux d'imposition défini à {value}%")

    @Slot(object)
    def _on_building_added(self, building):
        """
        Appelé lorsqu'un bâtiment est ajouté.

        Parameters
        ----------
        building : Building
            Le bâtiment ajouté
        """
        self.city_grid.set_building(building.x, building.y, building)

    @Slot(int, int)
    def _on_building_removed(self, x: int, y: int):
        """
        Appelé lorsqu'un bâtiment est supprimé.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y
        """
        self.city_grid.remove_building(x, y)
