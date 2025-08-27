# Chapitre 6 : Utilisation du Qt Designer

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Maîtriser l'interface et les outils du Qt Designer
- Créer des interfaces graphiques complexes de manière visuelle
- Configurer les propriétés et signaux/slots dans Designer
- Promouvoir des widgets pour utiliser des composants personnalisés
- Intégrer Qt Designer avec VSCode et configurer l'environnement de développement
- Générer et intégrer le code Python à partir des fichiers .ui
- Appliquer les bonnes pratiques de conception d'interface avec Designer

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Présentation de Qt Designer

### 1.1 Interface et philosophie

Qt Designer est un outil WYSIWYG (What You See Is What You Get) pour créer des interfaces utilisateur :

```python
# Exemple typique d'intégration Designer → Python
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class DesignerDemo(QMainWindow):
    """Classe utilisant un fichier .ui créé avec Designer"""
    
    def __init__(self):
        super().__init__()
        # Chargement dynamique du fichier .ui
        uic.loadUi('interface.ui', self)
        
        # Connexion des signaux après chargement
        self.setup_connections()
    
    def setup_connections(self):
        """Configure les connexions non définies dans Designer"""
        # Les widgets sont automatiquement accessibles via leur objectName
        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.on_button_clicked)
        
        if hasattr(self, 'lineEdit'):
            self.lineEdit.textChanged.connect(self.on_text_changed)
    
    def on_button_clicked(self):
        """Gestionnaire de clic personnalisé"""
        print("Bouton cliqué depuis interface Designer")
    
    def on_text_changed(self, text):
        """Gestionnaire de changement de texte"""
        print(f"Texte modifié: {text}")

def main():
    app = QApplication(sys.argv)
    window = DesignerDemo()
    window.show()
    return app.exec()

# Alternative: génération de code Python
# pyuic6 interface.ui -o ui_interface.py
# puis import et héritage de la classe générée
```

### 1.2 Avantages du Designer par rapport au code

```python
# Comparaison: Interface en code pur vs Designer

# === APPROCHE CODE PUR ===
class ManualInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface manuelle")
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Groupe de contrôles
        controls_group = QGroupBox("Contrôles")
        controls_layout = QFormLayout()
        
        # Champs
        self.name_edit = QLineEdit()
        controls_layout.addRow("Nom:", self.name_edit)
        
        self.age_spin = QSpinBox()
        self.age_spin.setRange(0, 120)
        controls_layout.addRow("Âge:", self.age_spin)
        
        self.email_edit = QLineEdit()
        controls_layout.addRow("Email:", self.email_edit)
        
        controls_group.setLayout(controls_layout)
        main_layout.addWidget(controls_group)
        
        # Boutons
        buttons_layout = QHBoxLayout()
        
        self.save_button = QPushButton("Sauvegarder")
        self.cancel_button = QPushButton("Annuler")
        
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.cancel_button)
        
        main_layout.addLayout(buttons_layout)
        
        # 20+ lignes pour une interface simple !

# === APPROCHE DESIGNER ===
class DesignerInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1 ligne pour charger l'interface !
        uic.loadUi('form.ui', self)
        
        # Focus sur la logique métier
        self.setup_business_logic()
    
    def setup_business_logic(self):
        """Configuration de la logique métier"""
        # Validation en temps réel
        self.name_edit.textChanged.connect(self.validate_form)
        self.email_edit.textChanged.connect(self.validate_email)
        
        # Actions des boutons
        self.save_button.clicked.connect(self.save_data)
        self.cancel_button.clicked.connect(self.cancel_operation)
```

---

## 2. Prise en main de Qt Designer

### 2.1 Interface et zones de travail

Qt Designer se compose de plusieurs zones principales :

```
┌─────────────────────────────────────────────────────────────┐
│ Barre de menus et d'outils                                 │
├──────────────┬────────────────────────┬──────────────────────┤
│ Widget Box   │                        │ Property Editor      │
│              │                        │                      │
│ • Layouts    │    Zone de conception  │ • Properties         │
│ • Buttons    │       (Canvas)         │ • Signal/Slot        │
│ • Input      │                        │   Editor             │
│ • Display    │                        │                      │
│ • Containers │                        │                      │
│              │                        │                      │
├──────────────┼────────────────────────┼──────────────────────┤
│ Object       │                        │ Action Editor /      │
│ Inspector    │                        │ Resource Browser     │
│              │                        │                      │
│ • Structure  │                        │                      │
│   hiérarchique│                       │                      │
└──────────────┴────────────────────────┴──────────────────────┘
```

### 2.2 Création d'une première interface

Workflow typique de création :

```python
# Étapes de création d'interface dans Designer:

"""
1. NOUVEAU FICHIER
   File → New → Dialog / MainWindow / Widget
   
2. AJOUT DE WIDGETS
   • Glisser-déposer depuis Widget Box
   • Positionnement et redimensionnement
   
3. CONFIGURATION DES LAYOUTS
   • Sélection des widgets
   • Application du layout (toolbar ou menu)
   
4. PROPRIÉTÉS
   • Modification via Property Editor
   • objectName, text, geometry, etc.
   
5. SIGNAUX/SLOTS
   • Connexions via Signal/Slot Editor
   • Ou mode Edit Signal/Slots
   
6. SAUVEGARDE
   • Format .ui (XML)
   • Compilation vers .py si nécessaire
"""

# Exemple de fichier .ui généré (simplifié):
ui_example = """
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Mon Application</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>180</y>
      <width>100</width>
      <height>40</height>
     </rect>
    </property>
    <property name="text">
     <string>Cliquez-moi</string>
    </property>
   </widget>
  </widget>
 </widget>
</ui>
"""
```

### 2.3 Widgets essentiels et leur utilisation

```python
class WidgetCatalog:
    """Catalogue des widgets Designer les plus utilisés"""
    
    @staticmethod
    def input_widgets():
        """Widgets d'entrée de données"""
        return {
            'QLineEdit': {
                'usage': 'Saisie de texte sur une ligne',
                'propriétés_clés': ['text', 'placeholderText', 'maxLength', 'readOnly'],
                'signaux_utiles': ['textChanged', 'editingFinished', 'returnPressed']
            },
            'QTextEdit': {
                'usage': 'Saisie de texte multiligne',
                'propriétés_clés': ['html', 'plainText', 'readOnly'],
                'signaux_utiles': ['textChanged']
            },
            'QSpinBox': {
                'usage': 'Saisie de nombres entiers',
                'propriétés_clés': ['minimum', 'maximum', 'value', 'suffix'],
                'signaux_utiles': ['valueChanged']
            },
            'QComboBox': {
                'usage': 'Liste déroulante de choix',
                'propriétés_clés': ['items', 'currentText', 'editable'],
                'signaux_utiles': ['currentTextChanged', 'activated']
            }
        }
    
    @staticmethod
    def display_widgets():
        """Widgets d'affichage"""
        return {
            'QLabel': {
                'usage': 'Affichage de texte ou image',
                'propriétés_clés': ['text', 'alignment', 'wordWrap', 'pixmap'],
                'signaux_utiles': ['linkActivated']
            },
            'QProgressBar': {
                'usage': 'Barre de progression',
                'propriétés_clés': ['minimum', 'maximum', 'value', 'format'],
                'signaux_utiles': ['valueChanged']
            },
            'QLCDNumber': {
                'usage': 'Affichage numérique LCD',
                'propriétés_clés': ['digitCount', 'value', 'mode'],
                'signaux_utiles': []
            }
        }
    
    @staticmethod
    def container_widgets():
        """Widgets conteneurs"""
        return {
            'QGroupBox': {
                'usage': 'Groupement visuel avec titre',
                'propriétés_clés': ['title', 'checkable', 'checked'],
                'signaux_utiles': ['toggled']
            },
            'QTabWidget': {
                'usage': 'Interface à onglets',
                'propriétés_clés': ['currentIndex', 'tabPosition'],
                'signaux_utiles': ['currentChanged']
            },
            'QScrollArea': {
                'usage': 'Zone défilante pour contenu large',
                'propriétés_clés': ['widget', 'widgetResizable'],
                'signaux_utiles': []
            }
        }

# Exemple d'utilisation programmatique après Designer
class FormProcessor:
    """Classe pour traiter les données d'un formulaire Designer"""
    
    def __init__(self, ui_file):
        self.ui_file = ui_file
        self.widgets_data = {}
    
    def load_and_process(self):
        """Charge l'interface et configure le traitement"""
        # Simulation du chargement
        self.setup_validation()
        self.setup_data_binding()
    
    def setup_validation(self):
        """Configure la validation des champs"""
        validation_rules = {
            'email_edit': self.validate_email,
            'age_spin': self.validate_age,
            'name_edit': self.validate_name
        }
        
        for widget_name, validator in validation_rules.items():
            print(f"Validation configurée pour {widget_name}")
    
    def validate_email(self, email):
        """Validation d'email"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_age(self, age):
        """Validation d'âge"""
        return 0 <= age <= 120
    
    def validate_name(self, name):
        """Validation de nom"""
        return len(name.strip()) >= 2
```

---

## 3. Configuration des propriétés et signaux/slots

### 3.1 Éditeur de propriétés avancé

```python
class PropertyConfiguration:
    """Guide de configuration des propriétés dans Designer"""
    
    @staticmethod
    def common_properties():
        """Propriétés communes à tous les widgets"""
        return {
            'Géométrie': {
                'geometry': 'Position et taille (x, y, width, height)',
                'sizePolicy': 'Politique de redimensionnement',
                'minimumSize': 'Taille minimale',
                'maximumSize': 'Taille maximale'
            },
            'Apparence': {
                'font': 'Police de caractères',
                'styleSheet': 'Styles CSS personnalisés',
                'palette': 'Couleurs du widget',
                'cursor': 'Curseur de souris'
            },
            'Comportement': {
                'enabled': 'Widget activé/désactivé',
                'visible': 'Visibilité du widget',
                'toolTip': 'Bulle d\'aide au survol',
                'whatsThis': 'Aide contextuelle'
            }
        }
    
    @staticmethod
    def button_properties():
        """Propriétés spécifiques aux boutons"""
        return {
            'text': 'Texte affiché sur le bouton',
            'icon': 'Icône du bouton',
            'iconSize': 'Taille de l\'icône',
            'checkable': 'Bouton à bascule (on/off)',
            'checked': 'État initial si checkable',
            'autoDefault': 'Bouton par défaut automatique',
            'default': 'Bouton par défaut (Entrée)'
        }
    
    @staticmethod
    def layout_properties():
        """Propriétés des layouts"""
        return {
            'spacing': 'Espacement entre widgets',
            'margin': 'Marge autour du layout (déprécié)',
            'leftMargin': 'Marge gauche',
            'topMargin': 'Marge haute',
            'rightMargin': 'Marge droite',
            'bottomMargin': 'Marge basse',
            'stretch': 'Facteur d\'étirement des éléments'
        }

# Exemple d'interface avec propriétés configurées
class ConfiguredInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('configured_form.ui', self)
        self.verify_properties()
    
    def verify_properties(self):
        """Vérifie les propriétés configurées dans Designer"""
        # Vérification des propriétés après chargement
        if hasattr(self, 'submitButton'):
            print(f"Bouton submit - Texte: {self.submitButton.text()}")
            print(f"Bouton submit - Activé: {self.submitButton.isEnabled()}")
            print(f"Bouton submit - Tooltip: {self.submitButton.toolTip()}")
        
        # Modification programmatique si nécessaire
        if hasattr(self, 'statusLabel'):
            self.statusLabel.setStyleSheet("""
                QLabel {
                    color: green;
                    font-weight: bold;
                    background-color: #f0f8f0;
                    padding: 5px;
                    border: 1px solid #c0d0c0;
                    border-radius: 3px;
                }
            """)
```

### 3.2 Signaux et slots dans Designer

```python
class SignalSlotConfiguration:
    """Configuration des signaux/slots dans Designer"""
    
    def __init__(self):
        self.connections_info = self.get_designer_connections()
    
    def get_designer_connections(self):
        """Connexions typiques configurables dans Designer"""
        return {
            'Bouton vers QApplication': {
                'signal': 'QPushButton.clicked()',
                'slot': 'QApplication.quit()',
                'description': 'Fermer l\'application'
            },
            'QLineEdit vers QLabel': {
                'signal': 'QLineEdit.textChanged(QString)',
                'slot': 'QLabel.setText(QString)',
                'description': 'Copie de texte en temps réel'
            },
            'QSlider vers QSpinBox': {
                'signal': 'QSlider.valueChanged(int)',
                'slot': 'QSpinBox.setValue(int)',
                'description': 'Synchronisation de valeurs'
            },
            'QCheckBox vers QWidget': {
                'signal': 'QCheckBox.toggled(bool)',
                'slot': 'QWidget.setEnabled(bool)',
                'description': 'Activation conditionnelle'
            }
        }
    
    def create_manual_connections_example(self):
        """Exemple de connexions non supportées par Designer"""
        return """
        # Connexions avancées à faire en Python:
        
        # 1. Connexions avec lambda
        self.calculateButton.clicked.connect(
            lambda: self.result_label.setText(str(self.value1.value() + self.value2.value()))
        )
        
        # 2. Connexions conditionnelles
        def conditional_slot():
            if self.enable_checkbox.isChecked():
                self.process_data()
        
        self.trigger_button.clicked.connect(conditional_slot)
        
        # 3. Signaux personnalisés
        self.data_processor.finished.connect(self.on_processing_finished)
        
        # 4. Connexions avec paramètres personnalisés
        from functools import partial
        for i, button in enumerate(self.number_buttons):
            button.clicked.connect(partial(self.number_clicked, i))
        """

# Exemple pratique: Formulaire avec signaux/slots Designer + Python
class MixedConnectionsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mixed_connections.ui', self)
        
        # Connexions définies dans Designer:
        # - clearButton.clicked() → nameEdit.clear()
        # - clearButton.clicked() → emailEdit.clear()
        # - enableCheckBox.toggled(bool) → formGroupBox.setEnabled(bool)
        
        # Connexions avancées en Python
        self.setup_advanced_connections()
    
    def setup_advanced_connections(self):
        """Connexions complexes non supportées par Designer"""
        # Validation en temps réel
        self.nameEdit.textChanged.connect(self.validate_name)
        self.emailEdit.textChanged.connect(self.validate_email)
        
        # Soumission avec validation complète
        self.submitButton.clicked.connect(self.submit_form)
        
        # Mise à jour dynamique du statut
        self.update_status_timer = QTimer()
        self.update_status_timer.timeout.connect(self.update_form_status)
        self.update_status_timer.start(1000)  # Chaque seconde
    
    def validate_name(self, name):
        """Validation du nom"""
        is_valid = len(name.strip()) >= 2
        self.nameEdit.setStyleSheet("" if is_valid else "border: 2px solid red;")
        return is_valid
    
    def validate_email(self, email):
        """Validation de l'email"""
        import re
        is_valid = re.match(r'^[^@]+@[^@]+\.[^@]+$', email) is not None
        self.emailEdit.setStyleSheet("" if is_valid else "border: 2px solid red;")
        return is_valid
    
    def submit_form(self):
        """Soumission du formulaire avec validation"""
        name_valid = self.validate_name(self.nameEdit.text())
        email_valid = self.validate_email(self.emailEdit.text())
        
        if name_valid and email_valid:
            QMessageBox.information(self, "Succès", "Formulaire soumis avec succès!")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez corriger les erreurs.")
    
    def update_form_status(self):
        """Met à jour le statut du formulaire"""
        name_ok = len(self.nameEdit.text().strip()) >= 2
        email_ok = '@' in self.emailEdit.text()
        
        if name_ok and email_ok:
            self.statusLabel.setText("✅ Formulaire valide")
            self.statusLabel.setStyleSheet("color: green;")
            self.submitButton.setEnabled(True)
        else:
            self.statusLabel.setText("⚠️ Formulaire incomplet")
            self.statusLabel.setStyleSheet("color: orange;")
            self.submitButton.setEnabled(False)
```

---

## 4. Promotion de widgets et composants personnalisés

### 4.1 Concept de promotion de widgets

La promotion permet d'utiliser des widgets personnalisés dans Designer :

```python
# 1. D'abord, créer le widget personnalisé
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import pyqtSignal

class SearchWidget(QWidget):
    """Widget de recherche personnalisé"""
    
    # Signal émis lors d'une recherche
    search_requested = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Configure l'interface du widget"""
        layout = QVBoxLayout()
        
        # Champ de recherche
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Tapez votre recherche...")
        self.search_input.returnPressed.connect(self.perform_search)
        layout.addWidget(self.search_input)
        
        # Bouton de recherche
        self.search_button = QPushButton("Rechercher")
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)
        
        # Label de résultats
        self.results_label = QLabel("Aucune recherche effectuée")
        self.results_label.setStyleSheet("color: gray; font-style: italic;")
        layout.addWidget(self.results_label)
        
        self.setLayout(layout)
    
    def perform_search(self):
        """Effectue la recherche"""
        query = self.search_input.text().strip()
        if query:
            self.search_requested.emit(query)
            self.results_label.setText(f"Recherche: '{query}'")
        else:
            self.results_label.setText("Veuillez saisir un terme de recherche")
    
    def clear_search(self):
        """Efface la recherche"""
        self.search_input.clear()
        self.results_label.setText("Recherche effacée")

class ColoredLabel(QLabel):
    """Label avec couleur automatique selon le contenu"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color_rules = {
            'erreur': '#ff4444',
            'succès': '#44ff44', 
            'warning': '#ffaa44',
            'info': '#4444ff'
        }
    
    def setText(self, text):
        """Surcharge pour appliquer la couleur automatique"""
        super().setText(text)
        self.apply_auto_color(text)
    
    def apply_auto_color(self, text):
        """Applique la couleur selon le texte"""
        text_lower = text.lower()
        
        for keyword, color in self.color_rules.items():
            if keyword in text_lower:
                self.setStyleSheet(f"color: {color}; font-weight: bold;")
                return
        
        # Couleur par défaut
        self.setStyleSheet("color: black;")

class NumberInput(QSpinBox):
    """SpinBox avec validation et formatage avancés"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_advanced_features()
    
    def setup_advanced_features(self):
        """Configure les fonctionnalités avancées"""
        self.setRange(-999999, 999999)
        self.valueChanged.connect(self.on_value_changed)
        
        # Formatage avec séparateurs de milliers
        self.setGroupSeparatorShown(True)
    
    def on_value_changed(self, value):
        """Réaction au changement de valeur"""
        # Changer la couleur selon la valeur
        if value < 0:
            color = "red"
        elif value > 1000:
            color = "green"
        else:
            color = "black"
        
        self.setStyleSheet(f"color: {color}; font-weight: bold;")
```

### 4.2 Processus de promotion dans Designer

```python
class PromotionGuide:
    """Guide complet pour la promotion de widgets"""
    
    @staticmethod
    def promotion_steps():
        """Étapes pour promouvoir un widget dans Designer"""
        return [
            "1. Placer un widget de base (ex: QWidget) dans Designer",
            "2. Clic droit → 'Promote to...'",
            "3. Remplir le formulaire de promotion:",
            "   - Class name: Nom de votre classe (ex: SearchWidget)",
            "   - Header file: Nom du module Python (ex: custom_widgets)",
            "4. Cocher 'Global include' si utilisé partout",
            "5. Cliquer 'Add' puis 'Promote'",
            "6. Le widget apparaît avec le nouveau type dans l'Object Inspector"
        ]
    
    @staticmethod
    def promotion_best_practices():
        """Bonnes pratiques pour la promotion"""
        return {
            'Nommage': [
                "Utiliser des noms de classe explicites",
                "Préfixer les widgets personnalisés (ex: Custom*, My*)",
                "Respecter la convention PascalCase"
            ],
            'Organisation': [
                "Regrouper les widgets dans des modules thématiques",
                "Créer un module custom_widgets.py dédié",
                "Documenter les propriétés et signaux personnalisés"
            ],
            'Compatibilité': [
                "Hériter des classes Qt appropriées",
                "Implémenter les méthodes sizeHint() si nécessaire",
                "Gérer correctement les signaux personnalisés"
            ]
        }

# Exemple d'utilisation des widgets promus
class PromotedWidgetsDemo(QMainWindow):
    """Démonstration des widgets promus"""
    
    def __init__(self):
        super().__init__()
        # Charger l'interface avec widgets promus
        uic.loadUi('promoted_widgets.ui', self)
        
        # Les widgets promus sont automatiquement créés
        self.setup_promoted_widgets()
    
    def setup_promoted_widgets(self):
        """Configure les widgets promus après chargement"""
        # SearchWidget promu
        if hasattr(self, 'searchWidget'):
            self.searchWidget.search_requested.connect(self.handle_search)
        
        # ColoredLabel promu  
        if hasattr(self, 'statusLabel'):
            self.statusLabel.setText("Application prête")
        
        # NumberInput promu
        if hasattr(self, 'amountInput'):
            self.amountInput.valueChanged.connect(self.calculate_total)
    
    def handle_search(self, query):
        """Gestionnaire de recherche"""
        print(f"Recherche demandée: {query}")
        # Simulation de recherche
        results = [f"Résultat {i} pour '{query}'" for i in range(1, 4)]
        self.display_results(results)
    
    def display_results(self, results):
        """Affiche les résultats de recherche"""
        if hasattr(self, 'resultsTextEdit'):
            self.resultsTextEdit.clear()
            for result in results:
                self.resultsTextEdit.append(result)
    
    def calculate_total(self, amount):
        """Calcule un total avec TVA"""
        tva = amount * 0.20
        total = amount + tva
        
        if hasattr(self, 'totalLabel'):
            self.totalLabel.setText(f"Total TTC: {total:.2f} €")
```

---

## 5. Intégration avec VSCode

### 5.1 Configuration de l'environnement

```python
# Configuration VSCode pour Qt Designer

# 1. EXTENSIONS RECOMMANDÉES pour VSCode:
vscode_extensions = {
    "Qt for Python": "Officielle Microsoft pour PyQt/PySide",
    "Qt Creator Syntax": "Coloration syntaxique pour fichiers .ui",
    "XML Tools": "Formatage et validation XML pour fichiers .ui"
}

# 2. CONFIGURATION tasks.json pour automatiser les tâches
vscode_tasks = """{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Open Qt Designer",
            "type": "shell",
            "command": "designer",
            "group": "build",
            "detail": "Ouvre Qt Designer"
        },
        {
            "label": "Compile UI to Python",
            "type": "shell", 
            "command": "pyuic6",
            "args": [
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}.py"
            ],
            "group": "build",
            "detail": "Compile un fichier .ui vers Python"
        },
        {
            "label": "Compile all UI files",
            "type": "shell",
            "command": "find",
            "args": [
                ".",
                "-name", "*.ui",
                "-exec", "pyuic6", "{}", "-o", "{}.py", ";"
            ],
            "group": "build",
            "detail": "Compile tous les fichiers .ui du projet"
        }
    ]
}"""

# 3. CONFIGURATION launch.json pour déboguer
vscode_launch = """{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug PyQt App",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "QT_QPA_PLATFORM_PLUGIN_PATH": ""
            },
            "args": []
        }
    ]
}"""

class VSCodeIntegration:
    """Classe pour l'intégration VSCode/Qt Designer"""
    
    def __init__(self, project_path):
        self.project_path = project_path
        self.ui_files = []
        self.py_files = []
    
    def scan_ui_files(self):
        """Recherche tous les fichiers .ui du projet"""
        import os
        import glob
        
        pattern = os.path.join(self.project_path, "**/*.ui")
        self.ui_files = glob.glob(pattern, recursive=True)
        return self.ui_files
    
    def auto_compile_ui(self):
        """Compilation automatique des fichiers .ui"""
        import subprocess
        import os
        
        for ui_file in self.ui_files:
            # Générer le nom du fichier Python
            py_file = ui_file.replace('.ui', '_ui.py')
            
            # Vérifier si la compilation est nécessaire
            if (not os.path.exists(py_file) or 
                os.path.getmtime(ui_file) > os.path.getmtime(py_file)):
                
                try:
                    # Exécuter pyuic6
                    result = subprocess.run([
                        'pyuic6', ui_file, '-o', py_file
                    ], capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print(f"✅ Compilé: {ui_file} → {py_file}")
                    else:
                        print(f"❌ Erreur compilation {ui_file}: {result.stderr}")
                        
                except FileNotFoundError:
                    print("❌ pyuic6 non trouvé. Installer PyQt6-tools.")
    
    def create_integration_script(self):
        """Crée un script d'intégration pour le projet"""
        script_content = '''#!/usr/bin/env python3
"""
Script d'intégration Qt Designer pour VSCode
Usage: python ui_integration.py [--watch] [--compile-all]
"""

import argparse
import os
import subprocess
import time
from pathlib import Path

class QtIntegration:
    def __init__(self):
        self.project_root = Path(__file__).parent
        
    def compile_ui_file(self, ui_file):
        """Compile un fichier .ui vers Python"""
        py_file = ui_file.with_suffix('.py')
        py_file = py_file.with_name(f"ui_{py_file.name}")
        
        cmd = ['pyuic6', str(ui_file), '-o', str(py_file)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Compilé: {ui_file.name}")
            return True
        else:
            print(f"❌ Erreur: {result.stderr}")
            return False
    
    def compile_all(self):
        """Compile tous les fichiers .ui"""
        ui_files = list(self.project_root.rglob("*.ui"))
        
        if not ui_files:
            print("Aucun fichier .ui trouvé")
            return
        
        success_count = 0
        for ui_file in ui_files:
            if self.compile_ui_file(ui_file):
                success_count += 1
        
        print(f"Compilation terminée: {success_count}/{len(ui_files)} fichiers")
    
    def watch_files(self):
        """Surveille les modifications et compile automatiquement"""
        print("👀 Surveillance des fichiers .ui (Ctrl+C pour arrêter)")
        
        ui_files = {f: f.stat().st_mtime for f in self.project_root.rglob("*.ui")}
        
        try:
            while True:
                time.sleep(1)
                
                # Vérifier les modifications
                current_files = {f: f.stat().st_mtime for f in self.project_root.rglob("*.ui")}
                
                for ui_file, mtime in current_files.items():
                    if ui_file not in ui_files or ui_files[ui_file] != mtime:
                        print(f"📝 Modification détectée: {ui_file.name}")
                        self.compile_ui_file(ui_file)
                        ui_files[ui_file] = mtime
                
                # Détecter les nouveaux fichiers
                for ui_file in current_files:
                    if ui_file not in ui_files:
                        print(f"🆕 Nouveau fichier: {ui_file.name}")
                        self.compile_ui_file(ui_file)
                
                ui_files = current_files
                
        except KeyboardInterrupt:
            print("\\n👋 Surveillance arrêtée")

def main():
    parser = argparse.ArgumentParser(description="Intégration Qt Designer")
    parser.add_argument('--watch', action='store_true', help='Surveiller les modifications')
    parser.add_argument('--compile-all', action='store_true', help='Compiler tous les fichiers')
    
    args = parser.parse_args()
    integration = QtIntegration()
    
    if args.compile_all:
        integration.compile_all()
    elif args.watch:
        integration.watch_files()
    else:
        print("Utilisation: python ui_integration.py --help")

if __name__ == "__main__":
    main()
'''
        
        script_path = os.path.join(self.project_path, 'ui_integration.py')
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        # Rendre exécutable sur Unix
        import stat
        os.chmod(script_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
        
        print(f"✅ Script d'intégration créé: {script_path}")
```

---

## 6. Génération et intégration du code Python

### 6.1 Compilation pyuic6 vs chargement dynamique

```python
# MÉTHODE 1: Compilation avec pyuic6
# Commande: pyuic6 form.ui -o ui_form.py

# Fichier généré ui_form.py:
class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 280, 100, 30))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mon Application"))
        self.pushButton.setText(_translate("MainWindow", "Cliquer"))

# Utilisation de la classe générée:
class CompiledFormDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connexions des signaux
        self.ui.pushButton.clicked.connect(self.button_clicked)
    
    def button_clicked(self):
        print("Bouton cliqué via interface compilée")

# MÉTHODE 2: Chargement dynamique avec uic.loadUi()
class DynamicFormDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        
        # Les widgets sont directement accessibles
        self.pushButton.clicked.connect(self.button_clicked)
    
    def button_clicked(self):
        print("Bouton cliqué via chargement dynamique")

# COMPARAISON DES MÉTHODES:
comparison = {
    'Compilation (pyuic6)': {
        'Avantages': [
            'Performance légèrement meilleure',
            'Autocomplétion IDE complète',
            'Vérification d\'erreurs au développement',
            'Pas de dépendance au fichier .ui en production'
        ],
        'Inconvénients': [
            'Étape de compilation nécessaire',
            'Fichiers supplémentaires à gérer',
            'Perte des modifications manuelles si recompilation'
        ]
    },
    'Chargement dynamique (uic.loadUi)': {
        'Avantages': [
            'Simplicité d\'utilisation',
            'Modifications d\'interface instantanées',
            'Pas de fichiers intermédiaires',
            'Prototypage rapide'
        ],
        'Inconvénients': [
            'Dépendance au fichier .ui',
            'Pas d\'autocomplétion pour les widgets',
            'Vérification d\'erreurs seulement à l\'exécution'
        ]
    }
}
```

### 6.2 Bonnes pratiques d'intégration

```python
class IntegrationBestPractices:
    """Bonnes pratiques pour l'intégration Designer → Python"""
    
    @staticmethod
    def hybrid_approach_example():
        """Approche hybride recommandée"""
        return '''
        # Structure de projet recommandée:
        project/
        ├── ui/                    # Fichiers Designer
        │   ├── main_window.ui
        │   ├── dialog.ui
        │   └── settings.ui
        ├── generated/             # Code généré
        │   ├── __init__.py
        │   ├── ui_main_window.py
        │   ├── ui_dialog.py
        │   └── ui_settings.py
        ├── src/                   # Code métier
        │   ├── main_window.py
        │   ├── dialog.py
        │   └── settings.py
        └── main.py
        '''
    
    @staticmethod
    def create_base_form_class():
        """Classe de base pour formulaires Designer"""
        return '''
class BaseDesignerForm(QMainWindow):
    """Classe de base pour les formulaires Designer"""
    
    def __init__(self, ui_file=None, parent=None):
        super().__init__(parent)
        
        if ui_file:
            self.load_ui(ui_file)
        
        self.setup_connections()
        self.setup_validation()
        self.post_init()
    
    def load_ui(self, ui_file):
        """Charge l'interface Designer"""
        try:
            uic.loadUi(ui_file, self)
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Erreur de chargement", 
                f"Impossible de charger {ui_file}:\\n{e}"
            )
            raise
    
    def setup_connections(self):
        """À surcharger pour les connexions personnalisées"""
        pass
    
    def setup_validation(self):
        """À surcharger pour la validation des champs"""
        pass
    
    def post_init(self):
        """À surcharger pour la configuration finale"""
        pass
    
    def find_widgets_by_type(self, widget_type):
        """Trouve tous les widgets d'un type donné"""
        return self.findChildren(widget_type)
    
    def auto_connect_buttons(self):
        """Connecte automatiquement les boutons selon leur nom"""
        buttons = self.find_widgets_by_type(QPushButton)
        
        for button in buttons:
            name = button.objectName()
            
            # Convention: okButton → on_ok_clicked
            if name.endswith('Button'):
                action = name[:-6].lower()  # Enlever 'Button'
                method_name = f'on_{action}_clicked'
                
                if hasattr(self, method_name):
                    button.clicked.connect(getattr(self, method_name))
                    print(f"Auto-connecté: {name} → {method_name}")
        '''

class AdvancedFormExample(QMainWindow):
    """Exemple d'utilisation avancée avec Designer"""
    
    def __init__(self):
        super().__init__()
        uic.loadUi('advanced_form.ui', self)
        
        self.init_form()
        self.setup_advanced_features()
    
    def init_form(self):
        """Initialisation de base du formulaire"""
        # Configuration des validateurs
        self.setup_validators()
        
        # Connexions des signaux
        self.setup_signal_connections()
        
        # État initial
        self.reset_form()
    
    def setup_validators(self):
        """Configure les validateurs de champs"""
        from PyQt6.QtGui import QRegularExpressionValidator
        from PyQt6.QtCore import QRegularExpression
        
        # Validateur email
        if hasattr(self, 'emailLineEdit'):
            email_regex = QRegularExpression(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            email_validator = QRegularExpressionValidator(email_regex)
            self.emailLineEdit.setValidator(email_validator)
        
        # Validateur téléphone
        if hasattr(self, 'phoneLineEdit'):
            phone_regex = QRegularExpression(r'^(?:\+33|0)[1-9](?:[0-9]{8})$')
            phone_validator = QRegularExpressionValidator(phone_regex)
            self.phoneLineEdit.setValidator(phone_validator)
    
    def setup_signal_connections(self):
        """Configure les connexions de signaux"""
        # Validation en temps réel
        for widget_name in ['nameLineEdit', 'emailLineEdit', 'phoneLineEdit']:
            if hasattr(self, widget_name):
                widget = getattr(self, widget_name)
                widget.textChanged.connect(self.validate_form)
        
        # Boutons d'action
        if hasattr(self, 'saveButton'):
            self.saveButton.clicked.connect(self.save_data)
        
        if hasattr(self, 'cancelButton'):
            self.cancelButton.clicked.connect(self.cancel_operation)
        
        if hasattr(self, 'resetButton'):
            self.resetButton.clicked.connect(self.reset_form)
    
    def setup_advanced_features(self):
        """Configure les fonctionnalités avancées"""
        # Raccourcis clavier
        if hasattr(self, 'saveButton'):
            self.saveButton.setShortcut('Ctrl+S')
        
        # Auto-sauvegarde
        self.autosave_timer = QTimer()
        self.autosave_timer.timeout.connect(self.autosave)
        self.autosave_timer.start(30000)  # 30 secondes
        
        # Indicateur de modifications
        self.is_modified = False
        self.update_window_title()
    
    def validate_form(self):
        """Valide l'ensemble du formulaire"""
        is_valid = True
        
        # Vérification des champs obligatoires
        required_fields = ['nameLineEdit', 'emailLineEdit']
        
        for field_name in required_fields:
            if hasattr(self, field_name):
                field = getattr(self, field_name)
                if not field.text().strip():
                    is_valid = False
                    field.setStyleSheet("border: 2px solid red;")
                else:
                    field.setStyleSheet("")
        
        # Mise à jour du bouton de sauvegarde
        if hasattr(self, 'saveButton'):
            self.saveButton.setEnabled(is_valid)
        
        return is_valid
    
    def save_data(self):
        """Sauvegarde les données"""
        if self.validate_form():
            # Logique de sauvegarde
            print("Données sauvegardées")
            self.is_modified = False
            self.update_window_title()
            
            QMessageBox.information(self, "Succès", "Données sauvegardées avec succès!")
    
    def cancel_operation(self):
        """Annule l'opération en cours"""
        if self.is_modified:
            reply = QMessageBox.question(
                self, 
                "Confirmation",
                "Des modifications non sauvegardées seront perdues. Continuer ?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.close()
        else:
            self.close()
    
    def reset_form(self):
        """Remet le formulaire à zéro"""
        # Effacer tous les champs de saisie
        line_edits = self.findChildren(QLineEdit)
        for edit in line_edits:
            edit.clear()
            edit.setStyleSheet("")
        
        # Réinitialiser les cases à cocher
        checkboxes = self.findChildren(QCheckBox)
        for checkbox in checkboxes:
            checkbox.setChecked(False)
        
        self.is_modified = False
        self.update_window_title()
    
    def autosave(self):
        """Sauvegarde automatique"""
        if self.is_modified and self.validate_form():
            print("Sauvegarde automatique...")
            # Logique de sauvegarde automatique
    
    def update_window_title(self):
        """Met à jour le titre de la fenêtre"""
        title = "Formulaire Avancé"
        if self.is_modified:
            title += " *"
        self.setWindowTitle(title)
    
    def closeEvent(self, event):
        """Gestion de la fermeture de la fenêtre"""
        if self.is_modified:
            reply = QMessageBox.question(
                self,
                "Fermeture",
                "Sauvegarder avant de fermer ?",
                QMessageBox.StandardButton.Save | 
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            
            if reply == QMessageBox.StandardButton.Save:
                self.save_data()
                event.accept()
            elif reply == QMessageBox.StandardButton.Discard:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
```

---

## 7. Travaux pratiques

### 🚧 TP1 - Interface de base avec Designer
**Durée** : 30 minutes
- Créer une interface de gestion de contacts avec Designer
- Configurer les propriétés et layouts appropriés

### 🚧 TP2 - Signaux/slots et validation
**Durée** : 30 minutes  
- Implémenter la validation de formulaire avec signaux/slots
- Mixer connexions Designer et programmation Python

### 🚧 TP3 - Widgets personnalisés et promotion
**Durée** : 30 minutes
- Développer des widgets personnalisés réutilisables
- Intégrer via promotion dans Designer

### 🚧 TP4 - Intégration VSCode complète
**Durée** : 30 minutes
- Configurer l'environnement VSCode pour Qt Designer
- Créer un workflow de développement automatisé

---

## 8. Points clés à retenir

### ✅ Designer vs Code
- **Designer** excelle pour la conception visuelle et le prototypage rapide
- **Code Python** reste nécessaire pour la logique métier et les interactions complexes
- **Approche hybride** combine les avantages des deux méthodes

### ✅ Workflow de développement
- Conception visuelle dans Designer pour la structure de base
- Configuration des propriétés essentielles dans l'éditeur
- Implémentation de la logique métier en Python
- Tests et itérations rapides

### ✅ Intégration professionnelle
- Compilation automatique des fichiers .ui avec scripts
- Versioning des fichiers .ui avec Git
- Séparation claire entre interface et logique métier
- Documentation des widgets personnalisés

### ✅ Bonnes pratiques
- Nommage cohérent des widgets (objectName)
- Organisation des fichiers .ui par fonctionnalité
- Validation côté client avec retours visuels
- Gestion des erreurs de chargement d'interface

---

## Prochaine étape

Dans le **Chapitre 7 - Aspects avancés**, nous découvrirons :
- L'architecture MDI (Multiple Document Interface) avec QMdiArea
- Les fonctions de tracé avancées avec QPainter
- La gestion des threads et du réseau avec Qt
- L'internationalisation des applications PyQt6
