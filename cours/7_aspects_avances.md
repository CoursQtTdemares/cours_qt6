# Chapitre 7 : Aspects avancés

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Implémenter une architecture MDI (Multiple Document Interface) avec QMdiArea
- Utiliser QPainter pour créer des graphiques 2D personnalisés
- Gérer les styles et thèmes graphiques avec CSS avancé
- Travailler avec les threads Qt (QThread) et les timers (QTimer)
- Manipuler le système de fichiers avec QDir et QFile
- Internationaliser une application avec QTranslator
- Appliquer les techniques avancées de Qt pour des applications professionnelles

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Architecture MDI (Multiple Document Interface)

### 1.1 Introduction au MDI avec QMdiArea

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, 
    QTextEdit, QVBoxLayout, QWidget, QMenuBar, QMenu, QMessageBox
)
from PyQt6.QtCore import Qt
import sys

class MDIMainWindow(QMainWindow):
    """Fenêtre principale MDI"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application MDI")
        self.setGeometry(100, 100, 1000, 700)
        
        # Zone MDI centrale
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        
        # Configuration MDI
        self.mdi_area.setViewMode(QMdiArea.ViewMode.TabbedView)
        self.mdi_area.setTabsClosable(True)
        
        self.setup_menus()
        self.document_count = 0
    
    def setup_menus(self):
        """Configure les menus MDI"""
        menubar = self.menuBar()
        
        # Menu Fichier
        file_menu = menubar.addMenu("&Fichier")
        
        new_action = file_menu.addAction("&Nouveau document")
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_document)
        
        # Menu Fenêtre
        window_menu = menubar.addMenu("&Fenêtre")
        
        tile_action = window_menu.addAction("Mosaïque")
        tile_action.triggered.connect(self.mdi_area.tileSubWindows)
        
        cascade_action = window_menu.addAction("Cascade")
        cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        
        close_all_action = window_menu.addAction("Fermer tout")
        close_all_action.triggered.connect(self.mdi_area.closeAllSubWindows)
    
    def new_document(self):
        """Crée un nouveau document"""
        self.document_count += 1
        
        # Widget de contenu
        text_edit = QTextEdit()
        text_edit.setPlainText(f"Document {self.document_count}\n\nContenu du document...")
        
        # Sous-fenêtre MDI
        sub_window = QMdiSubWindow()
        sub_window.setWidget(text_edit)
        sub_window.setWindowTitle(f"Document {self.document_count}")
        
        # Ajouter à la zone MDI
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()
        
        return sub_window

class CustomMDIChild(QWidget):
    """Widget enfant MDI personnalisé"""
    
    def __init__(self, title="Nouveau document"):
        super().__init__()
        self.title = title
        self.is_modified = False
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.mark_modified)
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)
    
    def mark_modified(self):
        """Marque le document comme modifié"""
        self.is_modified = True
        self.update_title()
    
    def update_title(self):
        """Met à jour le titre avec indicateur de modification"""
        title = self.title
        if self.is_modified:
            title += " *"
        
        parent = self.parent()
        if parent and isinstance(parent, QMdiSubWindow):
            parent.setWindowTitle(title)
```

### 1.2 Gestion avancée des sous-fenêtres

```python
class AdvancedMDIArea(QMdiArea):
    """Zone MDI avec fonctionnalités avancées"""
    
    def __init__(self):
        super().__init__()
        self.setup_advanced_features()
    
    def setup_advanced_features(self):
        """Configure les fonctionnalités avancées"""
        # Politique de fermeture
        self.setDocumentMode(True)
        self.setTabsMovable(True)
        
        # Connexions
        self.subWindowActivated.connect(self.on_subwindow_activated)
    
    def on_subwindow_activated(self, window):
        """Réaction à l'activation d'une sous-fenêtre"""
        if window:
            print(f"Fenêtre activée: {window.windowTitle()}")

class MDIDocument:
    """Gestionnaire de documents MDI"""
    
    def __init__(self, mdi_area):
        self.mdi_area = mdi_area
        self.documents = []
    
    def create_document(self, document_type="text"):
        """Crée un document selon le type"""
        if document_type == "text":
            widget = QTextEdit()
        elif document_type == "image":
            widget = QLabel("Éditeur d'image")
        
        sub_window = QMdiSubWindow()
        sub_window.setWidget(widget)
        sub_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        
        self.mdi_area.addSubWindow(sub_window)
        self.documents.append(sub_window)
        
        sub_window.show()
        return sub_window
```

---

## 2. Fonctions de tracé avec QPainter

### 2.1 Dessin 2D basique

```python
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont
from PyQt6.QtCore import QRect, QPoint

class DrawingWidget(QWidget):
    """Widget de dessin personnalisé"""
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.shapes = []
    
    def paintEvent(self, event):
        """Événement de peinture"""
        painter = QPainter(self)
        
        # Configuration antialiasing
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Dessiner l'arrière-plan
        painter.fillRect(self.rect(), QColor(240, 240, 240))
        
        # Dessiner les formes
        self.draw_basic_shapes(painter)
        self.draw_text(painter)
        self.draw_custom_shapes(painter)
    
    def draw_basic_shapes(self, painter):
        """Dessine des formes de base"""
        # Rectangle
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.setBrush(QBrush(QColor(255, 200, 200)))
        painter.drawRect(10, 10, 100, 60)
        
        # Ellipse
        painter.setPen(QPen(QColor(0, 255, 0), 3))
        painter.setBrush(QBrush(QColor(200, 255, 200)))
        painter.drawEllipse(130, 10, 80, 80)
        
        # Ligne
        painter.setPen(QPen(QColor(0, 0, 255), 4))
        painter.drawLine(10, 100, 200, 150)
    
    def draw_text(self, painter):
        """Dessine du texte formaté"""
        painter.setPen(QPen(QColor(0, 0, 0)))
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        
        rect = QRect(10, 180, 200, 50)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Texte centré")
    
    def draw_custom_shapes(self, painter):
        """Dessine des formes personnalisées"""
        # Polygone
        from PyQt6.QtGui import QPolygon
        
        points = [QPoint(250, 50), QPoint(300, 20), QPoint(350, 50), 
                 QPoint(320, 100), QPoint(280, 100)]
        polygon = QPolygon(points)
        
        painter.setPen(QPen(QColor(255, 0, 255), 2))
        painter.setBrush(QBrush(QColor(255, 200, 255)))
        painter.drawPolygon(polygon)

class InteractiveDrawing(QWidget):
    """Widget de dessin interactif"""
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)
        self.drawing = False
        self.last_point = QPoint()
        self.path_points = []
    
    def mousePressEvent(self, event):
        """Début du dessin"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()
            self.path_points = [self.last_point]
    
    def mouseMoveEvent(self, event):
        """Dessin en cours"""
        if self.drawing:
            self.path_points.append(event.position().toPoint())
            self.update()
    
    def mouseReleaseEvent(self, event):
        """Fin du dessin"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
    
    def paintEvent(self, event):
        """Dessine le chemin"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Arrière-plan
        painter.fillRect(self.rect(), QColor(255, 255, 255))
        
        # Dessiner le chemin
        if len(self.path_points) > 1:
            painter.setPen(QPen(QColor(0, 0, 255), 3))
            
            for i in range(1, len(self.path_points)):
                painter.drawLine(self.path_points[i-1], self.path_points[i])
```

### 2.2 Transformations et animations

```python
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve

class AnimatedDrawing(QWidget):
    """Widget avec animations de dessin"""
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        
        self.rotation_angle = 0
        self.scale_factor = 1.0
        
        # Timer pour animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)  # 20 FPS
    
    def animate(self):
        """Animation continue"""
        self.rotation_angle += 2
        self.scale_factor = 1.0 + 0.3 * abs(math.sin(self.rotation_angle * 0.1))
        self.update()
    
    def paintEvent(self, event):
        """Dessine avec transformations"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Centre du widget
        center_x = self.width() // 2
        center_y = self.height() // 2
        
        # Sauvegarder l'état du painter
        painter.save()
        
        # Appliquer les transformations
        painter.translate(center_x, center_y)
        painter.rotate(self.rotation_angle)
        painter.scale(self.scale_factor, self.scale_factor)
        
        # Dessiner une forme
        painter.setPen(QPen(QColor(255, 0, 0), 3))
        painter.setBrush(QBrush(QColor(255, 200, 200)))
        painter.drawRect(-50, -50, 100, 100)
        
        # Restaurer l'état
        painter.restore()
        
        # Dessiner sans transformation
        painter.setPen(QPen(QColor(0, 0, 255), 2))
        painter.drawText(10, 20, f"Rotation: {self.rotation_angle}°")
```

---

## 3. Gestion des styles CSS avancés

### 3.1 Système de thèmes complet

```python
class ThemeManager:
    """Gestionnaire de thèmes avancé"""
    
    def __init__(self):
        self.themes = {
            'clair': self.light_theme(),
            'sombre': self.dark_theme(),
            'bleu': self.blue_theme()
        }
        self.current_theme = 'clair'
    
    def light_theme(self):
        return """
        QMainWindow {
            background-color: #f5f5f5;
            color: #333333;
        }
        
        QMenuBar {
            background-color: #ffffff;
            border-bottom: 1px solid #ddd;
            padding: 4px;
        }
        
        QMenuBar::item {
            background-color: transparent;
            padding: 8px 16px;
            border-radius: 4px;
        }
        
        QMenuBar::item:selected {
            background-color: #e3f2fd;
        }
        
        QPushButton {
            background-color: #2196f3;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #1976d2;
        }
        
        QPushButton:pressed {
            background-color: #0d47a1;
        }
        """
    
    def dark_theme(self):
        return """
        QMainWindow {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        
        QMenuBar {
            background-color: #3c3c3c;
            color: #ffffff;
            border-bottom: 1px solid #555;
        }
        
        QMenuBar::item:selected {
            background-color: #555555;
        }
        
        QPushButton {
            background-color: #0078d4;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
        }
        
        QTextEdit {
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #555;
        }
        """
    
    def blue_theme(self):
        return """
        QMainWindow {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #87ceeb, stop: 1 #4682b4);
            color: #000080;
        }
        
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #87ceeb, stop: 1 #4682b4);
            border: 2px solid #4682b4;
            border-radius: 8px;
            padding: 6px 12px;
        }
        """
    
    def apply_theme(self, widget, theme_name):
        """Applique un thème à un widget"""
        if theme_name in self.themes:
            widget.setStyleSheet(self.themes[theme_name])
            self.current_theme = theme_name

class StyledApplication(QMainWindow):
    """Application avec gestion de thèmes"""
    
    def __init__(self):
        super().__init__()
        self.theme_manager = ThemeManager()
        self.setup_ui()
        self.setup_theme_menu()
    
    def setup_theme_menu(self):
        """Menu de sélection de thème"""
        theme_menu = self.menuBar().addMenu("&Thème")
        
        for theme_name in self.theme_manager.themes.keys():
            action = theme_menu.addAction(theme_name.title())
            action.triggered.connect(
                lambda checked, name=theme_name: self.change_theme(name)
            )
    
    def change_theme(self, theme_name):
        """Change le thème de l'application"""
        self.theme_manager.apply_theme(self, theme_name)
```

---

## 4. Threading avec QThread

### 4.1 Threads de base

```python
from PyQt6.QtCore import QThread, pyqtSignal, QMutex, QWaitCondition

class WorkerThread(QThread):
    """Thread de travail basique"""
    
    # Signaux pour communication
    progress = pyqtSignal(int)
    finished_work = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.is_running = False
    
    def run(self):
        """Exécution du thread"""
        try:
            self.is_running = True
            
            for i in range(101):
                if not self.is_running:
                    break
                
                # Simulation de travail
                self.msleep(50)  # 50ms
                
                # Émission du signal de progression
                self.progress.emit(i)
            
            self.finished_work.emit("Travail terminé avec succès")
            
        except Exception as e:
            self.error_occurred.emit(str(e))
    
    def stop(self):
        """Arrête le thread"""
        self.is_running = False

class ThreadedApplication(QMainWindow):
    """Application utilisant des threads"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.worker_thread = None
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        
        self.start_button = QPushButton("Démarrer travail")
        self.start_button.clicked.connect(self.start_work)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("Arrêter")
        self.stop_button.clicked.connect(self.stop_work)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        central_widget.setLayout(layout)
    
    def start_work(self):
        """Démarre le travail en arrière-plan"""
        self.worker_thread = WorkerThread()
        
        # Connexions des signaux
        self.worker_thread.progress.connect(self.progress_bar.setValue)
        self.worker_thread.finished_work.connect(self.on_work_finished)
        self.worker_thread.error_occurred.connect(self.on_error)
        
        # Démarrer le thread
        self.worker_thread.start()
        
        # Interface utilisateur
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
    
    def stop_work(self):
        """Arrête le travail"""
        if self.worker_thread:
            self.worker_thread.stop()
            self.worker_thread.wait()  # Attendre la fin
        
        self.reset_ui()
    
    def on_work_finished(self, message):
        """Travail terminé"""
        QMessageBox.information(self, "Terminé", message)
        self.reset_ui()
    
    def on_error(self, error_message):
        """Erreur dans le thread"""
        QMessageBox.critical(self, "Erreur", error_message)
        self.reset_ui()
    
    def reset_ui(self):
        """Remet l'interface à l'état initial"""
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.progress_bar.setValue(0)
```

---

## 5. Gestion du système de fichiers

### 5.1 QDir et QFile

```python
from PyQt6.QtCore import QDir, QFile, QTextStream, QFileInfo

class FileManager:
    """Gestionnaire de fichiers Qt"""
    
    def __init__(self, base_path="."):
        self.base_dir = QDir(base_path)
    
    def list_files(self, pattern="*"):
        """Liste les fichiers selon un pattern"""
        filters = QDir.Filter.Files | QDir.Filter.NoDotAndDotDot
        files = self.base_dir.entryList([pattern], filters)
        return files
    
    def create_directory(self, dir_name):
        """Crée un répertoire"""
        return self.base_dir.mkdir(dir_name)
    
    def read_file(self, filename):
        """Lit un fichier texte"""
        file_path = self.base_dir.absoluteFilePath(filename)
        file = QFile(file_path)
        
        if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            content = stream.readAll()
            file.close()
            return content
        return None
    
    def write_file(self, filename, content):
        """Écrit dans un fichier"""
        file_path = self.base_dir.absoluteFilePath(filename)
        file = QFile(file_path)
        
        if file.open(QFile.OpenModeFlag.WriteOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(file)
            stream << content
            file.close()
            return True
        return False
    
    def get_file_info(self, filename):
        """Obtient les informations d'un fichier"""
        file_path = self.base_dir.absoluteFilePath(filename)
        info = QFileInfo(file_path)
        
        return {
            'exists': info.exists(),
            'size': info.size(),
            'modified': info.lastModified(),
            'is_readable': info.isReadable(),
            'is_writable': info.isWritable()
        }
```

---

## 6. Internationalisation avec QTranslator

### 6.1 Système de traduction

```python
from PyQt6.QtCore import QTranslator, QLocale, QCoreApplication

class TranslationManager:
    """Gestionnaire de traductions"""
    
    def __init__(self, app):
        self.app = app
        self.translator = QTranslator()
        self.current_language = 'fr'
    
    def load_language(self, language_code):
        """Charge une langue"""
        # Désinstaller l'ancien traducteur
        self.app.removeTranslator(self.translator)
        
        # Charger la nouvelle traduction
        translation_file = f"translations/app_{language_code}.qm"
        
        if self.translator.load(translation_file):
            self.app.installTranslator(self.translator)
            self.current_language = language_code
            return True
        return False
    
    def tr(self, text):
        """Fonction de traduction"""
        return QCoreApplication.translate("MainWindow", text)

class MultilingualApp(QMainWindow):
    """Application multilingue"""
    
    def __init__(self):
        super().__init__()
        self.translation_manager = TranslationManager(QApplication.instance())
        self.setup_ui()
        self.setup_language_menu()
    
    def setup_language_menu(self):
        """Menu de sélection de langue"""
        lang_menu = self.menuBar().addMenu("&Langue")
        
        languages = [
            ('fr', 'Français'),
            ('en', 'English'),
            ('es', 'Español')
        ]
        
        for code, name in languages:
            action = lang_menu.addAction(name)
            action.triggered.connect(
                lambda checked, c=code: self.change_language(c)
            )
    
    def change_language(self, language_code):
        """Change la langue de l'interface"""
        if self.translation_manager.load_language(language_code):
            self.retranslate_ui()
    
    def retranslate_ui(self):
        """Met à jour les textes traduits"""
        tr = self.translation_manager.tr
        self.setWindowTitle(tr("Mon Application"))
        # Mettre à jour tous les textes...
```

---

## 7. Travaux pratiques

### 🚧 TP1 - Application MDI complète
**Durée** : 30 minutes
- Créer une application MDI avec différents types de documents
- Implémenter la gestion des fenêtres et des menus

### 🚧 TP2 - Éditeur graphique avec QPainter
**Durée** : 30 minutes  
- Développer un mini-éditeur de formes géométriques
- Ajouter des transformations et animations

### 🚧 TP3 - Gestionnaire de fichiers avancé
**Durée** : 30 minutes
- Créer un explorateur de fichiers avec threads
- Intégrer la gestion des styles et thèmes

### 🚧 TP4 - Application multilingue
**Durée** : 30 minutes
- Internationaliser une application existante
- Créer les fichiers de traduction et les menus de langues

---

## 8. Points clés à retenir

### ✅ Architecture MDI
- **QMdiArea** pour les applications multi-documents
- Gestion flexible des sous-fenêtres et de leur cycle de vie
- Interface utilisateur adaptée aux workflows complexes

### ✅ Dessin personnalisé
- **QPainter** pour les graphiques 2D avancés
- Transformations, animations et rendu haute qualité
- Intégration dans les widgets pour interfaces riches

### ✅ Threading et performance
- **QThread** pour les tâches longues sans bloquer l'interface
- Communication par signaux pour la sécurité des threads
- Gestion propre du cycle de vie des threads

### ✅ Internationalisation
- **QTranslator** pour supporter plusieurs langues
- Workflow de traduction avec fichiers .ts/.qm
- Interface adaptative aux différentes cultures

---

## Prochaine étape

Dans le **Chapitre 8 - Projets pratiques et intégration**, nous mettrons en pratique :
- Le développement d'applications complètes end-to-end
- Les bonnes pratiques et patterns de développement Qt
- Les techniques de tests, debugging et packaging
- La distribution et déploiement d'applications PyQt6
