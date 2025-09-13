# Chapitre 3 : Gestion des stratégies de placement (Layout)

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Utiliser les composants d'interface de base (QLineEdit, QComboBox, QSpinBox, etc.)
- Organiser les widgets avec les layouts horizontaux, verticaux et en grille
- Maîtriser les layouts imbriqués et les techniques avancées
- Gérer les politiques de taille et l'espacement des widgets
- Créer des interfaces adaptatives qui s'ajustent automatiquement
- Appliquer les bonnes pratiques d'organisation d'interface

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Introduction aux layouts et widgets d'interface

### 1.1 Pourquoi utiliser des layouts ?

Les layouts (gestionnaires de disposition) sont essentiels pour créer des interfaces utilisateur professionnelles et adaptatives :

```python
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class BadExample(QMainWindow):
    """Exemple de ce qu'il ne faut PAS faire"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Sans Layout - Problématique')
        self.setGeometry(100, 100, 400, 300)

        # Positionnement absolu (à éviter !)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Widgets positionnés manuellement
        label = QLabel('Nom:', central_widget)
        label.move(10, 10)  # Position fixe
        label.resize(80, 30)

        line_edit = QLineEdit(central_widget)
        line_edit.move(100, 10)  # Position fixe
        line_edit.resize(200, 30)

        button = QPushButton('Valider', central_widget)
        button.move(150, 50)  # Position fixe
        button.resize(100, 30)


class GoodExample(QMainWindow):
    """Exemple avec layout - Recommandé"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Avec Layout - Adaptatif')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout qui s'adapte automatiquement
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Layout horizontal pour le champ
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Nom:'))
        input_layout.addWidget(QLineEdit())

        # Ajout au layout principal
        layout.addLayout(input_layout)
        layout.addWidget(QPushButton('Valider'))
```

### 1.2 Avantages des layouts

- **Adaptabilité** : L'interface s'ajuste automatiquement lors du redimensionnement
- **Cohérence** : Espacement et alignement uniformes
- **Maintenabilité** : Facilite les modifications ultérieures
- **Responsivité** : Support de différentes résolutions d'écran

---

## 2. Composants d'interface de base

### 2.1 Widgets d'entrée essentiels

```python
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QLabel,
    QLineEdit,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class InputWidgetsDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Composants d'entrée")
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

        # QLineEdit - Saisie de texte sur une ligne
        layout.addWidget(QLabel("Nom d'utilisateur:"))
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText('Entrez votre nom')
        self.username_edit.setMaxLength(50)
        layout.addWidget(self.username_edit)

        # QTextEdit - Saisie multiligne
        layout.addWidget(QLabel('Description:'))
        self.description_edit = QTextEdit()
        self.description_edit.setMaximumHeight(100)
        layout.addWidget(self.description_edit)

        # QComboBox - Liste déroulante
        layout.addWidget(QLabel('Pays:'))
        self.country_combo = QComboBox()
        self.country_combo.addItems(['France', 'Allemagne', 'Espagne', 'Italie'])
        self.country_combo.setCurrentText('France')
        layout.addWidget(self.country_combo)

        # QSpinBox - Saisie de nombres entiers
        layout.addWidget(QLabel('Âge:'))
        self.age_spin = QSpinBox()
        self.age_spin.setRange(0, 120)
        self.age_spin.setValue(25)
        self.age_spin.setSuffix(' ans')
        layout.addWidget(self.age_spin)

        # QCheckBox - Case à cocher
        self.newsletter_check = QCheckBox("S'abonner à la newsletter")
        self.newsletter_check.setChecked(True)
        layout.addWidget(self.newsletter_check)

        # QDateEdit - Sélection de date
        layout.addWidget(QLabel('Date de naissance:'))
        self.birth_date = QDateEdit()
        self.birth_date.setDate(QDate.currentDate())
        self.birth_date.setCalendarPopup(True)
        layout.addWidget(self.birth_date)
```

### 2.2 Gestion des événements des widgets

```python
    def setup_connections(self) -> None:
        """Configure les connexions signal/slot"""
        # Réaction aux changements de texte
        self.username_edit.textChanged.connect(self.on_username_changed)

        # Validation à la fin de saisie
        self.username_edit.editingFinished.connect(self.validate_username)

        # Changement de sélection
        self.country_combo.currentTextChanged.connect(self.on_country_changed)

        # Changement de valeur numérique
        self.age_spin.valueChanged.connect(self.on_age_changed)

        # État des cases à cocher
        self.newsletter_check.toggled.connect(self.on_newsletter_toggled)

    def on_username_changed(self, text: str) -> None:
        """Appelé à chaque caractère tapé"""
        if len(text) < 3:
            self.username_edit.setStyleSheet('border: 2px solid red;')
        else:
            self.username_edit.setStyleSheet('border: 2px solid green;')

    def validate_username(self) -> None:
        """Validation finale du nom d'utilisateur"""
        username = self.username_edit.text().strip()
        if not username:
            QMessageBox.warning(self, 'Erreur', "Le nom d'utilisateur est requis")

    def on_country_changed(self, country: str) -> None:
        """Réaction au changement de pays"""
        print(f'Pays sélectionné: {country}')

    def on_age_changed(self, age: int) -> None:
        """Réaction au changement d'âge"""
        if age >= 18:
            print('Utilisateur majeur')
        else:
            print('Utilisateur mineur')

    def on_newsletter_toggled(self, checked: bool) -> None:
        """Réaction au changement d'abonnement"""
        status = 'abonné' if checked else 'désabonné'
        print(f'Newsletter: {status}')
```

---

## 3. Layout horizontal (QHBoxLayout)

### 3.1 Utilisation basique

```python
class HorizontalLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Horizontal")
        self.setup_ui()
    
    def setup_ui(self):
        # Création du layout horizontal
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Ajout de widgets côte à côte
        layout.addWidget(QLabel("Recherche:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Rechercher"))
        layout.addWidget(QPushButton("Effacer"))

class AdvancedHorizontalLayout(QWidget):
    """Layout horizontal avec contrôle avancé"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Horizontal Avancé")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Widget avec étirement
        layout.addWidget(QLabel("Nom:"))
        name_edit = QLineEdit()
        layout.addWidget(name_edit, 1)  # Facteur d'étirement = 1
        
        layout.addWidget(QLabel("Âge:"))
        age_spin = QSpinBox()
        layout.addWidget(age_spin, 0)  # Pas d'étirement (taille naturelle)
        
        # Espacement flexible
        layout.addStretch()  # Pousse les éléments suivants vers la droite
        
        layout.addWidget(QPushButton("OK"))
        layout.addWidget(QPushButton("Annuler"))
        
        # Contrôle des marges et espacement
        layout.setContentsMargins(10, 10, 10, 10)  # gauche, haut, droite, bas
        layout.setSpacing(5)  # Espacement entre widgets
```

### 3.2 Facteurs d'étirement et espacement

```python
def demonstrate_stretch_factors(self):
    """Démonstration des facteurs d'étirement"""
    layout = QHBoxLayout()
    
    # Widget 1: facteur 1 (prend 1 part de l'espace disponible)
    button1 = QPushButton("Bouton 1 (1x)")
    layout.addWidget(button1, 1)
    
    # Widget 2: facteur 2 (prend 2 parts de l'espace disponible)
    button2 = QPushButton("Bouton 2 (2x)")
    layout.addWidget(button2, 2)
    
    # Widget 3: facteur 0 (taille naturelle, pas d'étirement)
    button3 = QPushButton("Bouton 3 (fixe)")
    layout.addWidget(button3, 0)
    
    return layout

def demonstrate_spacing_control(self):
    """Contrôle précis de l'espacement"""
    layout = QHBoxLayout()
    
    layout.addWidget(QLabel("Début"))
    
    # Espacement fixe de 20 pixels
    layout.addSpacing(20)
    
    layout.addWidget(QPushButton("Milieu"))
    
    # Espacement flexible (s'étire)
    layout.addStretch(1)
    
    layout.addWidget(QLabel("Fin"))
    
    return layout
```

---

## 4. Layout vertical (QVBoxLayout)

### 4.1 Organisation verticale des widgets

```python
class VerticalLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Vertical")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Formulaire vertical classique
        layout.addWidget(QLabel("Informations personnelles"))
        
        # Champ nom
        layout.addWidget(QLabel("Nom complet:"))
        layout.addWidget(QLineEdit())
        
        # Champ email
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(QLineEdit())
        
        # Zone de commentaire
        layout.addWidget(QLabel("Commentaires:"))
        comment_edit = QTextEdit()
        comment_edit.setMaximumHeight(80)
        layout.addWidget(comment_edit)
        
        # Espace flexible avant les boutons
        layout.addStretch()
        
        # Boutons en bas
        layout.addWidget(QPushButton("Enregistrer"))
        layout.addWidget(QPushButton("Annuler"))

class ResponsiveVerticalLayout(QWidget):
    """Layout vertical adaptatif"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Vertical Adaptatif")
        self.setup_ui()
    
    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # En-tête fixe
        header = QLabel("Paramètres de l'application")
        header.setStyleSheet("""
            font-size: 18px; 
            font-weight: bold; 
            padding: 10px;
            background-color: #3498db;
            color: white;
        """)
        main_layout.addWidget(header)
        
        # Zone de contenu extensible
        content_area = QTextEdit()
        content_area.setPlainText("Zone de contenu principal...")
        main_layout.addWidget(content_area, 1)  # S'étire pour remplir l'espace
        
        # Barre d'état fixe
        status_bar = QLabel("Prêt")
        status_bar.setStyleSheet("padding: 5px; background-color: #ecf0f1;")
        main_layout.addWidget(status_bar, 0)  # Taille fixe
```

### 4.2 Alignement dans les layouts verticaux

```python
def demonstrate_vertical_alignment(self):
    """Démonstration des alignements verticaux"""
    layout = QVBoxLayout()
    
    # Alignement à gauche (par défaut)
    left_button = QPushButton("Aligné à gauche")
    layout.addWidget(left_button, 0, Qt.AlignmentFlag.AlignLeft)
    
    # Alignement centré
    center_button = QPushButton("Centré")
    layout.addWidget(center_button, 0, Qt.AlignmentFlag.AlignCenter)
    
    # Alignement à droite
    right_button = QPushButton("Aligné à droite")
    layout.addWidget(right_button, 0, Qt.AlignmentFlag.AlignRight)
    
    # Widget qui prend toute la largeur
    full_width_edit = QLineEdit("Toute la largeur")
    layout.addWidget(full_width_edit)  # Pas d'alignement = toute la largeur
    
    return layout
```

---

## 5. Layout en grille (QGridLayout)

### 5.1 Organisation tabulaire

```python
class GridLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout en Grille")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Formulaire organisé en grille
        # addWidget(widget, ligne, colonne)
        layout.addWidget(QLabel("Prénom:"), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        
        layout.addWidget(QLabel("Nom:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        
        layout.addWidget(QLabel("Email:"), 2, 0)
        layout.addWidget(QLineEdit(), 2, 1)
        
        layout.addWidget(QLabel("Téléphone:"), 3, 0)
        layout.addWidget(QLineEdit(), 3, 1)
        
        # Widget sur plusieurs colonnes
        # addWidget(widget, ligne, colonne, nb_lignes, nb_colonnes)
        comment_label = QLabel("Commentaires:")
        layout.addWidget(comment_label, 4, 0, 1, 2)  # Sur 2 colonnes
        
        comment_edit = QTextEdit()
        comment_edit.setMaximumHeight(60)
        layout.addWidget(comment_edit, 5, 0, 1, 2)  # Sur 2 colonnes
        
        # Boutons sur la dernière ligne
        layout.addWidget(QPushButton("Valider"), 6, 0)
        layout.addWidget(QPushButton("Annuler"), 6, 1)

class AdvancedGridLayout(QWidget):
    """Layout en grille avec fonctionnalités avancées"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grille Avancée")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Configuration des proportions de colonnes
        layout.setColumnStretch(0, 1)  # Colonne 0: facteur 1
        layout.setColumnStretch(1, 2)  # Colonne 1: facteur 2
        layout.setColumnStretch(2, 1)  # Colonne 2: facteur 1
        
        # Configuration des proportions de lignes
        layout.setRowStretch(1, 1)     # Ligne 1 s'étire
        
        # En-têtes
        layout.addWidget(QLabel("Paramètre"), 0, 0)
        layout.addWidget(QLabel("Valeur"), 0, 1)
        layout.addWidget(QLabel("Action"), 0, 2)
        
        # Première ligne de données
        layout.addWidget(QLabel("Timeout:"), 1, 0)
        timeout_spin = QSpinBox()
        timeout_spin.setRange(1, 3600)
        timeout_spin.setValue(30)
        layout.addWidget(timeout_spin, 1, 1)
        layout.addWidget(QPushButton("Reset"), 1, 2)
        
        # Widget occupant plusieurs cellules
        info_text = QTextEdit()
        info_text.setPlainText("Zone d'information étendue...")
        layout.addWidget(info_text, 2, 0, 2, 3)  # 2 lignes x 3 colonnes
        
        # Espacement personnalisé
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
```

### 5.2 Techniques avancées de grille

```python
def create_calculator_layout(self):
    """Exemple: disposition de calculatrice"""
    layout = QGridLayout()
    
    # Écran de la calculatrice
    display = QLineEdit("0")
    display.setReadOnly(True)
    display.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(display, 0, 0, 1, 4)  # Occupe toute la largeur
    
    # Boutons numériques et opérateurs
    buttons = [
        ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
        ('0', 5, 0, 1, 2), ('.', 5, 2), ('=', 5, 3)  # 0 sur 2 colonnes
    ]
    
    for button_data in buttons:
        text = button_data[0]
        row = button_data[1]
        col = button_data[2]
        
        btn = QPushButton(text)
        
        if len(button_data) == 5:  # Bouton étendu
            row_span = button_data[3]
            col_span = button_data[4]
            layout.addWidget(btn, row, col, row_span, col_span)
        else:
            layout.addWidget(btn, row, col)
    
    return layout
```

---

## 6. Layouts imbriqués et techniques avancées

### 6.1 Combinaison de layouts

```python
class NestedLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts Imbriqués")
        self.setup_ui()
    
    def setup_ui(self):
        # Layout principal vertical
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # En-tête avec layout horizontal
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Titre de l'application"))
        header_layout.addStretch()
        header_layout.addWidget(QPushButton("Aide"))
        header_layout.addWidget(QPushButton("Paramètres"))
        main_layout.addLayout(header_layout)
        
        # Zone centrale avec layout horizontal
        content_layout = QHBoxLayout()
        
        # Panneau de gauche
        left_panel = self.create_left_panel()
        content_layout.addWidget(left_panel, 1)
        
        # Zone principale
        main_area = self.create_main_area()
        content_layout.addWidget(main_area, 3)
        
        # Panneau de droite
        right_panel = self.create_right_panel()
        content_layout.addWidget(right_panel, 1)
        
        main_layout.addLayout(content_layout, 1)
        
        # Pied de page avec layout horizontal
        footer_layout = QHBoxLayout()
        footer_layout.addWidget(QLabel("Statut: Prêt"))
        footer_layout.addStretch()
        footer_layout.addWidget(QLabel("Ligne: 1, Col: 1"))
        main_layout.addLayout(footer_layout)
    
    def create_left_panel(self):
        """Crée le panneau de navigation gauche"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        layout.addWidget(QLabel("Navigation"))
        layout.addWidget(QPushButton("Accueil"))
        layout.addWidget(QPushButton("Documents"))
        layout.addWidget(QPushButton("Paramètres"))
        layout.addStretch()
        
        widget.setMaximumWidth(150)
        widget.setStyleSheet("background-color: #f8f9fa; border-right: 1px solid #dee2e6;")
        return widget
    
    def create_main_area(self):
        """Crée la zone principale de travail"""
        widget = QTextEdit()
        widget.setPlainText("Zone de travail principale\n\nContenu de l'application...")
        return widget
    
    def create_right_panel(self):
        """Crée le panneau d'outils de droite"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        layout.addWidget(QLabel("Outils"))
        
        # Groupe d'outils avec layout en grille
        tools_layout = QGridLayout()
        tools_layout.addWidget(QPushButton("A"), 0, 0)
        tools_layout.addWidget(QPushButton("B"), 0, 1)
        tools_layout.addWidget(QPushButton("C"), 1, 0)
        tools_layout.addWidget(QPushButton("D"), 1, 1)
        layout.addLayout(tools_layout)
        
        layout.addStretch()
        
        widget.setMaximumWidth(120)
        widget.setStyleSheet("background-color: #f8f9fa; border-left: 1px solid #dee2e6;")
        return widget
```

### 6.2 Layouts conditionnels et dynamiques

```python
class DynamicLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts Dynamiques")
        self.setup_ui()
    
    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        # Contrôles pour modifier le layout
        controls_layout = QHBoxLayout()
        
        self.layout_combo = QComboBox()
        self.layout_combo.addItems(["Vertical", "Horizontal", "Grille"])
        self.layout_combo.currentTextChanged.connect(self.change_layout)
        controls_layout.addWidget(QLabel("Type de layout:"))
        controls_layout.addWidget(self.layout_combo)
        
        add_button = QPushButton("Ajouter widget")
        add_button.clicked.connect(self.add_widget)
        controls_layout.addWidget(add_button)
        
        remove_button = QPushButton("Supprimer widget")
        remove_button.clicked.connect(self.remove_widget)
        controls_layout.addWidget(remove_button)
        
        self.main_layout.addLayout(controls_layout)
        
        # Zone de contenu dynamique
        self.content_widget = QWidget()
        self.main_layout.addWidget(self.content_widget)
        
        self.widgets_list = []
        self.change_layout("Vertical")  # Layout initial
    
    def change_layout(self, layout_type):
        """Change le type de layout dynamiquement"""
        # Supprimer l'ancien layout
        if self.content_widget.layout():
            QWidget().setLayout(self.content_widget.layout())
        
        # Créer le nouveau layout
        if layout_type == "Vertical":
            new_layout = QVBoxLayout()
        elif layout_type == "Horizontal":
            new_layout = QHBoxLayout()
        else:  # Grille
            new_layout = QGridLayout()
        
        self.content_widget.setLayout(new_layout)
        
        # Ré-ajouter tous les widgets
        self.reorganize_widgets()
    
    def add_widget(self):
        """Ajoute un nouveau widget"""
        widget_count = len(self.widgets_list)
        button = QPushButton(f"Widget {widget_count + 1}")
        self.widgets_list.append(button)
        self.reorganize_widgets()
    
    def remove_widget(self):
        """Supprime le dernier widget"""
        if self.widgets_list:
            widget = self.widgets_list.pop()
            widget.setParent(None)
            self.reorganize_widgets()
    
    def reorganize_widgets(self):
        """Réorganise les widgets selon le layout actuel"""
        layout = self.content_widget.layout()
        
        for widget in self.widgets_list:
            if isinstance(layout, QVBoxLayout) or isinstance(layout, QHBoxLayout):
                layout.addWidget(widget)
            elif isinstance(layout, QGridLayout):
                # Disposition en grille 3x3
                index = self.widgets_list.index(widget)
                row = index // 3
                col = index % 3
                layout.addWidget(widget, row, col)
```

---

## 7. Politiques de taille et espacement

### 7.1 Politiques de taille des widgets

```python
from PyQt6.QtWidgets import QSizePolicy

class SizePolicyDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Politiques de Taille")
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Widget avec politique Fixed (taille fixe)
        fixed_button = QPushButton("Taille Fixe")
        fixed_button.setSizePolicy(
            QSizePolicy.Policy.Fixed, 
            QSizePolicy.Policy.Fixed
        )
        fixed_button.setFixedSize(100, 30)
        layout.addWidget(fixed_button)
        
        # Widget avec politique Minimum (taille minimale respectée)
        minimum_button = QPushButton("Taille Minimum")
        minimum_button.setSizePolicy(
            QSizePolicy.Policy.Minimum,
            QSizePolicy.Policy.Minimum
        )
        minimum_button.setMinimumSize(150, 40)
        layout.addWidget(minimum_button)
        
        # Widget avec politique Expanding (s'étire pour remplir)
        expanding_button = QPushButton("S'étire pour remplir")
        expanding_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        layout.addWidget(expanding_button)
        
        # Widget avec politique Preferred (taille préférée)
        preferred_edit = QLineEdit("Taille préférée")
        preferred_edit.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred
        )
        layout.addWidget(preferred_edit)
        
        # Widget avec politique Maximum (ne dépasse pas la taille max)
        maximum_label = QLabel("Taille maximale limitée")
        maximum_label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )
        maximum_label.setMaximumSize(200, 50)
        maximum_label.setStyleSheet("border: 1px solid black;")
        layout.addWidget(maximum_label)

def demonstrate_size_hints(self):
    """Démonstration des indices de taille"""
    widget = QPushButton("Bouton personnalisé")
    
    # Définir les tailles recommandées
    widget.setMinimumSize(80, 25)    # Taille minimale
    widget.setMaximumSize(200, 50)   # Taille maximale
    widget.resize(120, 35)           # Taille préférée
    
    # Alternative: surcharger sizeHint()
    # def sizeHint(self):
    #     return QSize(120, 35)
    
    return widget
```

### 7.2 Gestion avancée de l'espacement

```python
class SpacingDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion de l'espacement")
        self.setup_ui()
    
    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Section 1: Espacement uniforme
        main_layout.addWidget(QLabel("Espacement uniforme:"))
        uniform_layout = QHBoxLayout()
        uniform_layout.setSpacing(20)  # 20 pixels entre chaque widget
        for i in range(4):
            uniform_layout.addWidget(QPushButton(f"Btn {i+1}"))
        main_layout.addLayout(uniform_layout)
        
        # Section 2: Espacement variable
        main_layout.addWidget(QLabel("Espacement variable:"))
        variable_layout = QHBoxLayout()
        variable_layout.addWidget(QPushButton("Début"))
        variable_layout.addSpacing(5)   # 5 pixels
        variable_layout.addWidget(QPushButton("Proche"))
        variable_layout.addSpacing(50)  # 50 pixels
        variable_layout.addWidget(QPushButton("Éloigné"))
        variable_layout.addStretch()   # Espace flexible
        variable_layout.addWidget(QPushButton("Fin"))
        main_layout.addLayout(variable_layout)
        
        # Section 3: Marges personnalisées
        main_layout.addWidget(QLabel("Marges personnalisées:"))
        margin_widget = QWidget()
        margin_layout = QHBoxLayout()
        margin_layout.setContentsMargins(30, 10, 30, 10)  # G, H, D, B
        margin_layout.addWidget(QPushButton("Avec marges"))
        margin_widget.setLayout(margin_layout)
        margin_widget.setStyleSheet("border: 1px solid blue;")
        main_layout.addWidget(margin_widget)
        
        # Section 4: Contrôle fin avec QSpacerItem
        main_layout.addWidget(QLabel("Contrôle fin avec QSpacerItem:"))
        spacer_layout = QHBoxLayout()
        spacer_layout.addWidget(QPushButton("Gauche"))
        
        # QSpacerItem personnalisé
        from PyQt6.QtWidgets import QSpacerItem
        spacer = QSpacerItem(
            40, 20,  # Largeur, hauteur
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        spacer_layout.addItem(spacer)
        
        spacer_layout.addWidget(QPushButton("Droite"))
        main_layout.addLayout(spacer_layout)
```

---

## 8. Adaptation automatique et responsivité

### 8.1 Interfaces adaptatives

```python
class ResponsiveDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface Responsive")
        self.setMinimumSize(300, 200)
        self.setup_ui()
    
    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.create_responsive_content()
        
        # Détecter les changements de taille
        self.resizeEvent = self.on_resize
    
    def create_responsive_content(self):
        """Crée un contenu qui s'adapte à la taille"""
        # En-tête adaptatif
        header_layout = QHBoxLayout()
        
        title_label = QLabel("Application Responsive")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Menu burger pour petites tailles
        self.menu_button = QPushButton("☰")
        self.menu_button.setMaximumWidth(40)
        self.menu_button.clicked.connect(self.toggle_sidebar)
        header_layout.addWidget(self.menu_button)
        
        self.main_layout.addLayout(header_layout)
        
        # Zone de contenu adaptative
        self.content_layout = QHBoxLayout()
        
        # Barre latérale
        self.sidebar = self.create_sidebar()
        self.content_layout.addWidget(self.sidebar)
        
        # Zone principale
        main_content = QTextEdit()
        main_content.setPlainText("Zone de contenu principal\n\nCette zone s'adapte à la taille de la fenêtre.")
        self.content_layout.addWidget(main_content, 1)
        
        self.main_layout.addLayout(self.content_layout)
    
    def create_sidebar(self):
        """Crée une barre latérale adaptative"""
        sidebar = QWidget()
        sidebar.setMinimumWidth(150)
        sidebar.setMaximumWidth(200)
        
        layout = QVBoxLayout()
        sidebar.setLayout(layout)
        
        layout.addWidget(QLabel("Navigation"))
        layout.addWidget(QPushButton("Accueil"))
        layout.addWidget(QPushButton("Documents"))
        layout.addWidget(QPushButton("Paramètres"))
        layout.addStretch()
        
        sidebar.setStyleSheet("background-color: #f8f9fa;")
        return sidebar
    
    def on_resize(self, event):
        """Appelé lors du redimensionnement"""
        super().resizeEvent(event)
        
        width = self.width()
        
        # Masquer la sidebar si la fenêtre est trop petite
        if width < 500:
            self.sidebar.hide()
            self.menu_button.show()
        else:
            self.sidebar.show()
            self.menu_button.hide()
    
    def toggle_sidebar(self):
        """Affiche/masque la sidebar"""
        self.sidebar.setVisible(not self.sidebar.isVisible())
```

### 8.2 Gestion de différentes résolutions

```python
class MultiResolutionDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Support Multi-Résolution")
        self.setup_ui()
        self.adapt_to_screen()
    
    def adapt_to_screen(self):
        """Adapte l'interface à la résolution d'écran"""
        from PyQt6.QtGui import QGuiApplication
        
        screen = QGuiApplication.primaryScreen()
        screen_size = screen.size()
        dpi = screen.logicalDotsPerInch()
        
        # Ajuster selon la résolution
        if screen_size.width() >= 1920:  # Haute résolution
            self.setMinimumSize(800, 600)
            font_size = 12
        elif screen_size.width() >= 1366:  # Résolution standard
            self.setMinimumSize(600, 450)
            font_size = 10
        else:  # Petite résolution
            self.setMinimumSize(400, 300)
            font_size = 9
        
        # Ajuster la taille de police
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)
        
        # Adapter l'espacement selon le DPI
        spacing = max(5, int(dpi / 96 * 5))
        self.layout().setSpacing(spacing)
    
    def setup_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Interface qui s'adapte automatiquement
        for i in range(3):
            for j in range(3):
                button = QPushButton(f"Btn {i*3+j+1}")
                layout.addWidget(button, i, j)
```

---

## 9. Travaux pratiques

### 🚧 TP1 - Formulaire avec layouts de base
**Durée** : 30 minutes
- Créer un formulaire d'inscription avec layouts verticaux et horizontaux
- Utiliser différents widgets d'entrée avec validation

### 🚧 TP2 - Interface en grille avancée
**Durée** : 30 minutes  
- Concevoir une calculatrice avec QGridLayout
- Gérer les widgets multi-cellules et l'espacement

### 🚧 TP3 - Layouts imbriqués complexes
**Durée** : 30 minutes
- Créer une interface style IDE avec panneaux multiples
- Implémenter des zones redimensionnables

### 🚧 TP4 - Interface responsive
**Durée** : 30 minutes
- Développer une interface qui s'adapte au redimensionnement
- Gérer différents modes d'affichage selon la taille

---

## 10. Points clés à retenir

### ✅ Choix du layout approprié
- **QHBoxLayout** : Organisation horizontale, barres d'outils, boutons
- **QVBoxLayout** : Formulaires, listes verticales, organisation séquentielle  
- **QGridLayout** : Formulaires complexes, interfaces tabulaires, calculatrices

### ✅ Politiques de taille et espacement
- Utiliser les politiques de taille pour contrôler le comportement d'étirement
- Gérer l'espacement avec `setSpacing()` et `setContentsMargins()`
- Exploiter `addStretch()` pour créer des espaces flexibles

### ✅ Layouts imbriqués
- Combiner différents types de layouts pour des interfaces complexes
- Organiser logiquement l'interface en zones fonctionnelles
- Maintenir la cohérence visuelle malgré la complexité

### ✅ Responsivité et adaptation
- Prévoir le comportement lors du redimensionnement
- Tester sur différentes résolutions d'écran
- Utiliser les signaux de redimensionnement pour l'adaptation dynamique

---

## Prochaine étape

Dans le **Chapitre 4 - Traitement des événements**, nous découvrirons :
- Le système d'événements Qt et la boucle d'événements
- Le paradigme signaux/slots pour la communication entre objets
- La gestion des événements clavier, souris et personnalisés
- Les techniques avancées de connexion et déconnexion
