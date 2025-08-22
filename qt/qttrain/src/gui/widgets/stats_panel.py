from collections import deque
from typing import Dict

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from src.domain.models.city import CityStats

# Configuration matplotlib pour utiliser Qt
matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvas):
    """Widget matplotlib pour les graphiques."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """Initialise le canvas."""
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.axes.set_facecolor("#f0f0f0")
        self.fig.patch.set_facecolor("#f0f0f0")

        # Historique des données
        self.max_points = 100
        self.x_data = list(range(self.max_points))
        self.y_data_pop = deque([0] * self.max_points, maxlen=self.max_points)
        self.y_data_rating = deque([0] * self.max_points, maxlen=self.max_points)

        # Initialiser le graphique
        (self.pop_line,) = self.axes.plot(
            self.x_data, self.y_data_pop, label="Population", color="blue"
        )
        (self.rating_line,) = self.axes.plot(
            self.x_data, self.y_data_rating, label="Satisfaction", color="green"
        )
        self.axes.legend(loc="upper left")
        self.axes.set_ylim(0, 100)

        # Configurer les titres et labels avec des polices plus grandes
        self.axes.set_title("Évolution de la ville", fontsize=12, pad=10)
        self.axes.set_xlabel("Temps", fontsize=10)
        self.axes.set_ylabel("Valeurs", fontsize=10)

        # Ajuster les marges pour utiliser tout l'espace disponible
        self.fig.tight_layout(pad=2.0)

        # Ajuster l'espacement autour du graphique
        self.fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)


class StatsPanel(QWidget):
    """Widget pour afficher les statistiques de la ville."""

    def __init__(self, parent=None):
        """Initialise le panneau de statistiques."""
        super().__init__(parent)

        # Layout principal (horizontal)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(
            5, 5, 5, 5
        )  # Réduire les marges pour optimiser l'espace

        # Layout pour les statistiques et satisfactions (à gauche)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(5)  # Réduire l'espacement

        # Layout pour les statistiques principales et le slider de taxe (au milieu)
        middle_layout = QVBoxLayout()
        middle_layout.setSpacing(5)

        # Layout pour les graphiques (à droite)
        right_layout = QVBoxLayout()

        # Groupe pour les statistiques principales
        stats_group = QGroupBox("Statistiques")
        stats_layout = QVBoxLayout(stats_group)

        # Labels pour les statistiques
        self.labels: Dict[str, QLabel] = {}

        stats = [
            ("population", "Population"),
            ("funds", "Fonds"),
            ("mayor_rating", "Satisfaction du maire"),
        ]

        for key, text in stats:
            label = QLabel(f"{text}: 0")
            label.setFont(QFont("Arial", 10))
            stats_layout.addWidget(label)
            self.labels[key] = label

        # Ajouter à la section du milieu
        middle_layout.addWidget(stats_group)

        # Groupe pour les satisfactions
        satisfaction_group = QGroupBox("Satisfaction")
        satisfaction_layout = QVBoxLayout(satisfaction_group)

        # Barres de progression pour les satisfactions
        self.progress_bars: Dict[str, QProgressBar] = {}

        satisfactions = [
            ("space_satisfaction", "Espace"),
            ("job_satisfaction", "Emploi"),
            ("leisure_satisfaction", "Loisirs"),
            ("wealth_satisfaction", "Richesse"),
        ]

        for key, text in satisfactions:
            hbox = QHBoxLayout()
            label = QLabel(f"{text}:")
            label.setMinimumWidth(70)
            progress = QProgressBar()
            progress.setRange(0, 100)
            progress.setValue(50)
            hbox.addWidget(label)
            hbox.addWidget(progress)
            satisfaction_layout.addLayout(hbox)
            self.progress_bars[key] = progress

        # Ajouter à la section de gauche
        left_layout.addWidget(satisfaction_group)

        # Groupe pour le taux d'imposition
        tax_group = QGroupBox("Taux d'imposition")
        tax_layout = QVBoxLayout(tax_group)

        # Slider pour le taux d'imposition
        self.tax_label = QLabel("Taux: 10%")
        self.tax_slider = QSlider(Qt.Horizontal)
        self.tax_slider.setRange(0, 50)  # 0% à 50%
        self.tax_slider.setValue(10)
        self.tax_slider.setTickPosition(QSlider.TicksBelow)
        self.tax_slider.setTickInterval(5)

        tax_layout.addWidget(self.tax_label)
        tax_layout.addWidget(self.tax_slider)

        # Connecter le slider
        self.tax_slider.valueChanged.connect(self._on_tax_changed)

        # Ajouter à la section du milieu
        middle_layout.addWidget(tax_group)

        # Groupe pour les graphiques
        graph_group = QGroupBox("Graphiques")
        graph_layout = QVBoxLayout(graph_group)
        graph_layout.setContentsMargins(
            5, 15, 5, 5
        )  # Plus de marge en haut pour le titre

        # Canvas matplotlib
        self.canvas = MplCanvas(
            self, width=9, height=4
        )  # Plus large pour mieux utiliser l'espace
        graph_layout.addWidget(self.canvas)

        # Ajouter à la section de droite (prend tout l'espace)
        right_layout.addWidget(graph_group)

        # Ajouter les layouts au layout principal
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(middle_layout, 1)
        main_layout.addLayout(right_layout, 3)  # Donner plus d'espace au graphique

        # Définir une taille minimale
        self.setMinimumWidth(300)

    @Slot(CityStats)
    def update_stats(self, stats: CityStats) -> None:
        """
        Met à jour les statistiques affichées.

        Parameters
        ----------
        stats : CityStats
            Les statistiques de la ville
        """
        # Mettre à jour les labels
        self.labels["population"].setText(f"Population: {stats.population}")
        self.labels["funds"].setText(f"Fonds: {stats.funds} €")
        self.labels["mayor_rating"].setText(
            f"Satisfaction du maire: {int(stats.mayor_rating * 100)}%"
        )

        # Mettre à jour les barres de progression
        self.progress_bars["space_satisfaction"].setValue(
            int(stats.space_satisfaction * 100)
        )
        self.progress_bars["job_satisfaction"].setValue(
            int(stats.job_satisfaction * 100)
        )
        self.progress_bars["leisure_satisfaction"].setValue(
            int(stats.leisure_satisfaction * 100)
        )
        self.progress_bars["wealth_satisfaction"].setValue(
            int(stats.wealth_satisfaction * 100)
        )

        # Mettre à jour le slider d'imposition (éviter les boucles de feedback)
        if abs(self.tax_slider.value() - int(stats.tax_rate * 100)) > 1:
            self.tax_slider.blockSignals(True)
            self.tax_slider.setValue(int(stats.tax_rate * 100))
            self.tax_slider.blockSignals(False)
            self.tax_label.setText(f"Taux: {int(stats.tax_rate * 100)}%")

        # Mettre à jour les graphiques
        self.y_data_pop = self.canvas.y_data_pop
        self.y_data_pop.append(stats.population)

        self.y_data_rating = self.canvas.y_data_rating
        self.y_data_rating.append(stats.mayor_rating * 100)

        # Mettre à jour les données des courbes
        self.canvas.pop_line.set_ydata(self.y_data_pop)
        self.canvas.rating_line.set_ydata(self.y_data_rating)

        # Adapter l'échelle du graphique
        max_pop = max(100, max(self.y_data_pop) * 1.1)
        self.canvas.axes.set_ylim(0, max_pop)

        # Redessiner le graphique
        self.canvas.draw()

    def get_tax_rate_signal(self):
        """
        Obtient le signal de changement du taux d'imposition.

        Returns
        -------
        Signal
            Le signal valueChanged du slider
        """
        return self.tax_slider.valueChanged

    @Slot(int)
    def _on_tax_changed(self, value: int) -> None:
        """
        Appelé lorsque le taux d'imposition est modifié.

        Parameters
        ----------
        value : int
            La nouvelle valeur du taux d'imposition (en pourcentage)
        """
        # Mettre à jour le label
        self.tax_label.setText(f"Taux: {value}%")
