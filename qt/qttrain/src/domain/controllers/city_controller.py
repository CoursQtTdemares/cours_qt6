from PySide6.QtCore import QObject, QTimer, Signal

from src.domain.models.building import BuildingType
from src.domain.models.city import City


class CityController(QObject):
    """
    Contrôleur pour la ville selon le patron MVC.
    Gère les interactions entre la vue et le modèle.
    """

    simulation_started = Signal()
    simulation_stopped = Signal()

    def __init__(self):
        """Initialise un nouveau contrôleur de ville."""
        super().__init__()
        self.city = City()

        # Timer pour les mises à jour périodiques
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_simulation)
        self.simulation_speed = 1000  # ms (1 seconde par défaut)

    def add_building(self, x: int, y: int, building_type: BuildingType) -> bool:
        """
        Ajoute un bâtiment à la position spécifiée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y
        building_type : BuildingType
            Type de bâtiment à ajouter

        Returns
        -------
        bool
            True si le bâtiment a été ajouté avec succès, False sinon
        """
        return self.city.add_building(x, y, building_type)

    def remove_building(self, x: int, y: int) -> bool:
        """
        Supprime un bâtiment de la position spécifiée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y

        Returns
        -------
        bool
            True si le bâtiment a été supprimé avec succès, False sinon
        """
        return self.city.remove_building(x, y)

    def set_tax_rate(self, rate: float) -> None:
        """
        Définit le taux d'imposition.

        Parameters
        ----------
        rate : float
            Taux d'imposition entre 0 et 1
        """
        self.city.set_tax_rate(rate)

    def set_simulation_speed(self, speed_ms: int) -> None:
        """
        Définit la vitesse de simulation.

        Parameters
        ----------
        speed_ms : int
            Vitesse en millisecondes entre chaque mise à jour
        """
        self.simulation_speed = max(100, speed_ms)  # Minimum 100ms
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.simulation_speed)

    def start_simulation(self) -> None:
        """Démarre la simulation."""
        if not self.timer.isActive():
            self.timer.start(self.simulation_speed)
            self.simulation_started.emit()

    def stop_simulation(self) -> None:
        """Arrête la simulation."""
        if self.timer.isActive():
            self.timer.stop()
            self.simulation_stopped.emit()

    def toggle_simulation(self) -> None:
        """Démarre ou arrête la simulation."""
        if self.timer.isActive():
            self.stop_simulation()
        else:
            self.start_simulation()

    def _update_simulation(self) -> None:
        """Met à jour la simulation (appelé périodiquement)."""
        self.city.update()

    def create_new_city(self, width: int = 20, height: int = 15) -> None:
        """
        Crée une nouvelle ville.

        Parameters
        ----------
        width : int
            Largeur de la grille
        height : int
            Hauteur de la grille
        """
        # Arrêter la simulation actuelle
        self.stop_simulation()

        # Créer une nouvelle ville
        self.city = City(width, height)

        # Redémarrer la simulation
        self.start_simulation()
