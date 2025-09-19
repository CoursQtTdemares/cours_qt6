# Chapitre 2 : Principes généraux de PyQt6

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Structurer une application Qt complète avec fenêtre principale
- Créer et organiser des barres de menus, d'outils et de statut
- Intégrer des styles CSS pour personnaliser l'apparence
- Implémenter des menus contextuels interactifs
- Gérer l'interconnexion entre les différents éléments d'interface

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Architecture d'une application Qt complète

### 1.1 Pourquoi utiliser QMainWindow ?

`QMainWindow` est la fondation de la plupart des applications de bureau professionnelles. Contrairement à une simple `QWidget`, `QMainWindow` offre une **structure organisée** qui correspond aux attentes des utilisateurs d'applications desktop.

**Avantages de QMainWindow :**
- **Structure prédéfinie** : zones logiquement organisées
- **Gestion automatique** des barres et menus
- **Cohérence visuelle** avec les standards de l'OS
- **Extensibilité** pour des fonctionnalités avancées (docking, MDI)

### 1.2 Comprendre les 4 zones principales

Toute application professionnelle s'organise autour de **4 zones fondamentales** :

#### 🎯 **Zone 1 : La barre de menus (MenuBar)**
- **Rôle** : Accès à toutes les fonctionnalités de l'application
- **Position** : En haut de la fenêtre (sauf macOS où elle est dans la barre système)
- **Contenu** : Menus déroulants organisés par catégorie (Fichier, Édition, Affichage...)

#### 🎯 **Zone 2 : La barre d'outils (ToolBar)**
- **Rôle** : Accès rapide aux actions les plus fréquentes
- **Position** : Sous la barre de menus (peut être déplacée)
- **Contenu** : Boutons avec icônes, widgets de saisie rapide

#### 🎯 **Zone 3 : Le widget central (CentralWidget)**
- **Rôle** : Zone de travail principale de l'application
- **Position** : Centre de la fenêtre (zone la plus importante)
- **Contenu** : Le contenu métier de votre application (éditeur, tableau, etc.)

#### 🎯 **Zone 4 : La barre de statut (StatusBar)**
- **Rôle** : Feedback et informations contextuelles
- **Position** : En bas de la fenêtre
- **Contenu** : Messages temporaires, indicateurs permanents, barres de progression

#### 📊 **Schéma de l'interface QMainWindow**

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

### 1.3 Exemple pratique minimal

Voici une application qui illustre cette architecture de base :

```python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Les 4 zones de QMainWindow")
        self.setGeometry(100, 100, 600, 400)
        
        # Zone 3 : Widget central (OBLIGATOIRE)
        self.setup_central_widget()
        
        # Zone 1 : Barre de menus (optionnelle mais recommandée)
        self.setup_menu_bar()
        
        # Zone 2 : Barre d'outils (optionnelle)
        self.setup_tool_bar()
        
        # Zone 4 : Barre de statut (optionnelle mais utile)
        self.setup_status_bar()
    
    def setup_central_widget(self) -> None:
        """Zone 3 : Le cœur de votre application"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.label = QLabel("👋 Bienvenue dans l'architecture Qt !")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button = QPushButton("Tester les interactions")
        self.button.clicked.connect(self.handle_button_click)
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
    
    def setup_menu_bar(self) -> None:
        """Zone 1 : Navigation principale"""
        if (menubar := self.menuBar()) is not None:
            file_menu = menubar.addMenu("&Fichier")
            file_menu.addAction("Nouveau").triggered.connect(self.handle_new_file)
            file_menu.addAction("Ouvrir").triggered.connect(self.handle_open_file)
    
    def setup_tool_bar(self) -> None:
        """Zone 2 : Accès rapide"""
        if (toolbar := self.addToolBar("Principal")) is not None:
            toolbar.addAction("Nouveau").triggered.connect(self.handle_toolbar_new)
    
    def setup_status_bar(self) -> None:
        """Zone 4 : Feedback utilisateur"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Application prête")
    
    def handle_button_click(self) -> None:
        """Exemple d'interaction entre les zones"""
        self.label.setText("🎯 Interaction détectée !")
        self.update_status("Bouton cliqué avec succès")
    
    def update_status(self, message: str) -> None:
        """Utilitaire pour mettre à jour le statut"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(message, 2000)
    
    def handle_new_file(self) -> None:
        """Gestionnaire pour nouveau fichier depuis le menu"""
        self.update_status("Nouveau fichier")
    
    def handle_open_file(self) -> None:
        """Gestionnaire pour ouvrir fichier depuis le menu"""
        self.update_status("Ouverture...")
    
    def handle_toolbar_new(self) -> None:
        """Gestionnaire pour nouveau fichier depuis la barre d'outils"""
        self.update_status("Action rapide")
```

**Points clés de cet exemple :**
- Chaque zone a un rôle spécifique et défini
- Le widget central est **obligatoire** (Qt l'exige)
- Les autres zones sont optionnelles mais fortement recommandées
- L'interaction entre les zones crée une expérience utilisateur cohérente

### 1.4 Cycle de vie d'une application Qt

```python
import sys
from PyQt6.QtWidgets import QApplication

def main() -> int:
    # 1. Création de l'application
    app = QApplication(sys.argv)
    
    # 2. Configuration globale (optionnel)
    app.setApplicationName("Mon App")
    app.setApplicationVersion("1.0")
    
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

## 2. Communication par signaux et slots

### 2.1 Comprendre le mécanisme fondamental

Les **signaux et slots** constituent le **cœur de la communication** dans Qt. C'est le mécanisme qui permet aux widgets de "parler" entre eux et avec votre code.

#### 🔄 **Qu'est-ce qu'un signal ?**
Un signal est une **notification émise par un widget** quand quelque chose se produit :
- Clic sur un bouton
- Modification de texte dans un champ
- Sélection d'un élément dans une liste
- Changement de valeur d'un slider

#### 🎯 **Qu'est-ce qu'un slot ?**
Un slot est une **fonction qui reçoit et traite** un signal :
- N'importe quelle fonction Python peut être un slot
- Les widgets Qt ont leurs propres slots intégrés
- Vous pouvez créer vos propres slots personnalisés

#### 🔗 **La connexion signal-slot**
```
[Widget] ---> Signal ---> Slot [Fonction]
[Bouton] ---> clicked ---> ma_fonction()
```

### 2.2 Premier exemple : simple connexion

Commençons par le plus simple : connecter un bouton à une fonction qui affiche un message.

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mon Application")
        
        # Créer un bouton
        button = QPushButton("Appuyez sur moi !")
            
        # CONNEXION : signal 'clicked' -> slot 'handle_click'
        button.clicked.connect(self.handle_click) 
        
        self.setCentralWidget(button)
    
    def handle_click(self) -> None:
        """Slot personnalisé qui reçoit le signal clicked"""
        print("🎯 Bouton cliqué !") 

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
```

**Connexion signal-slot** : Le signal `clicked` du bouton est connecté à notre méthode `handle_click`
**Réaction** : Quand le bouton est cliqué, ce message s'affiche dans la console

**Ce qui se passe :**
1. L'utilisateur clique sur le bouton
2. Le bouton émet le signal `clicked`
3. Qt appelle automatiquement notre méthode `handle_click`
4. Notre code s'exécute en réponse au clic

### 2.3 Modifier l'interface en réponse aux signaux

Afficher dans la console c'est bien, mais **modifier l'interface** c'est mieux ! Voyons comment notre slot peut agir sur l'interface elle-même.

```python
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mon Application")
        
        # On garde une référence au bouton dans self
        self.button = QPushButton("Appuyez sur moi !") 
        self.button.clicked.connect(self.handle_click)
        
        self.setCentralWidget(self.button)
    
    def handle_click(self) -> None:
        """Slot qui modifie l'interface"""
        self.button.setText("Vous m'avez déjà cliqué !") 
        self.button.setEnabled(False)  # ③
        self.setWindowTitle("Application utilisée") 
```

**Référence importante** : On stocke le bouton dans `self.button` pour pouvoir le modifier plus tard
**Changer le texte** : On utilise `setText()` pour modifier le texte du bouton
**Désactiver le widget** : `setEnabled(False)` rend le bouton non-cliquable
**Modifier le titre** : On peut aussi changer le titre de la fenêtre

**🚨 Point important :** Pour pouvoir modifier un widget dans un slot, vous devez garder une référence vers ce widget (le stocker dans `self`).

### 2.4 Chaîner les signaux : réactions en cascade

Une fonctionnalité puissante de Qt est la possibilité de **chaîner les événements**. Un signal peut déclencher une action, qui elle-même déclenche d'autres événements.

```python
from random import choice

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mon Application")
        self.click_count = 0
        
        self.button = QPushButton("Cliquez-moi !")
        self.button.clicked.connect(self.handle_button_click)
        
        # Signal de la fenêtre elle-même
        self.windowTitleChanged.connect(self.handle_title_change) 
        
        self.setCentralWidget(self.button)
    
    def handle_button_click(self) -> None:
        """Premier maillon de la chaîne"""
        self.click_count += 1
        
        # Changer le titre déclenche automatiquement windowTitleChanged
        titles = ["Première fois", "Deuxième fois", "Encore ?", "Stop !"]
        if self.click_count <= len(titles):
            new_title = titles[self.click_count - 1]
            self.setWindowTitle(new_title) 
    
    def handle_title_change(self, new_title: str) -> None:
        """Deuxième maillon : réagit au changement de titre"""
        print(f"📝 Titre changé : {new_title}") 
        
        if new_title == "Stop !":
            self.button.setText("Fini !")
            self.button.setEnabled(False) 
```

**Signal de fenêtre** : `windowTitleChanged` est émis quand le titre change
**Déclencheur** : Changer le titre avec `setWindowTitle()` émet automatiquement le signal
**Réaction automatique** : Notre slot reçoit le nouveau titre
**Action finale** : Si le titre est "Stop !", on désactive le bouton

**🔑 Concept clé :** Les signaux permettent de créer des **réactions en chaîne** sans que les composants aient besoin de se connaître directement. Le bouton ne sait pas qu'il va désactiver quelque chose, mais les règles que vous définissez créent ces interactions.

### 2.5 Signal important à retenir

**⚠️ Les signaux ne se déclenchent que lors de vrais changements**

Le signal `windowTitleChanged` n'est émis que si le nouveau titre est **différent** du précédent. Si vous définissez le même titre plusieurs fois, le signal ne sera émis qu'une seule fois.

```python
def test_signal_behavior(self) -> None:
    """Démontre quand les signaux se déclenchent"""
    self.setWindowTitle("Test")      # Signal émis
    self.setWindowTitle("Test")      # Signal PAS émis (même titre)
    self.setWindowTitle("Nouveau")   # Signal émis (titre différent)
```

**💡 Conseil :** Toujours vérifier les conditions de déclenchement des signaux dans la documentation pour éviter les surprises !

### 2.6 Signaux avec données : recevoir des informations

Certains signaux **transmettent des informations** utiles à vos slots. Le signal `clicked` d'un bouton checkable est un parfait exemple.

```python
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Bouton à bascule")
        
        self.button = QPushButton("Mode jour")
        self.button.setCheckable(True) 
        
        # Le signal clicked envoie l'état (True/False)
        self.button.clicked.connect(self.handle_toggle) 
        
        self.setCentralWidget(self.button)
    
    def handle_toggle(self, checked: bool) -> None: 
        """Slot qui reçoit l'état du bouton"""
        if checked:
            self.button.setText("Mode nuit") 
            self.setStyleSheet("background-color: #2c3e50; color: white;")
        else:
            self.button.setText("Mode jour")
            self.setStyleSheet("background-color: white; color: black;")
```

**Bouton basculant** : `setCheckable(True)` permet au bouton d'avoir deux états
**Connexion avec données** : Le signal `clicked` envoie automatiquement l'état `True`/`False`
**Réception** : Notre slot reçoit la donnée dans le paramètre `checked`
**Adaptation** : L'interface s'adapte selon l'état reçu

**💡 Point important :** Vous devez connaître le **type de données** que chaque signal envoie. La documentation Qt indique toujours ces informations.

### 2.7 Connecter directement les widgets entre eux

Une fonctionnalité puissante de Qt : vous pouvez connecter les widgets **directement entre eux**, sans passer par une fonction Python !

```python
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Connexion directe")
        
        # Créer les widgets
        self.label = QLabel("Tapez quelque chose...") 
        self.input = QLineEdit()
        
        # Connexion DIRECTE : pas de fonction Python !
        self.input.textChanged.connect(self.label.setText) 
        
        # Organisation dans un layout (voir chapitre suivant)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
```

**Widget de destination** : Le label affichera le texte
**Connexion magique** : `textChanged` envoie le texte directement à `setText`

**🎯 Ce qui se passe :**
- Vous tapez dans le champ de saisie
- Le signal `textChanged` est émis avec le nouveau texte
- Qt appelle directement `setText()` sur le label
- Le texte apparaît instantanément dans le label

**Avantages des connexions directes :**
- **Simplicité** : Pas besoin d'écrire de fonction intermédiaire
- **Performance** : Exécution plus rapide (pas de passage par Python)
- **Lisibilité** : L'intention est claire et directe

### 2.8 Quand utiliser chaque approche ?

#### 🔗 **Connexion directe** (widget vers widget)
Utilisez quand :
- Les données correspondent exactement (même type)
- Aucune logique métier n'est nécessaire
- L'action est simple et directe

```python
# Exemples de connexions directes
slider.valueChanged.connect(progress_bar.setValue)
line_edit.textChanged.connect(label.setText)
checkbox.toggled.connect(widget.setEnabled)
```

#### 🐍 **Slot Python personnalisé**
Utilisez quand :
- Vous devez transformer les données
- Une logique métier est requise
- Plusieurs actions doivent se produire
- Vous voulez déboguer ou journaliser

```python
def handle_value_change(self, value: int) -> None:
    """Slot avec logique métier"""
    # Transformation des données
    percentage = value / 100
    
    # Logique conditionnelle
    if percentage > 0.8:
        self.warning_label.setText("⚠️ Valeur élevée !")
    
    # Actions multiples
    self.progress_bar.setValue(value)
    self.update_status(f"Valeur : {percentage:.1%}")
```

---

## 3. Les widgets de base essentiels

### 3.1 Comprendre les widgets Qt

Dans Qt, un **widget** est le nom donné à un composant d'interface utilisateur avec lequel l'utilisateur peut interagir. Les interfaces utilisateur sont composées de **multiples widgets**, organisés dans la fenêtre. Qt propose une large sélection de widgets disponibles, et vous permet même de créer vos propres widgets personnalisés.

![Exemple de widgets](assets/example_widgets.png)

Les widgets sont les **briques fondamentales** de votre interface :
- Ils **reçoivent** les interactions utilisateur (clics, saisie, sélection)
- Ils **affichent** des informations (texte, images, données)
- Ils **émettent des signaux** quand leur état change
- Ils peuvent être **stylés et personnalisés** avec CSS

### 3.2 Les 5 widgets que vous utiliserez tout le temps

Dans 80% des cas, vous utiliserez ces **5 widgets fondamentaux**. Maîtrisez-les d'abord !

#### 📝 **QLineEdit** - La saisie de texte
**Utilisation** : Nom d'utilisateur, email, recherche, toute saisie sur une ligne

#### 🎯 **QPushButton** - L'action utilisateur  
**Utilisation** : Valider, annuler, envoyer, toute action à déclencher

#### 📋 **QLabel** - L'affichage d'informations
**Utilisation** : Titre, description, résultat, feedback utilisateur

#### ☑️ **QCheckBox** - Les options on/off
**Utilisation** : Préférences, options facultatives, activation/désactivation

#### 📝 **QComboBox** - Le choix dans une liste
**Utilisation** : Pays, catégories, options prédéfinies

### 3.3 QLineEdit - La saisie de texte par excellence

`QLineEdit` est le widget **incontournable** pour toute saisie de texte sur une ligne. C'est probablement le widget que vous utiliserez le plus dans vos formulaires et interfaces de saisie.

#### 🎯 **Cas d'usage typiques**
- **Formulaires de connexion** : nom d'utilisateur, email, mot de passe
- **Champs de recherche** : barre de recherche dans une application
- **Saisie de données courtes** : nom, téléphone, adresse, etc.
- **Champs de configuration** : paramètres, préférences utilisateur

#### 📊 **Les signaux essentiels à comprendre**

QLineEdit propose plusieurs signaux, mais deux sont particulièrement importants à bien distinguer :

**`textChanged(str)`** : Se déclenche à **chaque caractère** tapé ou modifié
```python
# Exemple : compteur de caractères en temps réel
self.input = QLineEdit()
self.input.textChanged.connect(self.count_characters)

def count_characters(self, text: str) -> None:
    """Appelé à chaque frappe de touche"""
    self.status_label.setText(f"Caractères : {len(text)}")
    print("Texte changé...")
    print(text)
```

**`textEdited(str)`** : Se déclenche uniquement lors de **modifications par l'utilisateur**
```python
# Exemple : distinction entre saisie utilisateur et modification programmatique
self.input.textEdited.connect(self.user_typed)

def user_typed(self, text: str) -> None:
    """Appelé seulement quand l'utilisateur tape"""
    print("Texte édité par l'utilisateur...")
    print(text)
    # Ce signal ne se déclenche PAS si on fait self.input.setText("nouveau")
```

**🔑 Différence importante :** `textChanged` se déclenche pour **tous** les changements (utilisateur + code), tandis que `textEdited` ne se déclenche que pour les **modifications utilisateur**. Cette distinction est cruciale pour éviter les boucles infinies !

**`editingFinished()`** : Se déclenche quand l'utilisateur **termine** la saisie
```python
# Exemple : validation du format email à la fin de la saisie
self.email_input.editingFinished.connect(self.validate_email)

def validate_email(self) -> None:
    """Validation déclenchée par Enter ou perte de focus"""
    email = self.email_input.text()
    if "@" in email and "." in email and len(email) > 5:
        self.result_label.setText("✅ Email valide")
    else:
        self.result_label.setText("❌ Format email invalide")
```

#### 🔧 **Configuration pratique des QLineEdit**

```python
# Création et configuration d'un champ de saisie
line_edit = QLineEdit()

# Texte d'aide qui disparaît à la saisie
line_edit.setPlaceholderText("Entrez votre email...") 

# Limite de caractères
line_edit.setMaxLength(50) 

# Mode d'affichage (normal, mot de passe, etc.)
line_edit.setEchoMode(QLineEdit.EchoMode.Password) 

# Masque de saisie pour validation automatique
line_edit.setInputMask('000.000.000.000;_') 
```

**Placeholder** : Texte d'aide affiché quand le champ est vide
**Longueur maximale** : Limite automatique du nombre de caractères
**Mode d'écho** : `Normal`, `Password`, `NoEcho`, `PasswordEchoOnEdit`
**Masque de saisie** : Format imposé (ici pour une adresse IPv4)

#### 💡 **Exemple pratique : validation de saisie en temps réel**

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget
import sys

class FormWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Validation en temps réel")
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Interface avec validation automatique"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Champ email avec validation
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("votre.email@exemple.com")
        self.email_input.textChanged.connect(self.validate_email_realtime) 
        
        # Label de feedback
        self.feedback_label = QLabel("Tapez votre email")
        
        layout.addWidget(QLabel("Email :"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.feedback_label)
    
    def validate_email_realtime(self, text: str) -> None:
        """Validation en temps réel à chaque caractère"""
        if len(text) == 0:
            self.feedback_label.setText("Tapez votre email")
            self.feedback_label.setStyleSheet("color: gray;")
        elif "@" in text and "." in text.split("@")[-1]:
            self.feedback_label.setText("✅ Format email valide")
            self.feedback_label.setStyleSheet("color: green;")
        else:
            self.feedback_label.setText("❌ Format email incomplet")
            self.feedback_label.setStyleSheet("color: orange;")
```

**Validation temps réel** : À chaque caractère, on vérifie et on donne un retour visuel

**🎯 Avantages de cette approche :**
- **Feedback immédiat** : L'utilisateur sait tout de suite si sa saisie est correcte
- **Expérience utilisateur** : Pas besoin d'attendre la validation finale
- **Guidage** : L'utilisateur comprend ce qui est attendu

### 3.4 QWidget - Le conteneur universel

Il y a un widget dans nos démonstrations précédentes que vous pourriez ne pas avoir remarqué : **QWidget**. Nous l'avons utilisé pour créer une fenêtre vide dans notre premier exemple, mais QWidget a un rôle **bien plus important** que cela.

#### 🎯 **QWidget comme conteneur**

QWidget peut être utilisé comme **conteneur pour d'autres widgets**, combiné avec des **Layouts**, pour construire des fenêtres ou des widgets composés. C'est la base de l'organisation de vos interfaces complexes.

```python
# Dans nos exemples précédents, nous utilisions souvent :
central_widget = QWidget() 
self.setCentralWidget(central_widget)

layout = QVBoxLayout() 
central_widget.setLayout(layout)

# Puis nous ajoutions d'autres widgets au layout
layout.addWidget(self.email_input)
layout.addWidget(self.feedback_label)
```

**Widget conteneur** : QWidget sert de "boîte" pour organiser d'autres widgets
**Layout associé** : Le layout gère l'arrangement spatial des widgets enfants

#### 🔑 **Rôles de QWidget**

**Comme widget racine :**
- Fenêtre simple sans les barres de QMainWindow
- Base pour des dialog boxes
- Prototypage rapide d'interfaces

**Comme conteneur organisateur :**
- Grouper logiquement des widgets liés
- Créer des sections dans une interface complexe
- Faciliter la réutilisation de groupes de composants

**Comme base de widgets personnalisés :**
- Hériter de QWidget pour créer vos propres composants
- Encapsuler la logique métier avec l'interface
- Réutiliser des interfaces complexes dans plusieurs endroits

#### 💡 **Exemple : créer un widget de formulaire réutilisable**

```python
from PyQt6.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton

class UserFormWidget(QWidget):
    """Widget personnalisé réutilisable pour saisie utilisateur"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Organisation des widgets dans un formulaire"""
        layout = QVBoxLayout()
        self.setLayout(layout) 
        
        # Widgets du formulaire
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Votre nom complet")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("votre@email.com")
        
        self.submit_btn = QPushButton("Envoyer")
        
        # Organisation
        layout.addWidget(QLabel("Nom :"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Email :"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.submit_btn)
    
    def get_user_data(self) -> dict[str, str]:
        """Récupère les données du formulaire"""
        return {
            "name": self.name_input.text(),
            "email": self.email_input.text()
        }

# Utilisation dans une fenêtre principale
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Notre widget personnalisé devient le widget central
        self.user_form = UserFormWidget() 
        self.setCentralWidget(self.user_form)
        
        # Connexion du signal
        self.user_form.submit_btn.clicked.connect(self.handle_submit)
    
    def handle_submit(self) -> None:
        """Traite les données du formulaire"""
        data = self.user_form.get_user_data()
        print(f"Données reçues : {data}")
```

**Layout sur QWidget** : Chaque QWidget peut avoir son propre layout
**Réutilisation** : Notre widget personnalisé est utilisé comme n'importe quel autre widget

**🎯 Gardez QWidget à l'esprit** : vous le verrez partout dans Qt ! C'est la classe de base de tous les widgets visuels, et comprendre son rôle de conteneur est essentiel pour organiser des interfaces complexes.

### 3.5 QComboBox - Choisir dans une liste

`QComboBox` est parfait quand l'utilisateur doit choisir **une option parmi plusieurs** prédéfinies.

#### 🎯 **Cas d'usage typiques**
- Sélection de pays, région, ville
- Choix de catégorie ou type
- Options de configuration (thème, langue, etc.)

#### 🔧 **Utilisation de base**
```python
combo = QComboBox()

# Ajouter les options
options = ["Option 1", "Option 2", "Option 3"]
combo.addItems(options) 

# Définir la sélection par défaut  
combo.setCurrentText("Option 2") 
```

**Ajouter les choix** : `addItems()` prend une liste de chaînes
**Sélection initiale** : `setCurrentText()` définit l'option affichée au début

#### 📊 **Le signal principal**

**`currentTextChanged(str)`** : Se déclenche quand l'utilisateur sélectionne une nouvelle option

```python
# Exemple : adapter l'interface selon le choix
combo.currentTextChanged.connect(self.handle_selection)

def handle_selection(self, selected_text: str) -> None:
    if selected_text == "Mode Expert":
        self.show_advanced_options()
    else:
        self.hide_advanced_options()
```

### 3.6 QCheckBox - Les options à cocher

`QCheckBox` est idéal pour les **options binaires** : activé/désactivé, oui/non, inclure/exclure.

#### 🎯 **Cas d'usage typiques**
- Préférences utilisateur (notifications, sauvegarde auto, etc.)
- Options d'export (inclure images, format PDF, etc.)
- Conditions d'acceptation (CGV, newsletter, etc.)

#### 🔧 **Utilisation de base**
```python
checkbox = QCheckBox("Recevoir les notifications")
checkbox.setChecked(True)  # Coché par défaut
```

**État initial** : `setChecked(True/False)` définit si la case est cochée au départ

#### 📊 **Le signal essentiel**

**`toggled(bool)`** : Se déclenche à chaque changement d'état (coché/décoché)

```python
# Exemple : activer/désactiver d'autres widgets selon l'état
notifications_cb = QCheckBox("Activer les notifications")
notifications_cb.toggled.connect(self.handle_notifications)

def handle_notifications(self, enabled: bool) -> None:
    self.sound_option.setEnabled(enabled) 
    self.email_option.setEnabled(enabled)
```

**Cascade d'activation** : Une case peut activer/désactiver d'autres options

### 3.7 QPushButton et QLabel - Les compléments essentiels

#### 🎯 **QPushButton - Déclencher des actions**

Le bouton est le widget d'**action** par excellence :

```python
button = QPushButton("Valider")
button.clicked.connect(self.process_form) 
```

**Signal principal** : `clicked` se déclenche au clic (avec ou sans données selon le bouton)

**Variantes utiles :**
- `button.setCheckable(True)` : Bouton à bascule on/off
- `button.setDefault(True)` : Bouton par défaut (Enter l'active)
- `button.setEnabled(False)` : Bouton désactivé temporairement

#### 📋 **QLabel - Afficher des informations**

Le label sert à **informer l'utilisateur** :

```python
label = QLabel("Résultat du calcul")
label.setText("Nouveau texte")  # Changer le contenu
label.setWordWrap(True)  # Retour à la ligne automatique
```

**Mise à jour** : `setText()` change le contenu affiché
**Formatage** : Options pour améliorer l'affichage

### 3.8 Faire communiquer les widgets

La vraie puissance vient de l'**interaction entre widgets** :

```python
# Exemple : validation en temps réel
def setup_form_validation(self) -> None:
    self.email_input = QLineEdit()
    self.submit_button = QPushButton("S'inscrire")
    self.status_label = QLabel("Tapez votre email")
    
    # Le bouton n'est actif que si l'email est valide
    self.submit_button.setEnabled(False) 
    
    # À chaque changement, on vérifie et on met à jour
    self.email_input.textChanged.connect(self.check_email_validity) 

def check_email_validity(self, email: str) -> None:
    """Valide l'email et active/désactive le bouton"""
    is_valid = "@" in email and "." in email and len(email) > 5
    
    self.submit_button.setEnabled(is_valid) 
    
    if is_valid:
        self.status_label.setText("✅ Email valide")
    else:
        self.status_label.setText("❌ Email requis")
```

**État initial** : Bouton désactivé au départ
**Surveillance** : Chaque caractère tapé déclenche la validation  
**Réaction** : L'interface s'adapte automatiquement

**🔑 Concept clé :** Les widgets peuvent se contrôler mutuellement pour créer une expérience utilisateur cohérente et intuitive.

---

## 4. Les Actions Qt : le cœur de l'interface utilisateur

### 4.1 Le problème de la duplication

Avant de plonger dans les barres d'outils et les menus, nous devons comprendre un **problème fondamental** dans la création d'interfaces utilisateur : la **duplication**.

Imaginez que vous voulez ajouter une fonction "Sauvegarder" dans votre application. Où cette fonction devrait-elle être accessible ?

- **Dans le menu** "Fichier" → "Sauvegarder"
- **Dans la barre d'outils** avec un bouton et une icône disquette
- **Via un raccourci clavier** Ctrl+S
- **Dans un menu contextuel** clic-droit → "Sauvegarder"

#### 🚨 **L'approche naïve (à éviter)**

Sans Qt, vous pourriez être tenté de créer chaque élément séparément :

```python
# ❌ Duplication du code - MAUVAISE approche
def setup_naive_interface(self) -> None:
    # Menu
    menu_save = self.file_menu.addAction("Sauvegarder")
    menu_save.triggered.connect(self.save_document)
    
    # Barre d'outils
    toolbar_save = QPushButton("Save")
    toolbar_save.clicked.connect(self.save_document)
    self.toolbar.addWidget(toolbar_save)
    
    # Raccourci clavier - code séparé !
    shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
    shortcut.activated.connect(self.save_document)
```

**Problèmes de cette approche :**
- **Code dupliqué** : Même fonction connectée 3 fois
- **Maintenance difficile** : Changer le comportement = modifier 3 endroits
- **Incohérence possible** : Risque d'oublier un élément
- **Pas de synchronisation** : Comment désactiver "Sauvegarder" partout à la fois ?

### 4.2 La solution Qt : QAction

Qt résout ce problème avec **QAction** - un concept brillant qui représente une **action abstraite** de l'utilisateur.

#### 🎯 **Qu'est-ce qu'une QAction ?**

Une `QAction` est un **objet unique** qui définit :
- **Le nom** de l'action ("Sauvegarder")
- **L'icône** associée (💾)
- **Le raccourci clavier** (Ctrl+S)
- **Le message d'aide** ("Sauvegarder le document")
- **La fonction à exécuter** (`save_document()`)
- **L'état** (activé/désactivé, coché/décoché)

#### ✅ **L'approche Qt (recommandée)**

```python
from PyQt6.QtGui import QAction, QKeySequence

def setup_smart_interface(self) -> None:
    # ✅ UNE SEULE définition pour TOUTE l'interface
    self.save_action = QAction("&Sauvegarder", self) 
    self.save_action.setShortcut("Ctrl+S")  # ②
    self.save_action.setStatusTip("Sauvegarder le document")  # ③
    self.save_action.triggered.connect(self.save_document)  # ④
    
    # Maintenant on peut utiliser cette action PARTOUT :
    self.file_menu.addAction(self.save_action)  # Menu
    self.toolbar.addAction(self.save_action)    # Barre d'outils
    # Le raccourci est automatiquement géré !
```

**Parent requis** : Notez que nous passons `self` comme parent - QAction a besoin d'un objet parent
**Raccourci intégré** : Le raccourci fonctionne même si l'action n'est affichée nulle part
**Message d'aide** : Sera affiché dans la barre de statut automatiquement
**Connexion unique** : Une seule connexion signal-slot pour toute l'interface

### 4.3 Exemple pratique complet

Voyons comment créer une application avec plusieurs actions synchronisées :

```python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QLabel, QMainWindow, 
    QStatusBar, QToolBar, QVBoxLayout, QWidget
)

class ActionDemoWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Démonstration des Actions Qt")
        self.setGeometry(100, 100, 800, 600)
        
        # Widget central simple
        self.setup_central_widget()
        
        # Actions AVANT les menus et barres d'outils
        self.create_actions() 
        
        # Ensuite on utilise ces actions partout
        self.setup_menu_bar()  # ②
        self.setup_tool_bar()  # ③
        self.setup_status_bar()  # ④
    
    def setup_central_widget(self) -> None:
        """Zone centrale simple pour la démonstration"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.content_label = QLabel("Utilisez les menus, barres d'outils ou raccourcis !")
        self.content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.content_label)
    
    def create_actions(self) -> None:
        """Création centralisée de toutes les actions"""
        # Action Nouveau
        self.new_action = QAction("&Nouveau", self)
        self.new_action.setShortcut("Ctrl+N") 
        self.new_action.setStatusTip("Créer un nouveau document")
        self.new_action.triggered.connect(self.new_document)
        
        # Action Ouvrir
        self.open_action = QAction("&Ouvrir", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Ouvrir un document existant")
        self.open_action.triggered.connect(self.open_document)
        
        # Action Sauvegarder
        self.save_action = QAction("&Sauvegarder", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Sauvegarder le document")
        self.save_action.triggered.connect(self.save_document)
        
        # État initial : désactiver Sauvegarder
        self.save_action.setEnabled(False) 
    
    def setup_menu_bar(self) -> None:
        """Les menus utilisent nos actions prédéfinies"""
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("&Fichier")
        file_menu.addAction(self.new_action)  
        file_menu.addAction(self.open_action) 
        file_menu.addSeparator()
        file_menu.addAction(self.save_action) 
    
    def setup_tool_bar(self) -> None:
        """La barre d'outils utilise les mêmes actions"""
        toolbar = self.addToolBar("Principal")
        
        toolbar.addAction(self.new_action)  
        toolbar.addAction(self.open_action) 
        toolbar.addSeparator()
        toolbar.addAction(self.save_action) 
    
    def setup_status_bar(self) -> None:
        """Barre de statut pour voir les messages d'aide"""
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Prêt")
    
    # Gestionnaires d'actions
    def new_document(self) -> None:
        """Créer un nouveau document"""
        self.content_label.setText("📄 Nouveau document créé")
        self.save_action.setEnabled(True) 
        self.statusBar().showMessage("Nouveau document créé", 2000)
    
    def open_document(self) -> None:
        """Ouvrir un document"""
        self.content_label.setText("📂 Document ouvert")
        self.save_action.setEnabled(True) 
        self.statusBar().showMessage("Document ouvert", 2000)
    
    def save_document(self) -> None:
        """Sauvegarder le document"""
        self.content_label.setText("💾 Document sauvegardé")
        self.statusBar().showMessage("Document sauvegardé avec succès", 2000)

def main() -> int:
    app = QApplication(sys.argv)
    window = ActionDemoWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

**Raccourcis automatiques** : Ctrl+N, Ctrl+O, Ctrl+S fonctionnent automatiquement
**État synchronisé** : Désactiver `save_action` la désactive partout
**Réutilisation totale** : Même action dans menu ET barre d'outils
**Messages d'aide** : Passer la souris sur les éléments affiche les conseils
**Synchronisation magique** : Activer la sauvegarde après "nouveau" ou "ouvrir"

### 4.4 Avantages des QAction

#### 🎯 **Centralisation**
- **Une définition** → utilisable partout
- **Une modification** → effet global
- **Cohérence garantie** → même comportement partout

#### 🔄 **Synchronisation automatique**
- Désactiver une action → tous les éléments se désactivent
- Changer le texte → mise à jour partout
- État (coché/décoché) → synchronisé automatiquement

#### 🚀 **Productivité**
- **Moins de code** → moins d'erreurs
- **Maintenance facile** → un seul endroit à modifier
- **Fonctionnalités avancées** → raccourcis, icônes, groupes d'actions

#### 💡 **Extensibilité**
- Ajouter l'action à de nouveaux endroits → une ligne de code
- Créer des menus contextuels → réutiliser les actions existantes
- Thèmes et styles → automatiquement appliqués

**🔑 Concept fondamental :** Les QAction sont la **fondation** de toute interface Qt professionnelle. Maîtrisez-les et vos interfaces seront cohérentes, maintenables et extensibles !

---

## 5. Barres d'outils (QToolBar)

### 5.1 Pourquoi utiliser des barres d'outils ?

Les **barres d'outils** sont l'un des éléments d'interface les plus courants dans les applications de bureau. Elles offrent un **accès rapide** aux fonctions les plus fréquemment utilisées.

#### 🎯 **Rôle des barres d'outils**
- **Accès immédiat** : Fonctions courantes en un clic
- **Efficacité** : Plus rapide que naviguer dans les menus
- **Visibilité** : Les actions importantes sont toujours visibles
- **Personnalisation** : L'utilisateur peut souvent les déplacer ou cacher

#### 📊 **Barres d'outils vs Menus**

| **Barres d'outils** | **Menus** |
|-------------------|---------|
| Actions **fréquentes** | **Toutes** les actions |
| Accès **immédiat** | Accès **organisé** |
| **Icônes** principales | **Texte** principal |
| Espace **limité** | Espace **extensible** |

### 5.2 Créer une barre d'outils simple

Commençons par créer une barre d'outils basique. Dans Qt, les barres d'outils sont créées avec la classe `QToolBar`.

```python
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar
import sys

class SimpleToolbarWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ma première barre d'outils")
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central simple
        self.label = QLabel("Cliquez sur un bouton de la barre d'outils")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        
        # Créer la barre d'outils
        self.create_toolbar() 
    
    def create_toolbar(self) -> None:
        """Création d'une barre d'outils basique"""
        toolbar = QToolBar("Ma barre d'outils") 
        self.addToolBar(toolbar) 
        
        # Pour l'instant, elle est vide mais visible
        # Regardez en haut de la fenêtre !

def main() -> int:
    app = QApplication(sys.argv)
    window = SimpleToolbarWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

**Méthode simple** : On crée et ajoute la barre d'outils à la fenêtre
**Nom de la barre** : "Ma barre d'outils" apparaîtra si on fait clic-droit
**Ajout automatique** : Qt place la barre d'outils en haut automatiquement

**💡 Astuce :** Faites un clic-droit sur la barre d'outils pour voir le menu contextuel qui permet de la cacher !

### 5.3 Ajouter des actions à la barre d'outils

Maintenant, rendons notre barre d'outils utile en y ajoutant des **actions** (nos QAction de la section précédente) :

```python
from PyQt6.QtGui import QAction

class ToolbarWithActionsWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Barre d'outils avec actions")
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central
        self.label = QLabel("Utilisez les boutons de la barre d'outils")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        
        # D'abord créer les actions, puis la barre d'outils
        self.create_actions()
        self.create_toolbar()
    
    def create_actions(self) -> None:
        """Créer nos actions réutilisables"""
        self.hello_action = QAction("Dire Bonjour", self)
        self.hello_action.setStatusTip("Affiche un message de salutation")
        self.hello_action.triggered.connect(self.say_hello) 
        
        self.goodbye_action = QAction("Dire Au revoir", self)
        self.goodbye_action.setStatusTip("Affiche un message d'adieu")
        self.goodbye_action.triggered.connect(self.say_goodbye) 
    
    def create_toolbar(self) -> None:
        """Ajouter nos actions à la barre d'outils"""
        toolbar = QToolBar("Actions")
        self.addToolBar(toolbar)
        
        # Ajouter nos actions à la barre d'outils
        toolbar.addAction(self.hello_action)   
        toolbar.addAction(self.goodbye_action) 

        # Ajouter un séparateur visuel
        toolbar.addSeparator() 
    
    # Gestionnaires d'actions
    def say_hello(self) -> None:
        """Réaction au bouton Bonjour"""
        self.label.setText("👋 Bonjour ! Comment allez-vous ?")
    
    def say_goodbye(self) -> None:
        """Réaction au bouton Au revoir"""
        self.label.setText("👋 Au revoir ! À bientôt !")
```

**Actions d'abord** : On crée les actions avant de les utiliser
**Connexion** : Chaque action est connectée à sa fonction
**Ajout facile** : `toolbar.addAction()` ajoute l'action comme bouton
**Séparateur** : `addSeparator()` crée une ligne de séparation visuelle

### 5.4 Actions basculantes (checkable)

Certaines actions ne sont pas juste des "clics" mais des **états** qu'on peut activer/désactiver. Voici comment créer des boutons à bascule :

```python
def create_toggle_actions(self) -> None:
    """Actions avec état on/off"""
    # Action basculante
    self.night_mode_action = QAction("Mode Nuit", self)
    self.night_mode_action.setCheckable(True) 
    self.night_mode_action.setChecked(False)  
    self.night_mode_action.toggled.connect(self.toggle_night_mode) 

def create_toolbar_with_toggles(self) -> None:
    """Barre d'outils avec boutons basculants"""
    toolbar = QToolBar("Modes")
    self.addToolBar(toolbar)
    
    toolbar.addAction(self.night_mode_action)

def toggle_night_mode(self, enabled: bool) -> None:
    """Basculer entre mode jour/nuit"""
    if enabled:
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")
        self.label.setText("🌙 Mode nuit activé")
    else:
        self.setStyleSheet("")  # Style par défaut
        self.label.setText("☀️ Mode jour activé")
```

**Action basculante** : `setCheckable(True)` permet l'état on/off
**État initial** : `setChecked(False)` définit l'état de départ
**Signal spécial** : `toggled` reçoit l'état True/False

### 5.5 Ajouter des icônes

Les icônes rendent les barres d'outils plus **professionnelles** et **intuitives**. Voici comment en ajouter :

```python
from PyQt6.QtGui import QIcon

def create_actions_with_icons(self) -> None:
    """Actions avec icônes"""
    # Action Nouveau avec icône
    self.new_action = QAction("Nouveau", self)
    # Utilisation d'icônes du système (disponibles partout)
    self.new_action.setIcon(self.style().standardIcon(
        self.style().StandardPixmap.SP_FileIcon)) 
    self.new_action.triggered.connect(self.new_document)
    
    # Action Sauvegarder
    self.save_action = QAction("Sauvegarder", self)
    self.save_action.setIcon(self.style().standardIcon(
        self.style().StandardPixmap.SP_DialogSaveButton)) 
    self.save_action.triggered.connect(self.save_document)

def configure_toolbar_appearance(self) -> None:
    """Configurer l'apparence de la barre d'outils"""
    toolbar = QToolBar("Fichier")
    self.addToolBar(toolbar)
    
    # Style des boutons : icône + texte sous l'icône
    toolbar.setToolButtonStyle(
        Qt.ToolButtonStyle.ToolButtonTextUnderIcon) 
    
    # Taille des icônes
    from PyQt6.QtCore import QSize
    toolbar.setIconSize(QSize(24, 24)) 
    
    # Ajouter nos actions avec icônes
    toolbar.addAction(self.new_action)
    toolbar.addAction(self.save_action)
```

**Icônes système** : `standardIcon()` utilise les icônes de l'OS
**Style des boutons** : Texte sous, à côté, ou seulement icône
**Taille personnalisée** : `setIconSize()` pour ajuster la taille

#### 📊 **Options de style des boutons**

| Style | Description | Quand utiliser |
|-------|-------------|----------------|
| `ToolButtonIconOnly` | Icône seulement | Espace limité, icônes évidentes |
| `ToolButtonTextOnly` | Texte seulement | Pas d'icônes disponibles |
| `ToolButtonTextBesideIcon` | Texte à côté | Barre large, clarté importante |
| `ToolButtonTextUnderIcon` | Texte en dessous | Style moderne, vertical |
| `ToolButtonFollowStyle` | Suit l'OS | Cohérence système (recommandé) |

### 5.6 Barres d'outils multiples et spécialisées

Pour des applications complexes, vous pouvez créer **plusieurs barres d'outils** spécialisées :

```python
def create_multiple_toolbars(self) -> None:
    """Plusieurs barres d'outils organisées par fonction"""
    # Barre d'outils Fichier
    file_toolbar = QToolBar("Fichier")
    self.addToolBar(file_toolbar)
    file_toolbar.addAction(self.new_action)
    file_toolbar.addAction(self.open_action)
    file_toolbar.addAction(self.save_action)
    
    # Barre d'outils Édition
    edit_toolbar = QToolBar("Édition")
    self.addToolBar(edit_toolbar) 
    edit_toolbar.addAction(self.copy_action)
    edit_toolbar.addAction(self.paste_action)
    
    # Barre d'outils avec widgets personnalisés
    search_toolbar = QToolBar("Recherche")
    self.addToolBar(search_toolbar)
    
    # Ajouter un widget QLineEdit directement
    from PyQt6.QtWidgets import QLineEdit, QPushButton
    search_field = QLineEdit()
    search_field.setPlaceholderText("Rechercher...")
    search_field.setMaximumWidth(200) 
    search_toolbar.addWidget(search_field) 
    
    search_button = QPushButton("🔍")
    search_button.clicked.connect(lambda: self.search(search_field.text()))
    search_toolbar.addWidget(search_button) 
```

**Ajout séquentiel** : Chaque `addToolBar()` ajoute sous la précédente
**Taille contrôlée** : `setMaximumWidth()` évite que le champ soit trop large
**Widgets normaux** : `addWidget()` peut ajouter n'importe quel widget
**Capture de texte** : Lambda pour passer le texte du champ à la fonction

### 5.7 Gestion avancée des barres d'outils

#### 🔧 **Contrôler la position et l'apparence**

```python
def setup_advanced_toolbar(self) -> None:
    """Configuration avancée des barres d'outils"""
    toolbar = QToolBar("Avancée")
    
    # Position spécifique
    self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar) 
    
    # Interdire le déplacement
    toolbar.setMovable(False) 
    
    # Interdire le flottement (détachement)
    toolbar.setFloatable(False) 
    
    # Style uniforme
    toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
```

**Position forcée** : Gauche, droite, haut, bas avec `ToolBarArea`
**Immobilisation** : `setMovable(False)` fixe la barre
**Pas de détachement** : `setFloatable(False)` empêche la fenêtre flottante

### 5.8 Bonnes pratiques pour les barres d'outils

#### ✅ **Recommandations**
- **Actions fréquentes seulement** : Pas plus de 8-10 boutons par barre
- **Groupement logique** : Utilisez des séparateurs pour grouper
- **Icônes cohérentes** : Même style et taille pour toute l'application
- **Ordre conventionnel** : Nouveau, Ouvrir, Sauvegarder (comme Office)

#### ❌ **À éviter**
- **Trop de boutons** : Surcharge cognitive
- **Actions rares** : Les réserver aux menus
- **Icônes floues** : Utilisez des icônes nettes et appropriées
- **Incohérence** : Mélanger styles et tailles d'icônes

**🔑 Concept clé :** Les barres d'outils sont des **raccourcis visuels**. Elles doivent rendre l'application plus rapide à utiliser, pas plus complexe !

---

## 6. Barres de menus (QMenuBar)

### 6.1 Pourquoi des menus ?

Les **menus** sont un autre élément standard des interfaces utilisateur. Ils constituent la **navigation principale** de votre application et permettent d'accéder à **toutes** les fonctionnalités disponibles.

#### 🎯 **Rôle des menus**
- **Accès exhaustif** : Toutes les fonctions de l'application sont accessibles
- **Organisation logique** : Regroupement par catégorie (Fichier, Édition, Aide...)
- **Découvrabilité** : L'utilisateur peut explorer les fonctionnalités
- **Standards établis** : Les utilisateurs savent où chercher quoi

#### 📊 **Comparaison Menus vs Barres d'outils**

Les menus et barres d'outils sont **complémentaires** :

| **Menus** | **Barres d'outils** |
|-----------|-------------------|
| **Toutes** les fonctions | Actions **fréquentes** |
| Accès **organisé** | Accès **immédiat** |
| **Texte** descriptif | **Icônes** visuelles |
| Toujours **accessibles** | Parfois **cachées** |

### 6.2 Créer une barre de menus simple

La barre de menus est automatiquement disponible dans `QMainWindow`. Voyons comment l'utiliser avec nos **QAction** :

```python
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import sys

class SimpleMenuWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ma première barre de menus")
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central simple
        self.label = QLabel("Utilisez les menus pour tester les actions")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        
        # Créer les actions d'abord
        self.create_actions()
        
        # Puis créer les menus
        self.create_menus()
    
    def create_actions(self) -> None:
        """Actions réutilisables"""
        self.new_action = QAction("&Nouveau", self)  &N pour Alt+N
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.setStatusTip("Créer un nouveau document")
        self.new_action.triggered.connect(self.new_document)
        
        self.exit_action = QAction("&Quitter", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Quitter l'application")
        self.exit_action.triggered.connect(self.close)  Action système
    
    def create_menus(self) -> None:
        """Création de la structure des menus"""
        # Récupérer la barre de menus
        menubar = self.menuBar() 
        
        # Créer le menu Fichier
        file_menu = menubar.addMenu("&Fichier")  

        # Ajouter nos actions au menu
        file_menu.addAction(self.new_action) 
        file_menu.addSeparator() 
        file_menu.addAction(self.exit_action)
    
    def new_document(self) -> None:
        """Gestionnaire pour nouveau document"""
        self.label.setText("📄 Nouveau document créé via le menu !")
```

**Mnémoniques** : `&Fichier` crée le raccourci Alt+F pour ouvrir le menu
**Action système** : `self.close` ferme automatiquement la fenêtre
**Récupération** : `menuBar()` donne accès à la barre de menus
**Ajout de menu** : `addMenu()` crée un nouveau menu déroulant
**Réutilisation** : Nos actions sont ajoutées au menu comme dans les barres d'outils
**Séparateur** : `addSeparator()` crée une ligne de séparation visuelle

**🔑 Concept important :** Les mêmes QAction que nous avons créées pour les barres d'outils peuvent être **directement réutilisées** dans les menus !

---

## 7. Barre de statut (QStatusBar)

### 6.1 Utilisation basique

```python
    def setup_status_bar(self) -> None:
        """Configure la barre de statut"""
        if (status := self.statusBar()) is None:
            return

        # Message permanent à gauche
        status.showMessage("Prêt")

        # Widgets permanents à droite
        self.create_status_widgets()

    def create_status_widgets(self) -> None:
        """Crée des widgets pour la barre de statut"""
        if (status := self.statusBar()) is None:
            return

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

    def update_status_position(self, line: int, column: int) -> None:
        """Met à jour la position dans la barre de statut"""
        self.position_label.setText(f"Ligne: {line}, Col: {column}")

    def show_progress(self, value: int, maximum: int = 100) -> None:
        """Affiche une barre de progression"""
        self.progress_bar.setMaximum(maximum)
        self.progress_bar.setValue(value)
        self.progress_bar.setVisible(value < maximum)
```

---

## 7. Menus contextuels

### 7.1 Menu contextuel basique

```python
    def setup_context_menu(self) -> None:
        """Configure les menus contextuels"""
        # Activer les menus contextuels
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position: QPoint) -> None:
        """Affiche le menu contextuel"""
        context_menu = QMenu(self)

        # Actions du menu contextuel
        if (copy_action := context_menu.addAction("Copier")) is None:
            return

        copy_action.triggered.connect(self.copy_content)

        if (paste_action := context_menu.addAction("Coller")) is None:
            return

        paste_action.triggered.connect(self.paste_content)

        context_menu.addSeparator()

        if (properties_action := context_menu.addAction("Propriétés...")) is None:
            return

        properties_action.triggered.connect(self.show_properties)

        # Afficher le menu à la position du clic
        context_menu.exec(self.mapToGlobal(position))

    def copy_content(self) -> None:
        """Gestionnaire copier"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Contenu copié", 2000)

    def paste_content(self) -> None:
        """Gestionnaire coller"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Contenu collé", 2000)

    def show_properties(self) -> None:
        """Affiche les propriétés"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Affichage des propriétés...", 2000)
```

### 7.2 Menus contextuels conditionnels

```python
    def show_advanced_context_menu(self, position: QPoint) -> None:
        """Menu contextuel avec logique conditionnelle"""
        context_menu = QMenu(self)

        # Vérifier s'il y a une sélection
        has_selection = self.has_text_selected()

        # Actions conditionnelles
        if (cut_action := context_menu.addAction("Couper")) is None:
            return

        cut_action.setEnabled(has_selection)

        if (copy_action := context_menu.addAction("Copier")) is None:
            return

        copy_action.setEnabled(has_selection)

        if (paste_action := context_menu.addAction("Coller")) is None:
            return

        paste_action.setEnabled(self.can_paste())

        context_menu.addSeparator()

        # Sous-menu
        if (format_menu := context_menu.addMenu("Format")) is None:
            return

        format_menu.addAction("Gras")
        format_menu.addAction("Italique")
        format_menu.addAction("Couleur...")

        context_menu.exec(self.mapToGlobal(position))

    def has_text_selected(self) -> bool:
        """Vérifie s'il y a du texte sélectionné"""
        # Logique selon votre widget
        return True  # Exemple

    def can_paste(self) -> bool:
        """Vérifie si le collage est possible"""
        # Vérifier le presse-papier
        return True  # Exemple
```

---


## 8. Interconnexion des éléments d'interface

### 8.1 Le pouvoir de la synchronisation

Maintenant que nous maîtrisons les **QAction**, voyons leur véritable puissance : créer des interfaces **parfaitement synchronisées** où tous les éléments travaillent ensemble harmonieusement.

#### 🎯 **Objectif : Interface cohérente**

Imaginez une application où :
- **Menu** "Fichier" → "Sauvegarder" est grisé quand rien à sauvegarder
- **Bouton** de la barre d'outils est également grisé automatiquement  
- **Raccourci** Ctrl+S ne fonctionne que quand approprié
- **Titre** de la fenêtre indique s'il y a des modifications
- **Barre de statut** donne un feedback instantané

**Sans QAction**, vous devriez gérer chaque élément séparément. **Avec QAction**, tout est automatiquement synchronisé !

### 8.2 Exemple complet : Éditeur de texte synchronisé

Voici un exemple qui montre la synchronisation complète de tous les éléments d'interface :

```python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPlainTextEdit, 
    QStatusBar, QToolBar, QMessageBox
)

class SynchronizedEditor(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Éditeur Synchronisé")
        self.setGeometry(100, 100, 800, 600)
        
        # État du document
        self.document_modified = False
        self.current_file = None
        
        # Interface
        self.setup_editor()       
        self.create_actions()     
        self.setup_menus()        
        self.setup_toolbar()      
        self.setup_status_bar()   
        
        # Synchronisation automatique
        self.connect_signals()    
    
    def setup_editor(self) -> None:
        """Zone d'édition principale"""
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Tapez votre texte ici...")
        self.setCentralWidget(self.editor)
    
    def create_actions(self) -> None:
        """Actions centralisées pour toute l'interface"""
        # Action Nouveau
        self.new_action = QAction("&Nouveau", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.setStatusTip("Créer un nouveau document")
        self.new_action.setIcon(self.style().standardIcon(
            self.style().StandardPixmap.SP_FileIcon))
        self.new_action.triggered.connect(self.new_document)
        
        # Action Sauvegarder
        self.save_action = QAction("&Sauvegarder", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Sauvegarder le document")
        self.save_action.setIcon(self.style().standardIcon(
            self.style().StandardPixmap.SP_DialogSaveButton))
        self.save_action.setEnabled(False) 
        self.save_action.triggered.connect(self.save_document)
        
        # Action Annuler
        self.undo_action = QAction("&Annuler", self)
        self.undo_action.setShortcut("Ctrl+Z")
        self.undo_action.setStatusTip("Annuler la dernière action")
        self.undo_action.setEnabled(False) 
        self.undo_action.triggered.connect(self.editor.undo)
    
    def setup_menus(self) -> None:
        """Menus utilisant nos actions"""
        menubar = self.menuBar()
        
        # Menu Fichier
        file_menu = menubar.addMenu("&Fichier")
        file_menu.addAction(self.new_action)  
        file_menu.addSeparator()
        file_menu.addAction(self.save_action) 
        
        # Menu Édition
        edit_menu = menubar.addMenu("&Édition")
        edit_menu.addAction(self.undo_action) 
    
    def setup_toolbar(self) -> None:
        """Barre d'outils avec les MÊMES actions"""
        toolbar = self.addToolBar("Principal")
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        toolbar.addAction(self.new_action)  
        toolbar.addAction(self.save_action) 
        toolbar.addSeparator()
        toolbar.addAction(self.undo_action) 
    
    def setup_status_bar(self) -> None:
        """Barre de statut pour feedback"""
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Prêt")
    
    def connect_signals(self) -> None:
        """Connexions pour synchronisation automatique"""
        # Détecter les modifications du texte
        self.editor.textChanged.connect(self.on_text_changed) 
        
        # Synchroniser l'état "Annuler" avec l'éditeur
        self.editor.undoAvailable.connect(self.undo_action.setEnabled) 
    
    # Gestionnaires synchronisés
    def on_text_changed(self) -> None:
        """Appelé à chaque modification du texte"""
        if not self.document_modified:
            self.document_modified = True
            self.save_action.setEnabled(True)  # Active partout !
            self.update_window_title()        
            self.statusBar().showMessage("Document modifié")
    
    def new_document(self) -> None:
        """Créer nouveau document"""
        if self.document_modified:
            # Demander confirmation si modifications non sauvées
            reply = QMessageBox.question(
                self, "Nouveau document",
                "Des modifications non sauvées seront perdues. Continuer ?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
        
        self.editor.clear()
        self.current_file = None
        self.document_modified = False
        self.save_action.setEnabled(False)  # Désactive partout !
        self.update_window_title()
        self.statusBar().showMessage("Nouveau document créé")
    
    def save_document(self) -> None:
        """Sauvegarder le document"""
        # Ici vous ajouteriez la logique de sauvegarde réelle
        self.document_modified = False
        self.save_action.setEnabled(False)  # Désactive partout !
        self.update_window_title()
        self.statusBar().showMessage("Document sauvegardé", 2000)
    
    def update_window_title(self) -> None:
        """Met à jour le titre de la fenêtre"""
        title = "Éditeur Synchronisé"
        if self.current_file:
            title += f" - {self.current_file}"
        if self.document_modified:
            title += " *"  # Astérisque pour modifications
        self.setWindowTitle(title)

def main() -> int:
    app = QApplication(sys.argv)
    window = SynchronizedEditor()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

**État centralisé** : `document_modified` contrôle l'état global
**Interface cohérente** : Éditeur + menus + barre d'outils + titre
**Actions réutilisées** : Même action dans menu ET barre d'outils
**Désactivation initiale** : Sauvegarder et Annuler désactivés au départ
**Réutilisation totale** : Une action définie, utilisée partout
**Synchronisation** : textChanged active la sauvegarde partout
**Connexion directe** : undoAvailable contrôle directement l'action
**Activation globale** : setEnabled(True) active dans menu ET barre d'outils
**Feedback visuel** : Titre mis à jour automatiquement
**Désactivation globale** : Après sauvegarde, désactivé partout
**Convention** : L'astérisque (*) indique les modifications non sauvées

### 8.3 Les bénéfices de la synchronisation

#### ✅ **Avantages pour le développeur**
- **Code centralisé** : Une seule logique pour toute l'interface
- **Maintenance simplifiée** : Modifier un endroit = effet global
- **Cohérence garantie** : Impossible d'oublier un élément
- **Débuggage facile** : Une seule fonction à vérifier

#### ✅ **Avantages pour l'utilisateur**
- **Interface prévisible** : Même état partout
- **Feedback cohérent** : Informations synchronisées
- **Expérience fluide** : Pas de boutons "morts" ou incohérents
- **Confiance** : L'application semble "bien conçue"

### 8.4 Patterns de synchronisation avancés

#### 🔄 **Actions interdépendantes**

Certaines actions dépendent de l'état d'autres :

```python
def setup_dependent_actions(self) -> None:
    """Actions qui dépendent les unes des autres"""
    # Copier nécessite une sélection
    self.copy_action = QAction("Copier", self)
    self.copy_action.setEnabled(False)
    
    # Coller nécessite du contenu dans le presse-papier
    self.paste_action = QAction("Coller", self)
    self.paste_action.setEnabled(False)
    
    # Surveiller la sélection
    self.editor.selectionChanged.connect(self.update_selection_actions) 
    
    # Surveiller le presse-papier
    from PyQt6.QtWidgets import QApplication
    clipboard = QApplication.clipboard()
    clipboard.dataChanged.connect(self.update_clipboard_actions) 

def update_selection_actions(self) -> None:
    """Active/désactive selon la sélection"""
    has_selection = bool(self.editor.textCursor().hasSelection())
    self.copy_action.setEnabled(has_selection) 

def update_clipboard_actions(self) -> None:
    """Active/désactive selon le presse-papier"""
    from PyQt6.QtWidgets import QApplication
    clipboard = QApplication.clipboard()
    has_text = bool(clipboard.text())
    self.paste_action.setEnabled(has_text) 
```

**Surveillance sélection** : selectionChanged détecte quand du texte est sélectionné
**Surveillance presse-papier** : dataChanged détecte les changements du presse-papier
**Activation conditionnelle** : Copier actif seulement si sélection
**État du système** : Coller actif seulement si le presse-papier contient du texte

**🔑 Principe fondamental :** Une interface bien conçue donne à l'utilisateur des **indices visuels constants** sur ce qui est possible ou non. Les QAction permettent de maintenir cette cohérence automatiquement !

---

### 8.2 Communication entre composants

```python
from PyQt6.QtCore import pyqtSignal

class MainWindow(QMainWindow):
    # Signal personnalisé
    status_changed = pyqtSignal(str, str)  # message, type
    
    def __init__(self) -> None:
        super().__init__()
        # Connecter le signal au gestionnaire
        self.status_changed.connect(self.update_status_display)
        
        self.setup_ui()
    
    def setup_interconnected_components(self) -> None:
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
    
    def toggle_toolbar(self, visible: bool) -> None:
        """Affiche/cache la barre d'outils"""
        toolbar = self.findChild(QToolBar)
        if toolbar:
            toolbar.setVisible(visible)
            status = "visible" if visible else "cachée"
            self.status_changed.emit(f"Barre d'outils {status}", "info")
    
    def toggle_statusbar(self, visible: bool) -> None:
        """Affiche/cache la barre de statut"""
        self.statusBar().setVisible(visible)
        if visible:
            self.status_changed.emit("Barre de statut restaurée", "info")
    
    def update_status_display(self, message: str, msg_type: str) -> None:
        """Met à jour l'affichage du statut"""
        if self.statusBar().isVisible():
            self.statusBar().showMessage(message, 3000)
```

---

## 9. Personnalisation avec CSS et styles

### 9.1 Pourquoi utiliser CSS dans Qt ?

Qt permet d'utiliser **CSS** pour personnaliser l'apparence de vos applications, exactement comme pour les pages web ! Cela vous donne un contrôle total sur :

- **Couleurs** : arrière-plans, textes, bordures
- **Typographie** : polices, tailles, styles
- **Espacement** : marges, padding, alignements
- **Effets visuels** : ombres, arrondis, transitions

#### 🎨 **Avantages du CSS dans Qt**
- **Séparation** : logique métier séparée de l'apparence
- **Cohérence** : styles uniformes dans toute l'application
- **Flexibilité** : changement d'apparence sans toucher au code
- **Thèmes** : plusieurs apparences pour la même application

### 9.2 Appliquer des styles de base

#### 🔧 **Syntaxe simple**
```python
# Appliquer un style à un widget spécifique
button = QPushButton("Mon bouton")
button.setStyleSheet("background-color: #3498db; color: white; padding: 10px;")

# Appliquer un style à toute l'application
self.setStyleSheet("""
    QPushButton {
        background-color: #3498db;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
""")
```

#### 📊 **Exemple pratique : moderniser une interface**
```python
class ModernWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.apply_modern_style() 
    
    def setup_ui(self) -> None:
        """Interface basique"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.title_label = QLabel("Mon Application Moderne")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Valider")
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)
    
    def apply_modern_style(self) -> None:
        """Transformation CSS moderne"""
        style = """
        QMainWindow {
            background-color: #f8f9fa;
        }
        
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            padding: 20px;
        }
        
        QLineEdit {
            padding: 12px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 14px;
        }
        
        QLineEdit:focus {
            border-color: #3498db;
        }
        
        QPushButton {
            background-color: #3498db;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
        }
        
        QPushButton:hover {
            background-color: #2980b9;
        }
        
        QPushButton:pressed {
            background-color: #21618c;
        }
        """
        self.setStyleSheet(style) 
```

**Organisation** : On sépare la création de l'interface de son style
**Application** : `setStyleSheet()` transforme instantanément l'apparence

### 9.3 Créer un système de thèmes

#### 🌓 **Thème clair/sombre dynamique**
```python
class ThemeManager:
    @staticmethod
    def get_light_theme() -> str:
        """Retourne le CSS du thème clair"""
        return """
        QMainWindow {
            background-color: #ffffff;
            color: #2c3e50;
        }
        
        QPushButton {
            background-color: #3498db;
            color: white;
        }
        
        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #bdc3c7;
        }
        """
    
    @staticmethod
    def get_dark_theme() -> str:
        """Retourne le CSS du thème sombre"""
        return """
        QMainWindow {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        
        QPushButton {
            background-color: #e74c3c;
            color: white;
        }
        
        QLineEdit {
            background-color: #34495e;
            border: 1px solid #7f8c8d;
            color: #ecf0f1;
        }
        """

class ThemableWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.setup_theme_menu() 
        self.apply_theme("light")  # Thème par défaut
    
    def setup_theme_menu(self) -> None:
        """Menu pour changer de thème"""
        menubar = self.menuBar()
        theme_menu = menubar.addMenu("Thème")
        
        light_action = theme_menu.addAction("Clair")
        light_action.triggered.connect(lambda: self.apply_theme("light"))
        
        dark_action = theme_menu.addAction("Sombre")
        dark_action.triggered.connect(lambda: self.apply_theme("dark"))
    
    def apply_theme(self, theme_name: str) -> None:
        """Applique le thème choisi"""
        if theme_name == "light":
            style = ThemeManager.get_light_theme() 
        else:
            style = ThemeManager.get_dark_theme()
        
        self.setStyleSheet(style)
        self.statusBar().showMessage(f"Thème {theme_name} appliqué", 2000)
```

**Menu intégré** : L'utilisateur peut changer de thème facilement
**Centralisation** : Les styles sont organisés dans une classe dédiée

### 9.4 CSS avancé : sélecteurs et états

#### 🎯 **Cibler précisément les widgets**
```python
advanced_style = """
/* Tous les boutons */
QPushButton {
    padding: 10px;
}

/* Boutons avec une classe CSS spécifique */
QPushButton[class="primary"] {
    background-color: #3498db;
}

QPushButton[class="danger"] {
    background-color: #e74c3c;
}

/* États des widgets */
QPushButton:hover {
    transform: scale(1.05);
}

QPushButton:disabled {
    background-color: #95a5a6;
    color: #7f8c8d;
}

/* Widgets imbriqués */
QGroupBox QPushButton {
    margin: 5px;
}
"""

# Utilisation avec des classes CSS
primary_btn = QPushButton("Action principale")
primary_btn.setProperty("class", "primary") 

danger_btn = QPushButton("Supprimer")
danger_btn.setProperty("class", "danger")
```

**Classes CSS** : `setProperty("class", "nom")` permet d'appliquer des styles spécifiques

**🔑 Points clés :**
- Le CSS de Qt suit les mêmes règles que le CSS web
- Les styles s'appliquent en cascade (parent vers enfant)
- Vous pouvez combiner plusieurs feuilles de styles
- Les pseudo-classes (`:hover`, `:pressed`) ajoutent de l'interactivité

---

## 10. Travaux pratiques

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

## 11. Points clés à retenir

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
