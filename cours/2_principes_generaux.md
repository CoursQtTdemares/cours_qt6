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
        button.clicked.connect(self.handle_click)  # ①
        
        self.setCentralWidget(button)
    
    def handle_click(self) -> None:
        """Slot personnalisé qui reçoit le signal clicked"""
        print("🎯 Bouton cliqué !")  # ②

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
```

① **Connexion signal-slot** : Le signal `clicked` du bouton est connecté à notre méthode `handle_click`
② **Réaction** : Quand le bouton est cliqué, ce message s'affiche dans la console

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
        self.button = QPushButton("Appuyez sur moi !")  # ①
        self.button.clicked.connect(self.handle_click)
        
        self.setCentralWidget(self.button)
    
    def handle_click(self) -> None:
        """Slot qui modifie l'interface"""
        self.button.setText("Vous m'avez déjà cliqué !")  # ②
        self.button.setEnabled(False)  # ③
        self.setWindowTitle("Application utilisée")  # ④
```

① **Référence importante** : On stocke le bouton dans `self.button` pour pouvoir le modifier plus tard
② **Changer le texte** : On utilise `setText()` pour modifier le texte du bouton
③ **Désactiver le widget** : `setEnabled(False)` rend le bouton non-cliquable
④ **Modifier le titre** : On peut aussi changer le titre de la fenêtre

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
        self.windowTitleChanged.connect(self.handle_title_change)  # ①
        
        self.setCentralWidget(self.button)
    
    def handle_button_click(self) -> None:
        """Premier maillon de la chaîne"""
        self.click_count += 1
        
        # Changer le titre déclenche automatiquement windowTitleChanged
        titles = ["Première fois", "Deuxième fois", "Encore ?", "Stop !"]
        if self.click_count <= len(titles):
            new_title = titles[self.click_count - 1]
            self.setWindowTitle(new_title)  # ②
    
    def handle_title_change(self, new_title: str) -> None:
        """Deuxième maillon : réagit au changement de titre"""
        print(f"📝 Titre changé : {new_title}")  # ③
        
        if new_title == "Stop !":
            self.button.setText("Fini !")
            self.button.setEnabled(False)  # ④
```

① **Signal de fenêtre** : `windowTitleChanged` est émis quand le titre change
② **Déclencheur** : Changer le titre avec `setWindowTitle()` émet automatiquement le signal
③ **Réaction automatique** : Notre slot reçoit le nouveau titre
④ **Action finale** : Si le titre est "Stop !", on désactive le bouton

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
        self.button.setCheckable(True)  # ①
        
        # Le signal clicked envoie l'état (True/False)
        self.button.clicked.connect(self.handle_toggle)  # ②
        
        self.setCentralWidget(self.button)
    
    def handle_toggle(self, checked: bool) -> None:  # ③
        """Slot qui reçoit l'état du bouton"""
        if checked:
            self.button.setText("Mode nuit")  # ④
            self.setStyleSheet("background-color: #2c3e50; color: white;")
        else:
            self.button.setText("Mode jour")
            self.setStyleSheet("background-color: white; color: black;")
```

① **Bouton basculant** : `setCheckable(True)` permet au bouton d'avoir deux états
② **Connexion avec données** : Le signal `clicked` envoie automatiquement l'état `True`/`False`
③ **Réception** : Notre slot reçoit la donnée dans le paramètre `checked`
④ **Adaptation** : L'interface s'adapte selon l'état reçu

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
        self.label = QLabel("Tapez quelque chose...")  # ①
        self.input = QLineEdit()
        
        # Connexion DIRECTE : pas de fonction Python !
        self.input.textChanged.connect(self.label.setText)  # ②
        
        # Organisation dans un layout (voir chapitre suivant)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
```

① **Widget de destination** : Le label affichera le texte
② **Connexion magique** : `textChanged` envoie le texte directement à `setText`

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
line_edit.setPlaceholderText("Entrez votre email...")  # ①

# Limite de caractères
line_edit.setMaxLength(50)  # ②

# Mode d'affichage (normal, mot de passe, etc.)
line_edit.setEchoMode(QLineEdit.EchoMode.Password)  # ③

# Masque de saisie pour validation automatique
line_edit.setInputMask('000.000.000.000;_')  # ④
```

① **Placeholder** : Texte d'aide affiché quand le champ est vide
② **Longueur maximale** : Limite automatique du nombre de caractères
③ **Mode d'écho** : `Normal`, `Password`, `NoEcho`, `PasswordEchoOnEdit`
④ **Masque de saisie** : Format imposé (ici pour une adresse IPv4)

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
        self.email_input.textChanged.connect(self.validate_email_realtime)  # ①
        
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

① **Validation temps réel** : À chaque caractère, on vérifie et on donne un retour visuel

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
central_widget = QWidget()  # ①
self.setCentralWidget(central_widget)

layout = QVBoxLayout()  # ②
central_widget.setLayout(layout)

# Puis nous ajoutions d'autres widgets au layout
layout.addWidget(self.email_input)
layout.addWidget(self.feedback_label)
```

① **Widget conteneur** : QWidget sert de "boîte" pour organiser d'autres widgets
② **Layout associé** : Le layout gère l'arrangement spatial des widgets enfants

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
        self.setLayout(layout)  # ①
        
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
        self.user_form = UserFormWidget()  # ②
        self.setCentralWidget(self.user_form)
        
        # Connexion du signal
        self.user_form.submit_btn.clicked.connect(self.handle_submit)
    
    def handle_submit(self) -> None:
        """Traite les données du formulaire"""
        data = self.user_form.get_user_data()
        print(f"Données reçues : {data}")
```

① **Layout sur QWidget** : Chaque QWidget peut avoir son propre layout
② **Réutilisation** : Notre widget personnalisé est utilisé comme n'importe quel autre widget

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
combo.addItems(options)  # ①

# Définir la sélection par défaut  
combo.setCurrentText("Option 2")  # ②
```

① **Ajouter les choix** : `addItems()` prend une liste de chaînes
② **Sélection initiale** : `setCurrentText()` définit l'option affichée au début

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
checkbox.setChecked(True)  # ① Coché par défaut
```

① **État initial** : `setChecked(True/False)` définit si la case est cochée au départ

#### 📊 **Le signal essentiel**

**`toggled(bool)`** : Se déclenche à chaque changement d'état (coché/décoché)

```python
# Exemple : activer/désactiver d'autres widgets selon l'état
notifications_cb = QCheckBox("Activer les notifications")
notifications_cb.toggled.connect(self.handle_notifications)

def handle_notifications(self, enabled: bool) -> None:
    self.sound_option.setEnabled(enabled)  # ②
    self.email_option.setEnabled(enabled)
```

② **Cascade d'activation** : Une case peut activer/désactiver d'autres options

### 3.7 QPushButton et QLabel - Les compléments essentiels

#### 🎯 **QPushButton - Déclencher des actions**

Le bouton est le widget d'**action** par excellence :

```python
button = QPushButton("Valider")
button.clicked.connect(self.process_form)  # ①
```

① **Signal principal** : `clicked` se déclenche au clic (avec ou sans données selon le bouton)

**Variantes utiles :**
- `button.setCheckable(True)` : Bouton à bascule on/off
- `button.setDefault(True)` : Bouton par défaut (Enter l'active)
- `button.setEnabled(False)` : Bouton désactivé temporairement

#### 📋 **QLabel - Afficher des informations**

Le label sert à **informer l'utilisateur** :

```python
label = QLabel("Résultat du calcul")
label.setText("Nouveau texte")  # ① Changer le contenu
label.setWordWrap(True)  # ② Retour à la ligne automatique
```

① **Mise à jour** : `setText()` change le contenu affiché
② **Formatage** : Options pour améliorer l'affichage

### 3.8 Faire communiquer les widgets

La vraie puissance vient de l'**interaction entre widgets** :

```python
# Exemple : validation en temps réel
def setup_form_validation(self) -> None:
    self.email_input = QLineEdit()
    self.submit_button = QPushButton("S'inscrire")
    self.status_label = QLabel("Tapez votre email")
    
    # Le bouton n'est actif que si l'email est valide
    self.submit_button.setEnabled(False)  # ①
    
    # À chaque changement, on vérifie et on met à jour
    self.email_input.textChanged.connect(self.check_email_validity)  # ②

def check_email_validity(self, email: str) -> None:
    """Valide l'email et active/désactive le bouton"""
    is_valid = "@" in email and "." in email and len(email) > 5
    
    self.submit_button.setEnabled(is_valid)  # ③
    
    if is_valid:
        self.status_label.setText("✅ Email valide")
    else:
        self.status_label.setText("❌ Email requis")
```

① **État initial** : Bouton désactivé au départ
② **Surveillance** : Chaque caractère tapé déclenche la validation  
③ **Réaction** : L'interface s'adapte automatiquement

**🔑 Concept clé :** Les widgets peuvent se contrôler mutuellement pour créer une expérience utilisateur cohérente et intuitive.

---

## 4. Barres de menus (QMenuBar)

### 4.1 Création d'une barre de menus

```python
    def setup_menu_bar(self) -> None:
        """Configure la barre de menus"""
        if (menubar := self.menuBar()) is None:
            return

        if (file_menu := menubar.addMenu("&Fichier")) is None:
            return

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

    def new_file(self) -> None:
        """Gestionnaire pour nouveau fichier"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Nouveau fichier créé", 2000)

    def open_file(self) -> None:
        """Gestionnaire pour ouvrir fichier"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Ouverture d'un fichier...", 2000)
```

### 4.2 Menus hiérarchiques et actions avancées

```python
    def setup_advanced_menus(self) -> None:
        """Exemples de menus avancés"""
        if (menubar := self.menuBar()) is None:
            return

        # Menu Édition avec sous-menus
        if (edit_menu := menubar.addMenu("&Édition")) is None:
            return

        if (insert_menu := edit_menu.addMenu("&Insérer")) is None:
            return

        if (image_menu := insert_menu.addAction("Image")) is None:
            return

        if (table_menu := insert_menu.addAction("Tableau")) is None:
            return

        # Sous-menu "Insérer"
        image_menu.triggered.connect(self.insert_image)
        table_menu.triggered.connect(self.insert_table)

        # Action avec case à cocher
        word_wrap_action = QAction("Retour à la &ligne", self)
        word_wrap_action.setCheckable(True)
        word_wrap_action.setChecked(True)
        word_wrap_action.toggled.connect(self.toggle_word_wrap)
        edit_menu.addAction(word_wrap_action)

        # Actions groupées (radio buttons)
        if (view_menu := menubar.addMenu("&Affichage")) is None:
            return

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

    def toggle_word_wrap(self, checked: bool) -> None:
        """Gestionnaire pour retour à la ligne"""
        mode = "activé" if checked else "désactivé"
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(f"Retour à la ligne {mode}", 2000)

    def change_view_mode(self, action: QAction) -> None:
        """Gestionnaire pour changement de vue"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(f"Mode d'affichage : {action.text()}", 2000)

    def insert_image(self) -> None:
        """Gestionnaire pour insérer une image"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Insération d'une image...", 2000)

    def insert_table(self) -> None:
        """Gestionnaire pour insérer un tableau"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Insération d'un tableau...", 2000)
```

---

## 5. Barres d'outils (QToolBar)

### 5.1 Création d'une barre d'outils basique

```python
    def setup_tool_bar(self) -> None:
        """Configure la barre d'outils"""
        if (toolbar := self.addToolBar("Principal")) is None:
            return

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

    def save_file(self) -> None:
        """Gestionnaire pour sauvegarder"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Fichier sauvegardé", 2000)
```

### 5.2 Barres d'outils multiples et personnalisées

```python
    def setup_multiple_toolbars(self) -> None:
        """Création de plusieurs barres d'outils"""
        # Barre d'outils principale
        if (main_toolbar := self.addToolBar("Principal")) is None:
            return

        main_toolbar.addAction("Nouveau")
        main_toolbar.addAction("Ouvrir")
        main_toolbar.addAction("Sauvegarder")

        # Barre d'outils de formatage
        if (format_toolbar := self.addToolBar("Formatage")) is None:
            return

        format_toolbar.addAction("Gras")
        format_toolbar.addAction("Italique")
        format_toolbar.addAction("Souligné")

        # Widget personnalisé dans la toolbar
        if (search_toolbar := self.addToolBar("Recherche")) is None:
            return

        search_field = QLineEdit()
        search_field.setPlaceholderText("Rechercher...")
        search_field.setMaximumWidth(200)
        search_toolbar.addWidget(search_field)

        search_button = QPushButton("Rechercher")
        search_button.clicked.connect(lambda: self.search(search_field.text()))
        search_toolbar.addWidget(search_button)

    def search(self, text: str) -> None:
        """Gestionnaire de recherche"""
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(f"Recherche : {text}", 2000)
```

---

## 6. Barre de statut (QStatusBar)

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

### 8.1 Synchronisation entre menus et barres d'outils

```python
def create_synchronized_actions(self) -> None:
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

def document_modified(self) -> None:
    """Appelé quand le document est modifié"""
    self.save_action.setEnabled(True)
    self.setWindowTitle("Mon Application* - Document modifié")

def save_document(self) -> None:
    """Sauvegarde le document"""
    # Logique de sauvegarde...
    self.save_action.setEnabled(False)
    self.setWindowTitle("Mon Application")
    self.statusBar().showMessage("Document sauvegardé", 2000)
```

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
        self.apply_modern_style()  # ①
    
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
        self.setStyleSheet(style)  # ②
```

① **Organisation** : On sépare la création de l'interface de son style
② **Application** : `setStyleSheet()` transforme instantanément l'apparence

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
        self.setup_theme_menu()  # ①
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
            style = ThemeManager.get_light_theme()  # ②
        else:
            style = ThemeManager.get_dark_theme()
        
        self.setStyleSheet(style)
        self.statusBar().showMessage(f"Thème {theme_name} appliqué", 2000)
```

① **Menu intégré** : L'utilisateur peut changer de thème facilement
② **Centralisation** : Les styles sont organisés dans une classe dédiée

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
primary_btn.setProperty("class", "primary")  # ①

danger_btn = QPushButton("Supprimer")
danger_btn.setProperty("class", "danger")
```

① **Classes CSS** : `setProperty("class", "nom")` permet d'appliquer des styles spécifiques

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
