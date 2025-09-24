# Chapitre 6 : Aspects avancés de Qt

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Maîtriser l'architecture MDI (Multiple Document Interface) avec QMdiArea et QMdiSubWindow
- Utiliser les fonctions de tracé avancées pour créer des graphiques personnalisés
- Implémenter des traitements asynchrones avec QRunnable et QThreadPool
- Gérer les opérations sur le système de fichiers avec les classes Qt
- Internationaliser une application PyQt6 pour supporter plusieurs langues
- Créer une application complexe combinant tous ces aspects

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Architecture MDI (Multiple Document Interface)

### 1.1 Qu'est-ce que l'architecture MDI ?

L'architecture **MDI** permet de gérer plusieurs documents ou vues dans une seule fenêtre principale. C'est l'approche utilisée par des applications comme Microsoft Word (versions anciennes), Photoshop, ou les IDE de développement.

#### 🏢 **Concepts clés**
- **QMdiArea** : Le conteneur principal qui gère toutes les sous-fenêtres
- **QMdiSubWindow** : Une sous-fenêtre individuelle contenant un widget
- **Document** : Le contenu réel de chaque sous-fenêtre

#### ✅ **Avantages de l'architecture MDI**
- Gestion centralisée de plusieurs documents
- Partage d'une barre de menu commune
- Navigation facile entre les documents
- Maximisation/minimisation indépendante

### 1.2 Premier exemple MDI

Créons une application MDI basique pour comprendre les concepts :

```python
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit


class MDIMainWindow(QMainWindow):
    """Fenêtre principale avec architecture MDI"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mon Application MDI")
        self.setGeometry(100, 100, 800, 600)

        # Créer la zone MDI
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        self.setup_actions()
        self.setup_menu()
        self.setup_initial_documents()

    def setup_actions(self) -> None:
        """Configure les actions"""
        self.new_action = QAction("Nouveau document", self)
        self.new_action.triggered.connect(lambda: self.create_text_document())

        self.quit_action = QAction("Quitter", self)
        self.quit_action.triggered.connect(self.close)

        self.cascade_action = QAction("Cascade", self)
        self.cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)

        self.mosaic_action = QAction("Mosaïque", self)
        self.mosaic_action.triggered.connect(self.mdi_area.tileSubWindows)

        self.close_all_action = QAction("Fermer tout", self)
        self.close_all_action.triggered.connect(self.mdi_area.closeAllSubWindows)

    def setup_menu(self) -> None:
        """Configure le menu principal"""
        menubar = self.menuBar()

        if (menubar := self.menuBar()) is None:
            return

        # Menu Fichier
        if (file_menu := menubar.addMenu("Fichier")) is None:
            return

        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        # Menu Fenêtre
        if (window_menu := menubar.addMenu("Fenêtre")) is None:
            return

        window_menu.addAction(self.cascade_action)
        window_menu.addAction(self.mosaic_action)
        window_menu.addSeparator()
        window_menu.addAction(self.close_all_action)

    def setup_initial_documents(self) -> None:
        """Crée quelques documents d'exemple"""
        self.create_text_document("Document 1")
        self.create_text_document("Document 2")

        # Organiser en cascade
        self.mdi_area.cascadeSubWindows()

    def create_text_document(self, title: str = "Nouveau document") -> QMdiSubWindow:
        """Crée un nouveau document texte"""
        # Créer le widget de contenu
        text_edit = QTextEdit()
        text_edit.setPlainText(f"Contenu de {title}")

        # Créer la sous-fenêtre
        sub_window = QMdiSubWindow()
        sub_window.setWidget(text_edit)
        sub_window.setWindowTitle(title)
        sub_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # Ajouter à la zone MDI
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

        return sub_window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MDIMainWindow()
    window.show()
    sys.exit(app.exec())
```

## 2. Programmation asynchrone avec les Threads

### 2.1 Pourquoi utiliser les Threads ?

Les **Threads** permettent d'exécuter des tâches longues sans bloquer l'interface utilisateur :

#### 🚫 **Problème sans Threads**
```python
# ❌ MAUVAIS : Bloque l'interface
def download_weather_data(self) -> None:
    for city in ["Paris", "Lyon", "Marseille"]:
        response = requests.get(f"https://api.weather.com/{city}")
        # L'interface est figée pendant 3 secondes !
        time.sleep(1)  # Simulation de délai réseau
```

#### ✅ **Solution avec Threads**
```python
# ✅ BON : Interface réactive
def download_weather_data(self) -> None:
    worker = WeatherWorker(["Paris", "Lyon", "Marseille"])
    worker.signals.data_received.connect(self.update_display)
    self.thread_pool.start(worker)
    # L'interface reste réactive !
```

### 2.2 Implémentation avec QRunnable et QThreadPool

Créons un système de workers typé et robuste :

```python
import sys
import time
from typing import Any

from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class WorkerSignals(QObject):
    """Signaux pour communiquer avec le thread principal"""

    # Signal émis quand des données sont reçues
    data_received = pyqtSignal(int, dict)  # (worker_id, data)

    # Signal émis en cas d'erreur
    error_occurred = pyqtSignal(int, str)  # (worker_id, error_message)

    # Signal émis quand le travail est terminé
    finished = pyqtSignal(int)  # (worker_id,)


class WeatherWorker(QRunnable):
    """Worker pour télécharger les données météo"""

    def __init__(self, worker_id: int, city: str) -> None:
        super().__init__()
        self.worker_id = worker_id
        self.city = city
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self) -> None:
        """Exécute le téléchargement des données"""
        try:
            # Simulation d'un appel API
            self.signals.data_received.emit(self.worker_id, {"city": self.city, "temp": 20.5, "humidity": 65})

            # Simulation de délai réseau
            time.sleep(1)

        except Exception as e:
            self.signals.error_occurred.emit(self.worker_id, str(e))
        finally:
            self.signals.finished.emit(self.worker_id)


class WeatherApp(QMainWindow):
    """Application météo avec workers"""

    def __init__(self) -> None:
        super().__init__()
        self.thread_pool = QThreadPool()
        self.active_workers: set[int] = set()

        print(f"Threads maximum : {self.thread_pool.maxThreadCount()}")

        button = QPushButton("Télécharger")
        button.clicked.connect(lambda: self.download_weather_for_cities(["Paris", "Lyon", "Marseille"]))

        self.setCentralWidget(button)

    def download_weather_for_cities(self, cities: list[str]) -> None:
        """Lance le téléchargement pour plusieurs villes"""
        for worker_id, city in enumerate(cities):
            worker = WeatherWorker(worker_id, city)

            # Connecter les signaux
            worker.signals.data_received.connect(self.on_data_received)
            worker.signals.error_occurred.connect(self.on_error_occurred)
            worker.signals.finished.connect(self.on_worker_finished)

            # Démarrer le worker
            self.active_workers.add(worker_id)
            self.thread_pool.start(worker)

    def on_data_received(self, worker_id: int, data: dict[str, Any]) -> None:
        """Traite les données reçues"""
        print(f"Worker {worker_id}: Données pour {data['city']}")
        # Mettre à jour l'interface utilisateur ici

    def on_error_occurred(self, worker_id: int, error: str) -> None:
        """Gère les erreurs"""
        print(f"Worker {worker_id}: Erreur - {error}")

    def on_worker_finished(self, worker_id: int) -> None:
        """Nettoie quand un worker se termine"""
        self.active_workers.discard(worker_id)
        print(f"Worker {worker_id} terminé. Restants: {len(self.active_workers)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
```

### 2.3 Règle essentielle

**🚨 IMPORTANT** : Jamais modifier l'interface depuis un thread ! Toujours utiliser les signaux pour communiquer avec l'interface principale.

---

## 3. Gestion du système de fichiers

Qt fournit des dialogues prêts à l'emploi pour sélectionner des fichiers :

```python
from PyQt6.QtWidgets import QFileDialog

# Ouvrir un fichier
file_path, _ = QFileDialog.getOpenFileName(
    self,
    "Ouvrir un fichier",
    "",
    "Fichiers texte (*.txt);;Tous les fichiers (*)"
)

# Sauvegarder un fichier
file_path, _ = QFileDialog.getSaveFileName(
    self,
    "Sauvegarder",
    "",
    "Fichiers JSON (*.json)"
)
```

## 4. Fonctions de tracé avancées

### 4.1 QPainter et les primitives de dessin

Qt propose un système de dessin puissant avec **QPainter** pour créer des graphiques personnalisés :

```python
import sys
from typing import override

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter, QPaintEvent, QPen
from PyQt6.QtWidgets import QApplication, QWidget


class ExampleChart(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Graphique - 3 Points")
        self.setGeometry(100, 100, 400, 300)

    @override
    def paintEvent(self, event: QPaintEvent | None) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 3 points de température fixes
        # Point 1: 10h, 20°C
        point1 = QPointF(100, 150)

        # Point 2: 14h, 25°C
        point2 = QPointF(200, 100)

        # Point 3: 18h, 22°C
        point3 = QPointF(300, 120)

        # Dessiner le fond
        painter.fillRect(50, 50, 300, 200, QColor(240, 248, 255))

        # Dessiner 2 lignes pour relier les 3 points
        painter.setPen(QPen(QColor(255, 0, 0), 3))  # Rouge épais
        painter.drawLine(point1, point2)  # Ligne 1-2
        painter.drawLine(point2, point3)  # Ligne 2-3

        # Dessiner les 3 points
        painter.setPen(QPen(QColor(0, 0, 255), 2))  # Bleu
        painter.drawEllipse(point1, 8, 8)  # Point 1
        painter.drawEllipse(point2, 8, 8)  # Point 2
        painter.drawEllipse(point3, 8, 8)  # Point 3

        # Étiquettes simples
        painter.setPen(QPen(QColor(0, 0, 0), 1))  # Noir
        painter.drawText(QPointF(90, 180), "10h: 20°C")
        painter.drawText(QPointF(190, 80), "14h: 25°C")
        painter.drawText(QPointF(290, 100), "18h: 22°C")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExampleChart()
    window.show()
    sys.exit(app.exec())
```

### 4.2 Primitives de dessin essentielles

**QPainter** offre toutes les primitives classiques :
- `drawRect()`, `drawEllipse()`, `drawLine()` - Formes de base
- `drawText()` - Texte avec police personnalisée
- `drawPolygon()` - Formes complexes
- `QPen` pour les contours, `QBrush` pour les remplissages

---

## 5. Internationalisation (i18n)

### 5.1 Principe de base

Pour supporter plusieurs langues, marquez les textes avec `self.tr()` :

```python
from PyQt6.QtCore import QTranslator, QCoreApplication

class MyApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.translator = QTranslator()
        
        # Textes traduisibles
        self.setWindowTitle(self.tr("Mon Application"))
        button = QPushButton(self.tr("Cliquez ici"))
```

### 5.2 Processus de traduction

```bash
# 1. Extraire les chaînes
pylupdate6 *.py -ts app_fr.ts

# 2. Traduire le fichier .ts avec un éditeur

# 3. Compiler
lrelease app_fr.ts
```

### 5.3 Changer de langue

```python
def change_language(self, lang_code: str) -> None:
    if self.translator.load(f"app_{lang_code}.qm"):
        QCoreApplication.installTranslator(self.translator)
        # Mettre à jour l'interface
        self.retranslate_ui()
```

---

## 6. Travaux pratiques

Les 3 TPs explorent les aspects avancés de Qt avec des exemples pratiques :

### 🌐 TP1 - Téléchargement asynchrone de données
**Durée** : 30 minutes  
**Objectif** : Découvrir les threads avec QRunnable

**À réaliser** :
- Créer un `WeatherWorker` pour simuler des téléchargements
- Utiliser QThreadPool pour gérer 3 workers en parallèle (Paris, Lyon, Marseille)
- Connecter les signaux pour afficher les résultats dans un QTextEdit
- Ajouter un bouton pour déclencher les téléchargements

**Concepts abordés** : QRunnable, QThreadPool, signaux inter-threads

### 📊 TP2 - Graphiques personnalisés avec les données
**Durée** : 30 minutes  
**Objectif** : Utiliser QPainter pour tracer un graphique simple

**À réaliser** :
- Créer un widget personnalisé héritant de QWidget
- Implémenter `paintEvent()` pour dessiner 3 points de température
- Tracer 2 segments reliant les 3 points
- Intégrer le graphique avec les données du TP1

**Concepts abordés** : QPainter, dessin personnalisé, `paintEvent()`

### 🌍 TP3 - Internationalisation *(optionnel)*
**Durée** : 30 minutes  
**Objectif** : Ajouter le support multilingue

**À réaliser** :
- Marquer les textes avec `self.tr()`
- Créer les fichiers de traduction français/anglais
- Ajouter un menu "Langue" pour changer dynamiquement
- Tester le changement en temps réel

**Concepts abordés** : QTranslator, processus de traduction, `tr()`

---

## 7. Points clés à retenir

### ✅ Architecture MDI
- **QMdiArea** : Conteneur principal pour gérer plusieurs documents
- **QMdiSubWindow** : Chaque document dans sa propre sous-fenêtre
- **Disposition** : cascade, mosaïque, ou arrangements personnalisés

### ✅ Dessin personnalisé
- **QPainter** : Outil principal pour le dessin
- **paintEvent()** : Méthode à surcharger pour dessiner
- **Antialiasing** : Améliore la qualité visuelle

### ✅ Threads asynchrones
- **QRunnable** : Classe de base pour les tâches asynchrones
- **QThreadPool** : Gestionnaire de pool de threads
- **Signaux** : Communication sécurisée entre threads

### ✅ Gestion des fichiers
- **QFileDialog** : Dialogues ouvrir/sauvegarder
- **QStandardPaths** : Emplacements système standards

### ✅ Internationalisation
- **QTranslator** : Gestionnaire de traductions
- **tr()** : Marquer les chaînes traduisibles
- **Processus** : lupdate → traduire → lrelease

---
