from dataclasses import dataclass
from enum import Enum, auto


class BuildingType(Enum):
    """Types de bâtiments disponibles dans le jeu."""

    HOUSE = auto()  # Maison
    COMMERCE = auto()  # Commerce
    INDUSTRY = auto()  # Industrie
    LEISURE = auto()  # Distractions


@dataclass
class BuildingProperties:
    """Propriétés d'un bâtiment."""

    cost: int  # Coût de construction
    space: int  # Espace occupé
    capacity: int  # Capacité (personnes)
    satisfaction: float  # Impact sur la satisfaction
    jobs: int  # Nombre d'emplois générés
    income: int  # Revenu généré


class Building:
    """Classe de base pour tous les bâtiments."""

    def __init__(self, x: int, y: int, building_type: BuildingType):
        """
        Initialise un nouveau bâtiment.

        Parameters
        ----------
        x : int
            Position X sur la grille
        y : int
            Position Y sur la grille
        building_type : BuildingType
            Type de bâtiment
        """
        self.x = x
        self.y = y
        self.building_type = building_type
        self.properties = self._get_properties()

    def _get_properties(self) -> BuildingProperties:
        """
        Obtient les propriétés spécifiques au type de bâtiment.

        Returns
        -------
        BuildingProperties
            Les propriétés du bâtiment
        """
        if self.building_type == BuildingType.HOUSE:
            return BuildingProperties(
                cost=100, space=1, capacity=4, satisfaction=0.2, jobs=0, income=0
            )
        elif self.building_type == BuildingType.COMMERCE:
            return BuildingProperties(
                cost=200, space=2, capacity=0, satisfaction=0.1, jobs=5, income=50
            )
        elif self.building_type == BuildingType.INDUSTRY:
            return BuildingProperties(
                cost=500, space=4, capacity=0, satisfaction=-0.1, jobs=20, income=200
            )
        elif self.building_type == BuildingType.LEISURE:
            return BuildingProperties(
                cost=300, space=3, capacity=0, satisfaction=0.3, jobs=8, income=100
            )
        else:
            raise ValueError(f"Type de bâtiment inconnu: {self.building_type}")
