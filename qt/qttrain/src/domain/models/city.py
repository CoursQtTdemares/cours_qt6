from dataclasses import dataclass
from typing import Dict, Optional

from PySide6.QtCore import QObject, Signal

from src.domain.models.building import Building, BuildingType


@dataclass
class CityStats:
    """Statistiques d'une ville."""

    population: int = 0
    max_population: int = 0
    employed: int = 0
    happiness: float = 0.5  # Entre 0 et 1
    funds: int = 1000
    tax_rate: float = 0.10  # 10%
    space_satisfaction: float = 0.5
    job_satisfaction: float = 0.5
    leisure_satisfaction: float = 0.5
    wealth_satisfaction: float = 0.5
    mayor_rating: float = 0.5  # Entre 0 et 1


class City(QObject):
    """Modèle de la ville qui gère les bâtiments et les statistiques."""

    # Signals pour notifier les changements dans le modèle (patron MVC)
    building_added = Signal(Building)
    building_removed = Signal(int, int)  # x, y
    stats_updated = Signal(CityStats)

    def __init__(self, width: int = 20, height: int = 15):
        """
        Initialise une nouvelle ville.

        Parameters
        ----------
        width : int
            Largeur de la grille
        height : int
            Hauteur de la grille
        """
        super().__init__()
        self.width = width
        self.height = height
        self.buildings: Dict[tuple[int, int], Building] = {}  # (x, y) -> Building
        self.stats = CityStats()
        self.grid = [[None for _ in range(width)] for _ in range(height)]

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
        # Vérifier si la position est valide
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        # Vérifier si la position est libre
        if self.grid[y][x] is not None:
            return False

        # Vérifier si les fonds sont suffisants
        building = Building(x, y, building_type)
        if building.properties.cost > self.stats.funds:
            return False

        # Ajouter le bâtiment
        self.buildings[(x, y)] = building
        self.grid[y][x] = building

        # Déduire le coût
        self.stats.funds -= building.properties.cost

        # Mettre à jour les statistiques
        self._update_stats()

        # Émettre le signal
        self.building_added.emit(building)

        return True

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
        # Vérifier si la position est valide
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        # Vérifier si un bâtiment existe à cette position
        if self.grid[y][x] is None:
            return False

        # Supprimer le bâtiment
        building = self.buildings.pop((x, y))
        self.grid[y][x] = None

        # Mettre à jour les statistiques
        self._update_stats()

        # Émettre le signal
        self.building_removed.emit(x, y)

        return True

    def set_tax_rate(self, rate: float) -> None:
        """
        Définit le taux d'imposition.

        Parameters
        ----------
        rate : float
            Taux d'imposition entre 0 et 1
        """
        self.stats.tax_rate = max(0.0, min(1.0, rate))
        self._update_stats()

    def _update_stats(self) -> None:
        """Met à jour toutes les statistiques de la ville."""
        # Calcul de la capacité de population
        total_capacity = sum(b.properties.capacity for b in self.buildings.values())
        self.stats.max_population = total_capacity

        # Population (limitée par la capacité)
        target_population = int(total_capacity * self.stats.happiness)
        if target_population > self.stats.population:
            # La population augmente progressivement
            self.stats.population = min(target_population, self.stats.population + 5)
        else:
            # La population diminue plus rapidement
            self.stats.population = max(target_population, self.stats.population - 10)

        # Emplois disponibles
        total_jobs = sum(b.properties.jobs for b in self.buildings.values())
        self.stats.employed = min(self.stats.population, total_jobs)

        # Revenu des bâtiments
        building_income = sum(b.properties.income for b in self.buildings.values())

        # Impôts
        tax_income = int(self.stats.population * self.stats.tax_rate * 10)

        # Fonds (mise à jour par tour)
        self.stats.funds += building_income + tax_income

        # Calcul des satisfactions
        # Espace (ratio population/capacité idéale)
        if total_capacity > 0:
            population_ratio = self.stats.population / total_capacity
            self.stats.space_satisfaction = 1.0 - min(
                1.0, max(0.0, population_ratio - 0.5)
            )
        else:
            self.stats.space_satisfaction = 1.0

        # Emploi (ratio personnes employées/population)
        if self.stats.population > 0:
            self.stats.job_satisfaction = self.stats.employed / self.stats.population
        else:
            self.stats.job_satisfaction = 0.5

        # Loisirs (basé sur le nombre de bâtiments de loisirs)
        leisure_buildings = sum(
            1
            for b in self.buildings.values()
            if b.building_type == BuildingType.LEISURE
        )
        if self.stats.population > 0:
            leisure_ratio = min(
                1.0, leisure_buildings / (self.stats.population / 20 + 1)
            )
            self.stats.leisure_satisfaction = leisure_ratio
        else:
            self.stats.leisure_satisfaction = 0.5

        # Richesse (basée sur les revenus et les impôts)
        wealth_base = building_income / (self.stats.population + 1)
        tax_penalty = (
            self.stats.tax_rate * 2
        )  # Plus les impôts sont élevés, moins les gens sont satisfaits
        self.stats.wealth_satisfaction = min(
            1.0, max(0.0, wealth_base / 50 - tax_penalty + 0.5)
        )

        # Satisfaction du maire (moyenne des satisfactions)
        self.stats.mayor_rating = (
            self.stats.space_satisfaction
            + self.stats.job_satisfaction
            + self.stats.leisure_satisfaction
            + self.stats.wealth_satisfaction
        ) / 4.0

        # Bonheur global (affecte la croissance de la population)
        self.stats.happiness = (
            self.stats.space_satisfaction * 0.3
            + self.stats.job_satisfaction * 0.3
            + self.stats.leisure_satisfaction * 0.2
            + self.stats.wealth_satisfaction * 0.2
        ) - (self.stats.tax_rate * 0.5)  # Les impôts réduisent le bonheur
        self.stats.happiness = max(0.1, min(1.0, self.stats.happiness))

        # Émettre le signal de mise à jour des statistiques
        self.stats_updated.emit(self.stats)

    def update(self) -> None:
        """
        Met à jour la ville (appelé périodiquement).
        Utilisé pour la simulation au fil du temps.
        """
        self._update_stats()

    def get_building_at(self, x: int, y: int) -> Optional[Building]:
        """
        Récupère le bâtiment à la position spécifiée.

        Parameters
        ----------
        x : int
            Position X
        y : int
            Position Y

        Returns
        -------
        Optional[Building]
            Le bâtiment à la position ou None si aucun bâtiment
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None
