# Chapitre 2 : Principes généraux de PyQt6

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Structurer une application Qt complète avec fenêtre principale
- Créer et organiser des barres de menus, d'outils et de statut
- Intégrer des styles CSS pour personnaliser l'apparence
- Implémenter des menus contextuels interactifs
- Gérer l'interconnexion entre les différents éléments d'interface
- Appliquer les bonnes pratiques d'architecture Qt

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Architecture d'une application Qt complète

### 1.1 La fenêtre principale (QMainWindow)

`QMainWindow` est la classe de base recommandée pour la fenêtre principale d'une application. Elle fournit un framework structuré avec des zones prédéfinies :

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QLabel, QMenuBar, QToolBar, QStatusBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon Application PyQt6")
        self.setGeometry(100, 100, 800, 600)
        
        # Widget central obligatoire
        self.setup_central_widget()
        
        # Barres d'interface
        self.setup_menu_bar()
        self.setup_tool_bar()
        self.setup_status_bar()
    
    def setup_central_widget(self):
        """Configure le widget central"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Contenu principal
        label = QLabel("Zone de contenu principal")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
```

### 1.2 Les zones de l'interface QMainWindow

```
┌─────────────────────────────────────┐
│            Barre de Menu            │
├─────────────────────────────────────┤
│            Barre d'Outils           │
├─────────────────────────────────────┤
│                                     │
│         Widget Central              │
│       (Zone principale)             │
│                                     │
├─────────────────────────────────────┤
│           Barre de Statut           │
└─────────────────────────────────────┘
```

#### Zones disponibles :
- **MenuBar** : Menus déroulants (Fichier, Édition, etc.)
- **ToolBar** : Boutons d'accès rapide avec icônes
- **CentralWidget** : Zone principale de l'application (obligatoire)
- **StatusBar** : Informations d'état et messages temporaires
- **DockWidgets** : Panneaux détachables (abordé plus tard)

### 1.3 Cycle de vie d'une application Qt

```python
def main():
    # 1. Création de l'application
    app = QApplication(sys.argv)
    
    # 2. Configuration globale (optionnel)
    app.setApplicationName("Mon App")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Mon Entreprise")
    
    # 3. Création de la fenêtre principale
    window = MainWindow()
    
    # 4. Affichage de la fenêtre
    window.show()
    
    # 5. Démarrage de la boucle d'événements
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

---

## 2. Barres de menus (QMenuBar)

### 2.1 Création d'une barre de menus

```python
def setup_menu_bar(self):
    """Configure la barre de menus"""
    menubar = self.menuBar()
    
    # Menu Fichier
    file_menu = menubar.addMenu("&Fichier")
    
    # Action Nouveau
    new_action = QAction("&Nouveau", self)
    new_action.setShortcut("Ctrl+N")
    new_action.setStatusTip("Créer un nouveau document")
    new_action.triggered.connect(self.new_file)
    file_menu.addAction(new_action)
    
    # Action Ouvrir
    open_action = QAction("&Ouvrir", self)
    open_action.setShortcut("Ctrl+O")
    open_action.setStatusTip("Ouvrir un document existant")
    open_action.triggered.connect(self.open_file)
    file_menu.addAction(open_action)
    
    # Séparateur
    file_menu.addSeparator()
    
    # Action Quitter
    exit_action = QAction("&Quitter", self)
    exit_action.setShortcut("Ctrl+Q")
    exit_action.setStatusTip("Quitter l'application")
    exit_action.triggered.connect(self.close)
    file_menu.addAction(exit_action)

def new_file(self):
    """Gestionnaire pour nouveau fichier"""
    self.statusBar().showMessage("Nouveau fichier créé", 2000)

def open_file(self):
    """Gestionnaire pour ouvrir fichier"""
    self.statusBar().showMessage("Ouverture d'un fichier...", 2000)
```

### 2.2 Menus hiérarchiques et actions avancées

```python
def setup_advanced_menus(self):
    """Exemples de menus avancés"""
    menubar = self.menuBar()
    
    # Menu Édition avec sous-menus
    edit_menu = menubar.addMenu("&Édition")
    
    # Sous-menu "Insérer"
    insert_menu = edit_menu.addMenu("&Insérer")
    insert_menu.addAction("Image").triggered.connect(self.insert_image)
    insert_menu.addAction("Tableau").triggered.connect(self.insert_table)
    
    # Action avec case à cocher
    word_wrap_action = QAction("Retour à la &ligne", self)
    word_wrap_action.setCheckable(True)
    word_wrap_action.setChecked(True)
    word_wrap_action.toggled.connect(self.toggle_word_wrap)
    edit_menu.addAction(word_wrap_action)
    
    # Actions groupées (radio buttons)
    view_menu = menubar.addMenu("&Affichage")
    
    view_group = QActionGroup(self)
    
    list_view = QAction("Vue &Liste", self)
    list_view.setCheckable(True)
    list_view.setChecked(True)
    view_group.addAction(list_view)
    
    icon_view = QAction("Vue &Icônes", self)
    icon_view.setCheckable(True)
    view_group.addAction(icon_view)
    
    view_menu.addAction(list_view)
    view_menu.addAction(icon_view)
    
    view_group.triggered.connect(self.change_view_mode)

def toggle_word_wrap(self, checked):
    """Gestionnaire pour retour à la ligne"""
    mode = "activé" if checked else "désactivé"
    self.statusBar().showMessage(f"Retour à la ligne {mode}", 2000)

def change_view_mode(self, action):
    """Gestionnaire pour changement de vue"""
    self.statusBar().showMessage(f"Mode d'affichage : {action.text()}", 2000)
```

---

## 3. Barres d'outils (QToolBar)

### 3.1 Création d'une barre d'outils basique

```python
def setup_tool_bar(self):
    """Configure la barre d'outils"""
    toolbar = self.addToolBar("Principal")
    toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
    
    # Action Nouveau avec icône
    new_action = QAction("Nouveau", self)
    new_action.setIcon(QIcon("icons/new.png"))  # Remplacer par vraie icône
    new_action.triggered.connect(self.new_file)
    toolbar.addAction(new_action)
    
    # Action Ouvrir
    open_action = QAction("Ouvrir", self)
    open_action.setIcon(QIcon("icons/open.png"))
    open_action.triggered.connect(self.open_file)
    toolbar.addAction(open_action)
    
    # Séparateur dans la toolbar
    toolbar.addSeparator()
    
    # Action Sauvegarder
    save_action = QAction("Sauvegarder", self)
    save_action.setIcon(QIcon("icons/save.png"))
    save_action.triggered.connect(self.save_file)
    toolbar.addAction(save_action)

def save_file(self):
    """Gestionnaire pour sauvegarder"""
    self.statusBar().showMessage("Fichier sauvegardé", 2000)
```

### 3.2 Barres d'outils multiples et personnalisées

```python
def setup_multiple_toolbars(self):
    """Création de plusieurs barres d'outils"""
    # Barre d'outils principale
    main_toolbar = self.addToolBar("Principal")
    main_toolbar.addAction("Nouveau")
    main_toolbar.addAction("Ouvrir")
    main_toolbar.addAction("Sauvegarder")
    
    # Barre d'outils de formatage
    format_toolbar = self.addToolBar("Formatage")
    format_toolbar.addAction("Gras")
    format_toolbar.addAction("Italique")
    format_toolbar.addAction("Souligné")
    
    # Widget personnalisé dans la toolbar
    search_toolbar = self.addToolBar("Recherche")
    
    search_field = QLineEdit()
    search_field.setPlaceholderText("Rechercher...")
    search_field.setMaximumWidth(200)
    search_toolbar.addWidget(search_field)
    
    search_button = QPushButton("Rechercher")
    search_button.clicked.connect(lambda: self.search(search_field.text()))
    search_toolbar.addWidget(search_button)

def search(self, text):
    """Gestionnaire de recherche"""
    self.statusBar().showMessage(f"Recherche : {text}", 2000)
```

---

## 4. Barre de statut (QStatusBar)

### 4.1 Utilisation basique

```python
def setup_status_bar(self):
    """Configure la barre de statut"""
    status = self.statusBar()
    
    # Message permanent à gauche
    status.showMessage("Prêt")
    
    # Widgets permanents à droite
    self.create_status_widgets()

def create_status_widgets(self):
    """Crée des widgets pour la barre de statut"""
    status = self.statusBar()
    
    # Label pour position
    self.position_label = QLabel("Ligne: 1, Col: 1")
    status.addPermanentWidget(self.position_label)
    
    # Label pour mode
    self.mode_label = QLabel("Insertion")
    status.addPermanentWidget(self.mode_label)
    
    # Barre de progression
    self.progress_bar = QProgressBar()
    self.progress_bar.setVisible(False)
    self.progress_bar.setMaximumWidth(200)
    status.addPermanentWidget(self.progress_bar)

def update_status_position(self, line, column):
    """Met à jour la position dans la barre de statut"""
    self.position_label.setText(f"Ligne: {line}, Col: {column}")

def show_progress(self, value, maximum=100):
    """Affiche une barre de progression"""
    self.progress_bar.setMaximum(maximum)
    self.progress_bar.setValue(value)
    self.progress_bar.setVisible(value < maximum)
```

---

## 5. Menus contextuels

### 5.1 Menu contextuel basique

```python
from PyQt6.QtWidgets import QMenu

def setup_context_menu(self):
    """Configure les menus contextuels"""
    # Activer les menus contextuels
    self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
    self.customContextMenuRequested.connect(self.show_context_menu)

def show_context_menu(self, position):
    """Affiche le menu contextuel"""
    context_menu = QMenu(self)
    
    # Actions du menu contextuel
    copy_action = context_menu.addAction("Copier")
    copy_action.triggered.connect(self.copy_content)
    
    paste_action = context_menu.addAction("Coller")
    paste_action.triggered.connect(self.paste_content)
    
    context_menu.addSeparator()
    
    properties_action = context_menu.addAction("Propriétés...")
    properties_action.triggered.connect(self.show_properties)
    
    # Afficher le menu à la position du clic
    context_menu.exec(self.mapToGlobal(position))

def copy_content(self):
    """Gestionnaire copier"""
    self.statusBar().showMessage("Contenu copié", 2000)

def paste_content(self):
    """Gestionnaire coller"""
    self.statusBar().showMessage("Contenu collé", 2000)

def show_properties(self):
    """Affiche les propriétés"""
    self.statusBar().showMessage("Affichage des propriétés...", 2000)
```

### 5.2 Menus contextuels conditionnels

```python
def show_advanced_context_menu(self, position):
    """Menu contextuel avec logique conditionnelle"""
    context_menu = QMenu(self)
    
    # Vérifier s'il y a une sélection
    has_selection = self.has_text_selected()
    
    # Actions conditionnelles
    cut_action = context_menu.addAction("Couper")
    cut_action.setEnabled(has_selection)
    
    copy_action = context_menu.addAction("Copier")
    copy_action.setEnabled(has_selection)
    
    paste_action = context_menu.addAction("Coller")
    paste_action.setEnabled(self.can_paste())
    
    context_menu.addSeparator()
    
    # Sous-menu
    format_menu = context_menu.addMenu("Format")
    format_menu.addAction("Gras")
    format_menu.addAction("Italique")
    format_menu.addAction("Couleur...")
    
    context_menu.exec(self.mapToGlobal(position))

def has_text_selected(self):
    """Vérifie s'il y a du texte sélectionné"""
    # Logique selon votre widget
    return True  # Exemple

def can_paste(self):
    """Vérifie si le collage est possible"""
    # Vérifier le presse-papier
    return True  # Exemple
```

---

## 6. Intégration HTML et CSS dans Qt

### 6.1 Application de styles CSS

```python
def setup_styles(self):
    """Applique des styles CSS à l'application"""
    style_sheet = """
    QMainWindow {
        background-color: #f0f0f0;
    }
    
    QMenuBar {
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 4px;
    }
    
    QMenuBar::item {
        background-color: transparent;
        padding: 8px 12px;
        border-radius: 4px;
    }
    
    QMenuBar::item:selected {
        background-color: #34495e;
    }
    
    QToolBar {
        background-color: #ecf0f1;
        border: 1px solid #bdc3c7;
        padding: 2px;
    }
    
    QToolButton {
        border: none;
        padding: 8px;
        border-radius: 4px;
        min-width: 60px;
    }
    
    QToolButton:hover {
        background-color: #d5dbdb;
    }
    
    QToolButton:pressed {
        background-color: #bdc3c7;
    }
    
    QStatusBar {
        background-color: #34495e;
        color: white;
        border-top: 1px solid #2c3e50;
    }
    """
    
    self.setStyleSheet(style_sheet)
```

### 6.2 Styles dynamiques et thèmes

```python
def setup_themes(self):
    """Gestion des thèmes"""
    self.current_theme = "clair"
    
    # Action pour changer de thème
    theme_menu = self.menuBar().addMenu("&Thème")
    
    light_theme = QAction("Thème clair", self)
    light_theme.triggered.connect(lambda: self.apply_theme("clair"))
    theme_menu.addAction(light_theme)
    
    dark_theme = QAction("Thème sombre", self)
    dark_theme.triggered.connect(lambda: self.apply_theme("sombre"))
    theme_menu.addAction(dark_theme)

def apply_theme(self, theme_name):
    """Applique un thème spécifique"""
    if theme_name == "sombre":
        style = """
        QMainWindow {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        
        QMenuBar {
            background-color: #1a252f;
            color: #ecf0f1;
        }
        
        QMenuBar::item:selected {
            background-color: #34495e;
        }
        
        QToolBar {
            background-color: #34495e;
            border: 1px solid #2c3e50;
        }
        
        QLabel {
            color: #ecf0f1;
        }
        """
    else:  # thème clair
        style = """
        QMainWindow {
            background-color: #ecf0f1;
            color: #2c3e50;
        }
        
        QMenuBar {
            background-color: #3498db;
            color: white;
        }
        
        QToolBar {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
        }
        """
    
    self.setStyleSheet(style)
    self.current_theme = theme_name
    self.statusBar().showMessage(f"Thème {theme_name} appliqué", 2000)
```

### 6.3 Widgets avec contenu HTML

```python
from PyQt6.QtWidgets import QTextEdit

def setup_html_content(self):
    """Utilisation de contenu HTML dans les widgets"""
    # Widget central avec HTML
    html_widget = QTextEdit()
    html_content = """
    <h2 style="color: #3498db;">Bienvenue dans PyQt6</h2>
    <p>Cette application démontre l'intégration de <strong>HTML</strong> 
       et <em>CSS</em> dans Qt.</p>
    
    <ul>
        <li>Formatage riche du texte</li>
        <li>Images intégrées</li>
        <li>Liens hypertexte</li>
    </ul>
    
    <p style="background-color: #f39c12; padding: 10px; border-radius: 5px;">
        <strong>Note :</strong> Qt supporte un sous-ensemble de HTML 4.
    </p>
    """
    
    html_widget.setHtml(html_content)
    self.setCentralWidget(html_widget)

def create_rich_status_message(self, message, message_type="info"):
    """Crée des messages de statut formatés"""
    colors = {
        "info": "#3498db",
        "success": "#27ae60", 
        "warning": "#f39c12",
        "error": "#e74c3c"
    }
    
    color = colors.get(message_type, "#3498db")
    
    # Note: QStatusBar ne supporte pas HTML, mais on peut utiliser des QLabel
    status_label = QLabel(f'<span style="color: {color};">{message}</span>')
    self.statusBar().addWidget(status_label, 1)
    
    # Supprimer après 3 secondes
    QTimer.singleShot(3000, lambda: self.statusBar().removeWidget(status_label))
```

---

## 7. Interconnexion des éléments d'interface

### 7.1 Synchronisation entre menus et barres d'outils

```python
def create_synchronized_actions(self):
    """Crée des actions synchronisées entre menus et barres d'outils"""
    # Action partagée
    self.save_action = QAction("Sauvegarder", self)
    self.save_action.setShortcut("Ctrl+S")
    self.save_action.setIcon(QIcon("icons/save.png"))
    self.save_action.setStatusTip("Sauvegarder le document")
    self.save_action.triggered.connect(self.save_document)
    
    # Ajouter à la fois au menu et à la barre d'outils
    file_menu = self.menuBar().addMenu("Fichier")
    file_menu.addAction(self.save_action)
    
    toolbar = self.addToolBar("Principal")
    toolbar.addAction(self.save_action)
    
    # État initial
    self.save_action.setEnabled(False)  # Désactivé au début

def document_modified(self):
    """Appelé quand le document est modifié"""
    self.save_action.setEnabled(True)
    self.setWindowTitle("Mon Application* - Document modifié")

def save_document(self):
    """Sauvegarde le document"""
    # Logique de sauvegarde...
    self.save_action.setEnabled(False)
    self.setWindowTitle("Mon Application")
    self.statusBar().showMessage("Document sauvegardé", 2000)
```

### 7.2 Communication entre composants

```python
from PyQt6.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    # Signal personnalisé
    status_changed = pyqtSignal(str, str)  # message, type
    
    def __init__(self):
        super().__init__()
        # Connecter le signal au gestionnaire
        self.status_changed.connect(self.update_status_display)
        
        self.setup_ui()
    
    def setup_interconnected_components(self):
        """Configure les composants interconnectés"""
        # Menu Affichage
        view_menu = self.menuBar().addMenu("Affichage")
        
        # Actions pour les barres d'outils
        self.toolbar_action = QAction("Barre d'outils", self)
        self.toolbar_action.setCheckable(True)
        self.toolbar_action.setChecked(True)
        self.toolbar_action.toggled.connect(self.toggle_toolbar)
        view_menu.addAction(self.toolbar_action)
        
        self.statusbar_action = QAction("Barre de statut", self)
        self.statusbar_action.setCheckable(True)
        self.statusbar_action.setChecked(True)
        self.statusbar_action.toggled.connect(self.toggle_statusbar)
        view_menu.addAction(self.statusbar_action)
    
    def toggle_toolbar(self, visible):
        """Affiche/cache la barre d'outils"""
        toolbar = self.findChild(QToolBar)
        if toolbar:
            toolbar.setVisible(visible)
            status = "visible" if visible else "cachée"
            self.status_changed.emit(f"Barre d'outils {status}", "info")
    
    def toggle_statusbar(self, visible):
        """Affiche/cache la barre de statut"""
        self.statusBar().setVisible(visible)
        if visible:
            self.status_changed.emit("Barre de statut restaurée", "info")
    
    def update_status_display(self, message, msg_type):
        """Met à jour l'affichage du statut"""
        if self.statusBar().isVisible():
            self.statusBar().showMessage(message, 3000)
```

---

## 8. Travaux pratiques

### 🚧 TP1 - Application avec interface complète
**Durée** : 45 minutes
- Créer une application avec menus, barres d'outils et statut
- Implémenter les actions de base (Nouveau, Ouvrir, Sauvegarder)

### 🚧 TP2 - Personnalisation avec CSS
**Durée** : 30 minutes  
- Appliquer des styles CSS personnalisés
- Implémenter un système de thèmes (clair/sombre)

### 🚧 TP3 - Menus contextuels avancés
**Durée** : 20 minutes
- Créer des menus contextuels conditionnels
- Gérer différents contextes d'utilisation

### 🚧 TP4 - Synchronisation des composants
**Durée** : 25 minutes
- Interconnecter menus, barres d'outils et actions
- Implémenter des signaux personnalisés

---

## 9. Points clés à retenir

### ✅ Architecture d'application
- `QMainWindow` structure l'interface en zones logiques
- Le widget central est obligatoire
- Les barres (menus, outils, statut) sont optionnelles mais recommandées

### ✅ Bonnes pratiques d'interface
- Partager les `QAction` entre menus et barres d'outils
- Utiliser des raccourcis clavier cohérents
- Fournir des messages d'aide dans la barre de statut
- Gérer l'état des actions (activé/désactivé)

### ✅ Personnalisation visuelle
- CSS permet une personnalisation avancée de l'apparence
- Qt supporte un sous-ensemble de HTML 4 pour le contenu riche
- Les thèmes améliorent l'expérience utilisateur

### ✅ Interaction utilisateur
- Menus contextuels adaptés au contexte
- Barres d'outils pour l'accès rapide aux fonctions courantes
- Barre de statut pour le feedback en temps réel

---

## Prochaine étape

Dans le **Chapitre 3 - Gestion des stratégies de placement (Layout)**, nous découvrirons :
- Les différents types de layouts (horizontal, vertical, grille)
- L'organisation des widgets avec les gestionnaires de disposition
- Les layouts imbriqués et les techniques avancées
- L'adaptation automatique aux redimensionnements
