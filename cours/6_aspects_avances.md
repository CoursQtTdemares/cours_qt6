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
from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow,
    QTextEdit, QMenuBar, QMenu, QVBoxLayout, QWidget
)

class MDIMainWindow(QMainWindow):
    """Fenêtre principale avec architecture MDI"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mon Application MDI")
        self.setGeometry(100, 100, 800, 600)
        
        # Créer la zone MDI
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        
        # Configurer l'apparence
        self.mdi_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.mdi_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        self.setup_menu()
        self.setup_initial_documents()
    
    def setup_menu(self) -> None:
        """Configure le menu principal"""
        menubar = self.menuBar()
        
        # Menu Fichier
        file_menu = menubar.addMenu("Fichier")
        file_menu.addAction("Nouveau document", self.create_text_document)
        file_menu.addSeparator()
        file_menu.addAction("Quitter", self.close)
        
        # Menu Fenêtre
        window_menu = menubar.addMenu("Fenêtre")
        window_menu.addAction("Cascade", self.mdi_area.cascadeSubWindows)
        window_menu.addAction("Mosaïque", self.mdi_area.tileSubWindows)
        window_menu.addSeparator()
        window_menu.addAction("Fermer tout", self.mdi_area.closeAllSubWindows)
    
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

### 1.3 Stratégies de positionnement

QMdiArea propose plusieurs stratégies pour organiser les sous-fenêtres :

```python
from PyQt6.QtWidgets import QMdiArea

class AdvancedMDIArea(QMdiArea):
    """Zone MDI avec stratégies de positionnement avancées"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setup_view_mode()
    
    def setup_view_mode(self) -> None:
        """Configure le mode d'affichage"""
        # Mode par défaut : fenêtres libres
        self.setViewMode(QMdiArea.ViewMode.SubWindowView)
        
        # Alternative : mode onglets
        # self.setViewMode(QMdiArea.ViewMode.TabbedView)
    
    def arrange_cascade(self) -> None:
        """Organise les fenêtres en cascade"""
        self.cascadeSubWindows()
    
    def arrange_tile(self) -> None:
        """Organise les fenêtres en mosaïque"""
        self.tileSubWindows()
    
    def arrange_horizontal(self) -> None:
        """Organise les fenêtres horizontalement"""
        sub_windows = self.subWindowList()
        if not sub_windows:
            return
        
        area_size = self.size()
        window_width = area_size.width() // len(sub_windows)
        
        for i, window in enumerate(sub_windows):
            window.resize(window_width, area_size.height())
            window.move(i * window_width, 0)
    
    def arrange_vertical(self) -> None:
        """Organise les fenêtres verticalement"""
        sub_windows = self.subWindowList()
        if not sub_windows:
            return
        
        area_size = self.size()
        window_height = area_size.height() // len(sub_windows)
        
        for i, window in enumerate(sub_windows):
            window.resize(area_size.width(), window_height)
            window.move(0, i * window_height)
```

---

## 2. Fonctions de tracé avancées

### 2.1 QPainter et les primitives de dessin

Qt propose un système de dessin puissant avec **QPainter** pour créer des graphiques personnalisés :

```python
from typing import Optional
from PyQt6.QtCore import QRectF, QPointF
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PyQt6.QtWidgets import QWidget

class WeatherChartWidget(QWidget):
    """Widget personnalisé pour afficher un graphique météo"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setMinimumSize(400, 300)
        
        # Données d'exemple (température par heure)
        self.temperatures: list[float] = [12.5, 13.2, 14.1, 15.8, 17.2, 18.5, 19.1, 18.8]
        self.hours: list[str] = ["8h", "9h", "10h", "11h", "12h", "13h", "14h", "15h"]
    
    def paintEvent(self, event) -> None:
        """Dessine le graphique de température"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Préparer la zone de dessin
        rect = self.rect()
        margin = 40
        chart_rect = QRectF(
            margin, margin,
            rect.width() - 2 * margin,
            rect.height() - 2 * margin
        )
        
        self.draw_background(painter, chart_rect)
        self.draw_axes(painter, chart_rect)
        self.draw_temperature_curve(painter, chart_rect)
        self.draw_labels(painter, chart_rect)
    
    def draw_background(self, painter: QPainter, chart_rect: QRectF) -> None:
        """Dessine le fond du graphique"""
        # Fond dégradé bleu clair
        brush = QBrush(QColor(240, 248, 255))
        painter.fillRect(chart_rect, brush)
        
        # Bordure
        pen = QPen(QColor(100, 149, 237), 2)
        painter.setPen(pen)
        painter.drawRect(chart_rect)
    
    def draw_axes(self, painter: QPainter, chart_rect: QRectF) -> None:
        """Dessine les axes du graphique"""
        pen = QPen(QColor(128, 128, 128), 1)
        painter.setPen(pen)
        
        # Lignes de grille horizontales
        for i in range(5):
            y = chart_rect.top() + (i * chart_rect.height() / 4)
            painter.drawLine(
                chart_rect.left(), y,
                chart_rect.right(), y
            )
    
    def draw_temperature_curve(self, painter: QPainter, chart_rect: QRectF) -> None:
        """Dessine la courbe de température"""
        if len(self.temperatures) < 2:
            return
        
        # Calculer les échelles
        min_temp = min(self.temperatures)
        max_temp = max(self.temperatures)
        temp_range = max_temp - min_temp or 1
        
        # Préparer le pinceau pour la courbe
        pen = QPen(QColor(255, 69, 0), 3)
        painter.setPen(pen)
        
        # Dessiner la courbe point par point
        points: list[QPointF] = []
        for i, temp in enumerate(self.temperatures):
            x = chart_rect.left() + (i * chart_rect.width() / (len(self.temperatures) - 1))
            y = chart_rect.bottom() - ((temp - min_temp) / temp_range * chart_rect.height())
            points.append(QPointF(x, y))
        
        # Tracer les segments
        for i in range(len(points) - 1):
            painter.drawLine(points[i], points[i + 1])
        
        # Dessiner les points
        brush = QBrush(QColor(255, 69, 0))
        painter.setBrush(brush)
        for point in points:
            painter.drawEllipse(point, 4, 4)
    
    def draw_labels(self, painter: QPainter, chart_rect: QRectF) -> None:
        """Dessine les étiquettes"""
        font = QFont("Arial", 10)
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))
        
        # Labels des heures
        for i, hour in enumerate(self.hours):
            x = chart_rect.left() + (i * chart_rect.width() / (len(self.hours) - 1))
            y = chart_rect.bottom() + 20
            painter.drawText(QPointF(x - 10, y), hour)
```

### 2.2 Primitives de dessin essentielles

**QPainter** offre toutes les primitives classiques :
- `drawRect()`, `drawEllipse()`, `drawLine()` - Formes de base
- `drawText()` - Texte avec police personnalisée
- `drawPolygon()` - Formes complexes
- `QPen` pour les contours, `QBrush` pour les remplissages

---

## 3. Programmation asynchrone avec les Threads

### 3.1 Pourquoi utiliser les Threads ?

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

### 3.2 Implémentation avec QRunnable et QThreadPool

Créons un système de workers typé et robuste :

```python
from typing import Any, Callable
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
import requests
import time

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
            self.signals.data_received.emit(
                self.worker_id,
                {"city": self.city, "temp": 20.5, "humidity": 65}
            )
            
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
```

### 3.3 Règle essentielle

**🚨 IMPORTANT** : Jamais modifier l'interface depuis un thread ! Toujours utiliser les signaux pour communiquer avec l'interface principale.

---

## 4. Gestion du système de fichiers

### 4.1 Dialogues de fichiers

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

### 4.2 Emplacements système

`QStandardPaths` permet d'accéder aux dossiers système standards :

```python
from PyQt6.QtCore import QStandardPaths

# Dossier Documents
docs_path = QStandardPaths.writableLocation(
    QStandardPaths.StandardLocation.DocumentsLocation
)

# Dossier de configuration de l'application
app_data = QStandardPaths.writableLocation(
    QStandardPaths.StandardLocation.AppDataLocation
)
```

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

Les 4 TPs construisent progressivement une **application météo MDI** complète :

### 🌤️ TP1 - Interface MDI météo de base
**Durée** : 30 minutes  
**Objectif** : Créer l'architecture MDI avec différents types de documents

**À réaliser** :
- Créer une fenêtre principale avec QMdiArea
- Implémenter 3 types de documents : "Vue actuelle", "Prévisions", "Graphiques"
- Ajouter un menu "Fenêtre" avec options de disposition (cascade, mosaïque)
- Créer des sous-fenêtres avec contenu basique (QLabel avec texte d'exemple)

**Concepts abordés** : QMdiArea, QMdiSubWindow, gestion des menus

### 📊 TP2 - Graphiques météo personnalisés
**Durée** : 30 minutes  
**Objectif** : Utiliser QPainter pour créer des graphiques météo

**À réaliser** :
- Créer un widget personnalisé héritant de QWidget
- Implémenter `paintEvent()` pour dessiner un graphique de températures
- Ajouter ce widget dans une sous-fenêtre MDI "Graphiques"
- Dessiner courbe, axes, grille et étiquettes

**Concepts abordés** : QPainter, dessin personnalisé, intégration dans MDI

### 🌐 TP3 - Téléchargement asynchrone de données
**Durée** : 30 minutes  
**Objectif** : Implémenter des workers pour récupérer des données météo

**À réaliser** :
- Créer un `WeatherWorker` héritant de `QRunnable`
- Implémenter le téléchargement simulé de données pour plusieurs villes
- Connecter les signaux pour mettre à jour l'interface
- Afficher les données dans une nouvelle sous-fenêtre "Données temps réel"

**Concepts abordés** : QRunnable, QThreadPool, signaux inter-threads

### 🌍 TP4 - Internationalisation *(optionnel)*
**Durée** : 30 minutes  
**Objectif** : Ajouter le support multilingue

**À réaliser** :
- Marquer tous les textes avec `self.tr()`
- Créer les fichiers de traduction (.ts) pour français et anglais
- Ajouter un menu "Langue" pour changer la langue à la volée
- Tester le changement de langue en temps réel

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
