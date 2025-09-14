# Chapitre 1 : Concepts généraux - PyQt6

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Comprendre ce qu'est Qt et le rôle du binding PyQt6
- Distinguer PyQt6 de ses alternatives (PyQt5, PySide6)
- Installer et configurer un environnement de développement PyQt6
- Utiliser VSCode pour développer des applications Qt
- Naviguer efficacement dans la documentation Qt/PyQt6
- Créer votre première application Qt fonctionnelle

## Durée estimée : 2h00
- **Théorie** : 1h
- **Travaux pratiques** : 1h

---

## 1. Introduction à Qt et PyQt6

### 1.1 Qu'est-ce que Qt ?

**Qt** est un framework de développement d'applications multiplateformes écrit en C++. Il permet de créer des interfaces graphiques natives qui s'exécutent sur Windows, macOS, Linux, et d'autres systèmes.

#### Points forts de Qt :
- **Multiplateforme** : "Write once, run anywhere"
- **Riche écosystème** : Widgets, graphiques, réseau, base de données, multimédia
- **Performance** : Applications natives compilées
- **Stabilité** : Framework mature utilisé par de nombreuses applications professionnelles
- **Internationalisation** : Support complet de l'Unicode et des traductions

#### Applications célèbres utilisant Qt :
- VLC Media Player
- Telegram Desktop
- OBS Studio
- KDE Plasma Desktop

### 1.2 Le concept de "Binding"

Un **binding** est une couche logicielle qui expose l'API d'une bibliothèque écrite dans un langage (ici C++) vers un autre langage (ici Python).

**PyQt6** utilise l'outil **SIP** (développé par Riverbank Computing) pour :
- Mapper automatiquement les classes C++ vers des classes Python
- Gérer la conversion des types (QString → str, QList → list)
- Exposer le système de signaux/slots en syntaxe Python
- Maintenir la gestion mémoire entre C++ et Python

### 1.3 Architecture Qt côté Python

#### L'objet QApplication
```python
import sys

from PyQt6.QtWidgets import QApplication, QLabel

# Un seul QApplication par processus
app = QApplication(sys.argv)

# ... création des widgets ...
label = QLabel("Hello, PyQt6!")
label.show()  # Un label par exemple

# Démarrage de la boucle d'événements
sys.exit(app.exec())
```

#### Modules principaux de PyQt6
- **QtCore** : Classes de base non graphiques
  - Boucle d'événements, timers, dates/heures
  - Gestion des fichiers et threads
  - Système de signaux/slots
  
- **QtGui** : Éléments graphiques bas niveau
  - Images, icônes, polices
  - Dessin (QPainter)
  - Gestion des couleurs et styles

- **QtWidgets** : Composants d'interface utilisateur
  - Fenêtres principales, boutons, champs de saisie
  - Layouts et organisation des composants
  - **Note** : C'est notre module principal pour ce cours

- **Autres modules** : QtNetwork, QtSql, QtMultimedia, QtSvg, etc.

#### Le modèle événementiel
Qt fonctionne avec une **boucle d'événements** qui :
- Capture les événements système (clics, saisie clavier, etc.)
- Les distribue aux widgets concernés
- Traite les signaux/slots de manière asynchrone

⚠️ **Important** : Une opération longue dans le thread GUI bloquera l'interface !

---

## 2. PyQt6 vs Alternatives

### 2.1 Tableau comparatif

| Aspect | PyQt6 | PyQt5 | PySide6 |
|--------|--------|--------|---------|
| **Version Qt** | Qt 6.x | Qt 5.x | Qt 6.x |
| **Mainteneur** | Riverbank Computing | Riverbank Computing | Qt Company |
| **Licence** | GPL v3 / Commercial | GPL v3 / Commercial | LGPL v3 / Commercial |
| **API** | Enums scopés | Enums non scopés | Enums scopés |
| **Méthode exec** | `app.exec()` | `app.exec_()` | `app.exec()` |
| **Maturité** | ✅ Stable | ✅ Très mature | ✅ Stable |

### 2.2 Recommandations d'usage

#### Choisir **PyQt6** si :
- Vous démarrez un nouveau projet
- Vous voulez les dernières fonctionnalités Qt 6
- La licence GPL convient à votre projet

#### Choisir **PyQt5** si :
- Vous maintenez un projet existant
- Vous avez des dépendances qui ne supportent que Qt 5
- Votre système d'exploitation est ancien

#### Choisir **PySide6** si :
- Vous développez une application commerciale propriétaire
- Vous voulez rester dans l'écosystème officiel Qt
- La licence LGPL est préférable

### 2.3 Différences syntaxiques principales

```python
# PyQt5 (ancien style)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

app = QApplication([])
label.setAlignment(Qt.AlignCenter)  # Enum non scopé
app.exec_()  # Ancienne méthode

# PyQt6 (style moderne)
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, PyQt6!")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Enum scopé
label.show()
app.exec()  # Nouvelle méthode

# PySide6 (style moderne)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, PySide6!")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.show()
app.exec()
```

---

## 3. Installation et configuration de l'environnement

### 3.1 Pré-requis

- **Python** : Version 3.8 à 3.12 (recommandé : 3.10+)
- **Système** : Windows, macOS, ou Linux
- **Gestionnaire de paquets** : `uv` (recommandé) ou `pip`

### 3.2 Installation avec UV (méthode recommandée)

#### Installation d'UV
Suivre les instructions officielles : https://docs.astral.sh/uv/getting-started/installation/

#### Création du projet
```bash
# Créer un nouveau dossier de projet
mkdir mon_projet_qt
cd mon_projet_qt

# Initialiser le projet avec uv
uv init

# Créer l'environnement virtuel
uv venv

# Installer PyQt6
uv add pyqt6

# Activer l'environnement (si nécessaire)
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
```

### 3.3 Installation alternative avec pip

```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# Mettre à jour pip
python -m pip install --upgrade pip wheel

# Installer PyQt6
pip install pyqt6
```

### 3.4 Vérification de l'installation

Créer un fichier `test_installation.py` :

```python
import sys

from PyQt6.QtWidgets import QApplication, QLabel


def test_pyqt() -> int:
    app = QApplication(sys.argv)

    label = QLabel("✅ PyQt6 fonctionne correctement !")
    label.resize(300, 100)
    label.show()

    print("🎉 Installation réussie !")
    return app.exec()


if __name__ == "__main__":
    sys.exit(test_pyqt())
```

```bash
uv run test_installation.py
```

Une fenêtre doit s'afficher avec le message de confirmation.

### 3.5 Dépannage courant

#### Linux : Erreur "xcb platform plugin"
```bash
sudo apt-get install qtbase5-dev-tools
# ou
sudo dnf install qt6-qtbase-devel
```

#### macOS : Conflits de frameworks
- Utiliser Python officiel de python.org
- Éviter les versions Python système ou Homebrew si problèmes

#### Windows : Problèmes d'affichage
- Vérifier que les pilotes graphiques sont à jour
- Éventuellement définir `QT_AUTO_SCREEN_SCALE_FACTOR=1`

---

## 4. Configuration de VSCode

### 4.1 Extensions recommandées

#### Extensions essentielles :
- **Python** (Microsoft) : Support Python de base
- **Pylance** : Analyse statique et IntelliSense
- **Black Formatter** ou **Ruff** : Formatage automatique du code

#### Extensions optionnelles :
- **Qt for Python** : Aperçu des fichiers .ui et .qml
- **Material Icon Theme** : Icônes pour meilleure navigation

### 4.2 Configuration du projet

#### Structure recommandée :
```
mon_projet_qt/
├── .venv/                 # Environnement virtuel
├── .vscode/
│   ├── settings.json      # Configuration VSCode
│   └── launch.json        # Configuration debug
├── src/                   # Dossier source
├── main.py                # Point d'entrée
├── pyproject.toml        # Configuration du projet
└── README.md
```

### 4.3 Application exemple pour le debug

Créer `main.py` :

```python
"""
Application PyQt6 exemple pour tester le debug VSCode
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Application PyQt6 - Debug Test")
        self.setGeometry(100, 100, 400, 300)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Composants
        self.label = QLabel("👋 Bienvenue dans PyQt6 !")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.counter = 0
        self.button = QPushButton("Cliquez-moi !")
        self.button.clicked.connect(self.on_button_click)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Barre de statut
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage("Application prête")

    def on_button_click(self) -> None:
        """Gestionnaire de clic - placez un breakpoint ici pour tester le debug"""
        self.counter += 1
        self.label.setText(f"🎯 Bouton cliqué {self.counter} fois !")
        if (status_bar := self.statusBar()) is not None:
            status_bar.showMessage(f"Compteur : {self.counter}")


def main() -> int:
    """Point d'entrée de l'application"""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
```

---

## 5. Documentation et ressources

### 5.1 Documentation officielle

#### PyQt6 (Riverbank Computing)
- **URL** : https://www.riverbankcomputing.com/static/Docs/PyQt6/
- **Contenu** : 
  - Index des modules et classes Python
  - Différences par rapport à PyQt6
  - Notes spécifiques sur les enums et flags

#### Qt 6 Documentation (C++)
- **URL** : https://doc.qt.io/qt-6/
- **Contenu** :
  - Référence complète de l'API C++
  - Exemples et tutoriels
  - Guides conceptuels

### 5.2 Ressources d'apprentissage

#### Tutoriels et exemples
- **Python GUIs** : https://www.pythonguis.com/
  - Tutoriels PyQt6 étape par étape
  - Exemples d'applications complètes
  
- **Exemples Qt Widgets** : https://doc.qt.io/qt-6/examples-widgets.html
  - Exemples C++ transposables en Python
  
- **Real Python** : https://realpython.com/python-pyqt-gui-calculator/
  - Tutoriels avancés avec bonnes pratiques

- **`livre` Create GUI Applications with PyQt6** :
    - [amazon](https://www.amazon.com/Create-Applications-Python-PyQt6-hands/dp/B0B1CK5ZZ1/ref=sr_1_1?crid=2BPD4NBMXEYMT&dib=eyJ2IjoiMSJ9.mksDhPpLEfeVfUAe_m9P3DTUOya1ToXSYlx7DEInsmFbGzOX2iOu2DKO6WVoPFZbvZve08DFUMp9T8mpEQuhHmWRTZnWThDZwPaDcd3p-ZoI09KXNutFQVpLy5CtXnNZyiVNWwZcAkFgwTq5i29ekWSCNziHMEYsxQcExprjRkyESGcZWyRc8bjoQInjnMLWlibbd4TsLVgGHlaGmMVp8FIBJBcJUGYa9XqnWz7kam4.sAjcinYrh_WWSASvUEBtBWa77Xn-mfN9nYh38C4sr-U&dib_tag=se&keywords=create+gui+application&qid=1756134586&sprefix=create+gui+application%2Caps%2C185&sr=8-1)
    - [pdf](livre_pyqt6.pdf)

---

## 6. Travaux pratiques

### 🚧 TP1 - Installation et validation de l'environnement
**Durée** : 15 minutes  

### 🚧 TP2 - Configuration VSCode et premier debug
**Durée** : 20 minutes  

### 🚧 TP3 - Navigation dans la documentation
**Durée** : 15 minutes  

### 🚧 TP4 - Première application personnalisée
**Durée** : 30 minutes  

---

## 7. Points clés à retenir

### ✅ Concepts essentiels
- Qt est un framework C++ multiplateforme, PyQt6 en est le binding Python
- Une seule instance `QApplication` par processus
- La boucle d'événements gère les interactions utilisateur
- Les signaux/slots permettent la communication entre composants

### ✅ Bonnes pratiques
- Toujours terminer par `sys.exit(app.exec())`
- Utiliser un environnement virtuel pour l'isolation
- Préférer PyQt6 pour les nouveaux projets
- Consulter la documentation Qt C++ puis transposer

### ✅ Configuration VSCode
- Sélectionner le bon interpréteur Python (celui du venv)
- Configurer le debug avec `launch.json`
- Installer les extensions Python appropriées

### 📚 Ressources indispensables
- Documentation PyQt6 : API Python spécifique
- Documentation Qt 6 : Référence complète
- Python GUIs : Tutoriels pratiques

---

## Prochaine étape

Dans le **Chapitre 2 - Principes généraux de PyQt6**, nous approfondirons :
- L'architecture d'une application Qt complète
- La gestion des événements et signaux/slots
- L'intégration HTML/CSS dans Qt
- La création de barres de menus et d'outils
