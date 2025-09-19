# Chapitre 3 : Gestion des stratégies de placement (Layout)

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
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

### 1.1 Qu'est-ce qu'un layout ?

En PyQt6, un **layout** (gestionnaire de disposition) est un système qui organise automatiquement la position et la taille des widgets dans une fenêtre. Contrairement au positionnement manuel, les layouts permettent de créer des interfaces qui s'adaptent dynamiquement aux changements de taille et aux différentes résolutions d'écran.

### 1.2 Les types de layouts disponibles

PyQt6 propose quatre layouts principaux pour organiser vos widgets :

| Layout | Comportement | Usage typique |
|--------|-------------|---------------|
| `QHBoxLayout` | Disposition horizontale linéaire | Barres d'outils, boutons alignés |
| `QVBoxLayout` | Disposition verticale linéaire | Formulaires, menus, listes |
| `QGridLayout` | Grille indexée X×Y | Formulaires complexes, calculatrices |
| `QFormLayout` | Formulaire étiquette-champ | Saisie de données structurées |

### 1.3 Principe de fonctionnement

Chaque layout suit une logique spécifique :

- **Layouts linéaires** (`QHBoxLayout`, `QVBoxLayout`) : Les widgets sont ajoutés séquentiellement dans une direction
- **Layout en grille** (`QGridLayout`) : Les widgets sont positionnés par coordonnées (ligne, colonne)  
- **Layout de formulaire** (`QFormLayout`) : Optimisé pour les paires étiquette-widget

### 1.4 Pourquoi utiliser des layouts ?

Les layouts apportent des avantages cruciaux pour le développement d'interfaces professionnelles :

```python
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class BadExample(QMainWindow):
    """Exemple de ce qu'il ne faut PAS faire."""

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
    """Exemple avec layout - Recommandé."""

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

### 1.5 Avantages des layouts

Les layouts offrent de nombreux bénéfices par rapport au positionnement manuel :

#### 🎯 **Adaptabilité automatique**
- L'interface se redimensionne intelligemment quand la fenêtre change de taille
- Les widgets maintiennent leurs relations spatiales et leurs proportions
- Fini les widgets qui disparaissent ou se chevauchent lors du redimensionnement

#### 🎨 **Cohérence visuelle**
- Espacement uniforme et professionnel entre les éléments
- Alignement automatique selon les règles du layout choisi
- Respect des conventions d'interface de l'OS cible

#### 🔧 **Maintenabilité du code**  
- Ajout ou suppression de widgets sans recalculer les positions
- Modifications d'interface plus rapides et moins sujettes aux erreurs
- Séparation claire entre la logique métier et la présentation

#### 📱 **Support multi-plateforme**
- Adaptation automatique aux différentes résolutions d'écran
- Respect des conventions visuelles de chaque système d'exploitation
- Interface utilisable sur desktop, tablette ou écrans haute résolution

#### ⚡ **Performance optimisée**
- Qt optimise automatiquement le calcul des positions
- Réduction des calculs manuels et des erreurs de positionnement
- Gestion efficace des mises à jour d'affichage

---

## 2. Layout horizontal (QHBoxLayout)

### 2.1 Principe et cas d'usage

Le `QHBoxLayout` organise les widgets **horizontalement**, de gauche à droite (ou de droite à gauche selon la locale). C'est l'un des layouts les plus utilisés pour créer des interfaces ergonomiques.

#### 🎯 **Quand utiliser QHBoxLayout ?**
- **Barres d'outils** : Boutons d'action alignés horizontalement
- **Champs de recherche** : Label + champ de saisie + bouton de recherche
- **Boutons de validation** : OK, Annuler, Appliquer en fin de dialogue
- **Indicateurs de statut** : Informations disposées côte à côte
- **Navigation** : Boutons Précédent/Suivant, pagination

#### ⚙️ **Comportement du layout horizontal**
- Les widgets sont ajoutés **séquentiellement** de gauche à droite
- La **hauteur** de tous les widgets s'aligne sur le plus haut
- La **largeur** peut être contrôlée par les facteurs d'étirement
- L'**espacement** entre widgets est uniforme (configurable)

#### 📏 **Gestion de l'espace**
- **Facteur d'étirement** : Contrôle comment les widgets se partagent l'espace horizontal
- **Espacement fixe** : Distance minimale garantie entre les widgets  
- **Marges** : Espace autour du layout entier
- **Stretch** : Zones flexibles qui absorbent l'espace supplémentaire

### 2.2 Utilisation basique

```python
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QWidget,
)


class HorizontalLayoutDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layout Horizontal")
        self.setup_ui()
    
    def setup_ui(self) -> None:
        # Création du layout horizontal
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Ajout de widgets côte à côte
        layout.addWidget(QLabel("Recherche:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Rechercher"))
        layout.addWidget(QPushButton("Effacer"))


class AdvancedHorizontalLayout(QWidget):
    """Layout horizontal avec contrôle avancé."""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layout Horizontal Avancé")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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

### 2.3 Facteurs d'étirement et espacement

```python
def demonstrate_stretch_factors(self) -> QHBoxLayout:
    """Démonstration des facteurs d'étirement."""
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

def demonstrate_spacing_control(self) -> QHBoxLayout:
    """Contrôle précis de l'espacement."""
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

## 3. Layout vertical (QVBoxLayout)

### 3.1 Principe et philosophie

Le `QVBoxLayout` organise les widgets **verticalement**, de haut en bas. Il constitue la base de nombreuses interfaces utilisateur, particulièrement adaptées aux workflows séquentiels et à la présentation hiérarchique d'informations.

#### 🎯 **Quand utiliser QVBoxLayout ?**
- **Formulaires** : Succession d'étiquettes et de champs de saisie
- **Listes et menus** : Éléments empilés verticalement
- **Interfaces de configuration** : Sections organisées de haut en bas
- **Flux de travail** : Étapes séquentielles d'un processus
- **Zones de contenu** : Articles, messages, éléments de feed

#### ⚙️ **Comportement du layout vertical**
- Les widgets sont ajoutés **séquentiellement** de haut en bas
- La **largeur** de tous les widgets s'étend sur toute la largeur disponible
- La **hauteur** peut être contrôlée par les facteurs d'étirement et politiques de taille
- L'**ordre d'ajout** détermine l'ordre d'affichage vertical

#### 📏 **Stratégies de dimensionnement**
- **Facteur d'étirement** : Détermine comment les widgets se partagent l'espace vertical
- **Taille fixe** : Widgets qui gardent leur hauteur naturelle (boutons, labels)
- **Zones extensibles** : Widgets qui peuvent grandir (QTextEdit, listes)
- **Espacement intelligent** : Adaptation automatique selon le contenu

### 3.2 Organisation verticale des widgets

```python
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class VerticalLayoutDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layout Vertical")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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
    """Layout vertical adaptatif."""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layout Vertical Adaptatif")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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

### 3.3 Alignement dans les layouts verticaux

```python
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout


def demonstrate_vertical_alignment(self) -> QVBoxLayout:
    """Démonstration des alignements verticaux."""
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

## 4. Layout en grille (QGridLayout)

### 4.1 Principe du layout en grille

Le `QGridLayout` est le plus flexible et puissant des layouts PyQt6. Il organise les widgets dans une **grille bidimensionnelle** (lignes × colonnes), similaire à un tableau HTML ou à une feuille de calcul.

#### 🎯 **Quand utiliser QGridLayout ?**
- **Formulaires complexes** : Nombreux champs organisés en colonnes
- **Calculatrices** : Boutons organisés en grille régulière
- **Interfaces de configuration** : Paramètres groupés par catégories
- **Dashboards** : Widgets d'information disposés en grille
- **Grilles de données** : Affichage tabulaire d'informations

#### ⚙️ **Concepts fondamentaux**
- **Coordonnées** : Chaque widget est positionné par (ligne, colonne)
- **Fusion de cellules** : Un widget peut occuper plusieurs cellules
- **Alignement** : Contrôle précis de la position dans chaque cellule
- **Proportions** : Contrôle de la taille relative des lignes et colonnes

#### 📊 **Avantages du QGridLayout**
- **Flexibilité maximale** : Combine les avantages des layouts linéaires
- **Alignement complexe** : Widgets alignés à la fois horizontalement et verticalement
- **Évolutivité** : Facile d'ajouter des lignes/colonnes sans tout réorganiser
- **Espacement uniforme** : Grille régulière avec espacement cohérent

#### 🔧 **Stratégies de dimensionnement**
- **Étirement de colonnes** : `setColumnStretch()` pour contrôler la largeur relative
- **Étirement de lignes** : `setRowStretch()` pour contrôler la hauteur relative
- **Taille minimale** : `setColumnMinimumWidth()`, `setRowMinimumHeight()`
- **Fusion de cellules** : Widgets s'étendant sur plusieurs lignes/colonnes

### 4.2 Organisation tabulaire

```python
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QWidget,
)


class GridLayoutDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layout en Grille")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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
    """Layout en grille avec fonctionnalités avancées."""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Grille Avancée")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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

### 4.3 Techniques avancées de grille

```python
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QPushButton


def create_calculator_layout(self) -> QGridLayout:
    """Exemple: disposition de calculatrice."""
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

## 5. Layouts imbriqués

```python
from PyQt6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class NestedLayoutDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Layouts Imbriqués")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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
    
    def create_left_panel(self) -> QWidget:
        """Crée le panneau de navigation gauche."""
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
    
    def create_main_area(self) -> QTextEdit:
        """Crée la zone principale de travail."""
        widget = QTextEdit()
        widget.setPlainText("Zone de travail principale\n\nContenu de l'application...")
        return widget
    
    def create_right_panel(self) -> QWidget:
        """Crée le panneau d'outils de droite."""
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

---

## 6. Bonnes pratiques d'organisation d'interface

### 6.1 Choisir le bon layout

Le choix du layout est crucial pour créer une interface intuitive et maintenable. Voici un guide de décision :

#### 🎯 **Arbre de décision pour le choix du layout**

```
Combien de widgets à organiser ?
├── 1-3 widgets simples
│   ├── Côte à côte → QHBoxLayout
│   └── Empilés → QVBoxLayout
├── 4-8 widgets
│   ├── Formulaire simple → QVBoxLayout + QHBoxLayout imbriqués
│   ├── Grille régulière → QGridLayout
│   └── Paires étiquette-champ → QFormLayout
└── 9+ widgets complexes
    ├── Zones distinctes → Layouts imbriqués
    ├── Interface modulaire → QGridLayout principal + sous-layouts
    └── Application complète → Architecture en couches
```

#### 📋 **Critères de choix selon le contexte**

| Contexte | Layout recommandé | Justification |
|----------|-------------------|---------------|
| Barre d'outils | `QHBoxLayout` | Actions alignées, accès rapide |
| Formulaire de saisie | `QVBoxLayout` ou `QFormLayout` | Flux de lecture naturel (haut→bas) |
| Panneau de configuration | `QGridLayout` | Organisation logique en sections |
| Interface de jeu/calculatrice | `QGridLayout` | Disposition régulière des boutons |
| Dashboard | Layouts imbriqués | Zones fonctionnelles distinctes |

### 6.2 Principes de design d'interface

#### 🎨 **Hiérarchie visuelle**
- **Groupement logique** : Regrouper les éléments liés fonctionnellement
- **Espacement cohérent** : Utiliser des proportions harmonieuses (règle des 8px)
- **Alignement** : Créer des lignes de force visuelles claires
- **Contraste de taille** : Différencier l'importance des éléments

#### 🧭 **Flux de navigation**
- **Ordre de lecture** : Respecter le sens de lecture (gauche→droite, haut→bas)
- **Actions primaires** : Placer les boutons principaux en position dominante
- **Cohérence spatiale** : Même fonction = même position dans l'interface
- **Zone d'attention** : Centrer l'attention sur l'action attendue

#### ⚖️ **Équilibre et proportions**
```python
# Exemple de proportions équilibrées
main_layout = QHBoxLayout()
sidebar_layout = QVBoxLayout()    # Largeur : 1 part
content_layout = QVBoxLayout()    # Largeur : 3 parts
tools_layout = QVBoxLayout()      # Largeur : 1 part

main_layout.addLayout(sidebar_layout, 1)   # 20% de la largeur
main_layout.addLayout(content_layout, 3)   # 60% de la largeur  
main_layout.addLayout(tools_layout, 1)     # 20% de la largeur
```

---

## 7. Politiques de taille et espacement

### 7.1 Politiques de taille des widgets

```python
from PyQt6.QtWidgets import QSizePolicy

class SizePolicyDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Politiques de Taille")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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

def demonstrate_size_hints(self) -> QPushButton:
    """Démonstration des indices de taille."""
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
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Gestion de l'espacement")
        self.setup_ui()
    
    def setup_ui(self) -> None:
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

## 8. Interfaces adaptatives et responsivité

### 8.1 Principes des interfaces adaptatives

Une interface adaptative se réajuste automatiquement selon l'espace disponible et les contraintes d'affichage. En PyQt6, cette capacité est essentielle pour créer des applications robustes qui fonctionnent sur différents écrans et configurations.

#### 🎯 **Objectifs d'une interface adaptive**
- **Utilisabilité préservée** : Fonctionnalités accessibles quelle que soit la taille d'écran
- **Lisibilité maintenue** : Texte et éléments restent clairs et visibles
- **Navigation intuitive** : Accès aux fonctions principales toujours possible
- **Esthétique cohérente** : Design harmonieux à toutes les résolutions

#### 🔄 **Stratégies d'adaptation**

1. **Adaptation par taille** : Modifier la disposition selon les dimensions disponibles
2. **Adaptation par densité** : Ajuster selon la résolution (DPI) de l'écran
3. **Adaptation par orientation** : Réorganiser pour portrait/paysage
4. **Adaptation contextuelle** : Masquer/montrer selon l'usage

#### 📐 **Techniques de mise en œuvre**

| Technique | Mécanisme | Usage typique |
|-----------|-----------|---------------|
| **Layouts flexibles** | Facteurs d'étirement, politiques de taille | Redimensionnement continu |
| **Seuils de taille** | `resizeEvent()`, breakpoints | Changements de mode d'affichage |
| **Masquage progressif** | `setVisible()` conditionnel | Simplification pour petits écrans |
| **Réorganisation** | Layouts multiples, `setLayout()` | Changement de structure |

### 8.2 Implémentation d'interfaces adaptatives

```python
class ResponsiveDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Interface Responsive")
        self.setMinimumSize(300, 200)
        self.setup_ui()
    
    def setup_ui(self) -> None:
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.create_responsive_content()
        
        # Détecter les changements de taille
        self.resizeEvent = self.on_resize
    
    def create_responsive_content(self) -> None:
        """Crée un contenu qui s'adapte à la taille."""
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
    
    def create_sidebar(self) -> QWidget:
        """Crée une barre latérale adaptative."""
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
    
    def on_resize(self, event) -> None:
        """Appelé lors du redimensionnement."""
        super().resizeEvent(event)
        
        width = self.width()
        
        # Masquer la sidebar si la fenêtre est trop petite
        if width < 500:
            self.sidebar.hide()
            self.menu_button.show()
        else:
            self.sidebar.show()
            self.menu_button.hide()
    
    def toggle_sidebar(self) -> None:
        """Affiche/masque la sidebar."""
        self.sidebar.setVisible(not self.sidebar.isVisible())
```

### 8.3 Gestion avancée des résolutions et DPI

La diversité des écrans modernes (des smartphones aux moniteurs 4K) impose une gestion intelligente des résolutions et densités de pixels.

#### 📏 **Comprendre les résolutions d'écran**
- **Résolution physique** : Pixels réels de l'écran (1920×1080, 2560×1440, etc.)
- **Résolution logique** : Pixels utilisés par l'OS pour l'affichage
- **DPI/PPI** : Densité de pixels par pouce (96, 144, 192 DPI typiques)
- **Facteur d'échelle** : Ratio entre résolution physique et logique

#### 🎛️ **Stratégies d'adaptation**

```python
# Exemple de détection et adaptation automatique
def get_display_characteristics() -> tuple[int, int, float]:
    """Obtient les caractéristiques de l'écran principal."""
    screen = QGuiApplication.primaryScreen()
    geometry = screen.geometry()
    dpi = screen.logicalDotsPerInch()
    scale_factor = screen.devicePixelRatio()
    
    return geometry.width(), geometry.height(), dpi, scale_factor

def calculate_ui_scaling(width: int, height: int, dpi: float) -> dict:
    """Calcule les paramètres d'interface selon l'écran."""
    # Catégorisation des écrans
    if width >= 2560:  # 2K et plus
        category = "high_res"
        base_font_size = 11
        spacing_factor = 1.2
        min_window_size = (1000, 700)
    elif width >= 1920:  # Full HD
        category = "standard"
        base_font_size = 10
        spacing_factor = 1.0
        min_window_size = (800, 600)
    elif width >= 1366:  # HD
        category = "compact"
        base_font_size = 9
        spacing_factor = 0.8
        min_window_size = (600, 450)
    else:  # Petits écrans
        category = "minimal"
        base_font_size = 8
        spacing_factor = 0.6
        min_window_size = (400, 300)
    
    # Ajustement selon le DPI
    if dpi > 120:
        base_font_size += 1
        spacing_factor *= 1.1
    
    return {
        "category": category,
        "font_size": base_font_size,
        "spacing": int(8 * spacing_factor),
        "margins": int(12 * spacing_factor),
        "min_size": min_window_size
    }
```

### 8.4 Breakpoints et modes d'affichage

#### 📱 **Définition des breakpoints**
Les breakpoints définissent les seuils où l'interface change de mode d'affichage :

```python
class BreakpointManager:
    """Gestionnaire des seuils de redimensionnement."""
    
    # Breakpoints standards (largeurs en pixels)
    BREAKPOINTS = {
        'mobile': 480,
        'tablet': 768, 
        'desktop': 1024,
        'wide': 1440
    }
    
    @classmethod
    def get_current_mode(cls, width: int) -> str:
        """Détermine le mode selon la largeur."""
        if width < cls.BREAKPOINTS['mobile']:
            return 'mobile'
        elif width < cls.BREAKPOINTS['tablet']:
            return 'tablet'
        elif width < cls.BREAKPOINTS['desktop']:
            return 'desktop'
        else:
            return 'wide'
    
    @classmethod
    def should_adapt(cls, old_width: int, new_width: int) -> bool:
        """Vérifie si une adaptation est nécessaire."""
        old_mode = cls.get_current_mode(old_width)
        new_mode = cls.get_current_mode(new_width)
        return old_mode != new_mode
```

### 8.5 Gestion de différentes résolutions

```python
class MultiResolutionDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Support Multi-Résolution")
        self.setup_ui()
        self.adapt_to_screen()
    
    def adapt_to_screen(self) -> None:
        """Adapte l'interface à la résolution d'écran."""
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
    
    def setup_ui(self) -> None:
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

Dans le **Chapitre 4 - Qt Designer**, nous découvrirons :
- Le système d'événements Qt et la boucle d'événements
- Le paradigme signaux/slots pour la communication entre objets
- La gestion des événements clavier, souris et personnalisés
- Les techniques avancées de connexion et déconnexion
