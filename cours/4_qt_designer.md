# Chapitre 4 : Utilisation de Qt Designer

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Installer et configurer Qt Designer dans un environnement Python moderne
- Maîtriser l'interface et les outils essentiels de Qt Designer  
- Créer des interfaces graphiques de manière visuelle et efficace
- Intégrer les fichiers .ui dans vos applications Python (chargement dynamique vs compilation)
- Appliquer les bonnes pratiques de conception d'interface avec Designer

## Durée estimée : 3h00
- **Théorie** : 1h30
- **Travaux pratiques** : 1h30

---

## 1. Installation et configuration

Qt Designer nécessite une configuration spécifique pour fonctionner correctement avec les versions récentes de Python et PyQt6.

#### 🔧 **Installation avec UV (recommandée)**

```bash
# Fixer la version Python pour éviter les conflits
uv python pin 3.11
```

Configuration dans `pyproject.toml` :

```toml
[project]
requires-python = ">=3.11,<3.13"
dependencies = [
    "pyqt6==6.3.1",
    "pyqt6-tools>=6.3.1.3.3",
    "setuptools>=80.9.0",
]
```

#### 🚀 **Lancement de Qt Designer**

```bash
# Lancer Qt Designer via uv
uv run pyqt6-tools designer
```

**💡 Pourquoi cette configuration ?**
- **Python 3.11** : Version stable avec PyQt6-tools
- **PyQt6 6.3.1** : Version testée et compatible
- **setuptools** : Requis pour PyQt6-tools

---

## 2. Introduction à Qt Designer

### 2.1 Philosophie WYSIWYG

Qt Designer est un outil **WYSIWYG** (What You See Is What You Get) qui vous permet de concevoir visuellement vos interfaces utilisateur.

#### 🎯 **Avantages du Designer**
- **Conception visuelle** : Drag & drop des widgets
- **Aperçu en temps réel** : Voir immédiatement le résultat
- **Productivité** : Plus rapide que coder manuellement
- **Séparation des préoccupations** : Interface séparée de la logique

### 2.2 Interface de Qt Designer

![Interface Qt Designer](assets/figure_74.png)

Lorsque vous ouvrez Qt Designer, vous êtes accueilli par le dialogue **New Form** qui vous permet de choisir le type d'interface :

![Qt Designer Editor](assets/figure_75.png)

#### 📊 **Zones principales de l'interface**

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
├──────────────┼────────────────────────┼──────────────────────┤
│ Object       │                        │ Resource Browser     │
│ Inspector    │                        │                      │
└──────────────┴────────────────────────┴──────────────────────┘
```

**Zones clés :**
- **Widget Box** : Palette des composants disponibles
- **Zone de conception** : Canvas où vous construisez votre interface
- **Property Editor** : Configuration des propriétés des widgets
- **Object Inspector** : Hiérarchie des widgets de votre interface

---

## 3. Chargement et intégration en Python

### 3.1 Chargement dynamique avec uic.loadUi()

La méthode **recommandée** pour débuter : chargement dynamique des fichiers `.ui`.

#### 🔧 **Méthode simple**

```python
"""Chargement direct d'un fichier .ui"""
import os
import sys
from PyQt6 import QtWidgets, uic

def main() -> int:
    # Chemin relatif sécurisé
    basedir = os.path.dirname(__file__)
    ui_path = os.path.join(basedir, "mainwindow.ui")
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Chargement direct du fichier .ui
    window = uic.loadUi(ui_path)
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

#### 🏗️ **Intégration dans une classe**

```python
"""Intégration dans une classe personnalisée"""
import os
import sys
from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Chargement de l'interface
        basedir = os.path.dirname(__file__)
        ui_path = os.path.join(basedir, "mainwindow.ui")
        uic.loadUi(ui_path, self)

def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

### 3.2 Compilation avec pyuic6

Alternative pour les projets plus importants : compilation des fichiers `.ui` en Python.

#### 🛠️ **Processus de compilation**

```bash
# Compiler un fichier .ui vers Python
pyuic6 mainwindow.ui -o ui_mainwindow.py
```

Le fichier généré contient une classe `Ui_MainWindow` :

```python
# ui_mainwindow.py (généré automatiquement)
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow:
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 280, 100, 30))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mon Application"))
        self.pushButton.setText(_translate("MainWindow", "Cliquer"))
```

#### 🏭 **Utilisation de la classe compilée**

```python
"""Utilisation d'une interface compilée"""
import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

# Import de la classe générée
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        # Configuration post-interface
        self.setup_ui_customization()
        self.setup_connections()
    
    def setup_ui_customization(self) -> None:
        """Personnalisation de l'interface après setupUi"""
        # Modifier les propriétés non définies dans Designer
        if hasattr(self, 'label'):
            font = self.label.font()
            font.setPointSize(25)
            self.label.setFont(font)
            self.label.setAlignment(
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
            )
    
    def setup_connections(self) -> None:
        """Configuration des signaux/slots"""
        # Les widgets sont accessibles directement
        self.pushButton.clicked.connect(self.update_label)
    
    def update_label(self) -> None:
        """Met à jour le label avec un nombre aléatoire"""
        number = random.randint(1, 6)
        self.label.setText(f"🎲 Résultat : {number}")

def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

### 3.3 Comparaison des méthodes

#### 📊 **Chargement dynamique vs Compilation**

| Aspect | uic.loadUi() | pyuic6 |
|--------|--------------|--------|
| **Simplicité** | ✅ Très simple | ⚠️ Étape supplémentaire |
| **Performance** | ⚠️ Légèrement plus lent | ✅ Plus rapide |
| **Débogage** | ⚠️ Erreurs à l'exécution | ✅ Erreurs à la compilation |
| **Autocomplétion** | ❌ Limitée | ✅ Complète |
| **Fichiers requis** | .ui + .py | .py seulement |
| **Prototypage** | ✅ Idéal | ⚠️ Plus lourd |

**💡 Recommandation :** Commencez avec `uic.loadUi()` pour apprendre, puis passez à la compilation pour les projets professionnels.

---

## 4. Ajout de la logique applicative

### 4.1 Connexion des signaux aux slots

Une fois l'interface chargée, vous pouvez connecter les widgets exactement comme avec du code pur Python :

```python
"""Exemple avec logique applicative simple"""
import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        # Personnalisation post-interface
        font = self.label.font()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Connexion des signaux
        self.pushButton.clicked.connect(self.update_label)
    
    def update_label(self) -> None:
        """Met à jour le label avec un nombre aléatoire"""
        number = random.randint(1, 6)
        self.label.setText(f"{number}")

def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

### 4.2 Propriété objectName

**Point crucial** : Dans Qt Designer, configurez toujours la propriété `objectName` de vos widgets. C'est ce nom qui sera utilisé pour accéder au widget en Python.

```python
# Si votre bouton s'appelle "pushButton" dans Designer :
self.pushButton.clicked.connect(self.my_function)

# Si votre label s'appelle "label" dans Designer :
self.label.setText("Nouveau texte")
```

---

## 5. Travaux pratiques

### 🚧 TP1 - Première interface avec Designer
**Durée** : 20 minutes

**Objectif** : Maîtriser le workflow de base

1. **Créer** une interface simple dans Qt Designer (MainWindow + Button + Label)
2. **Charger** avec `uic.loadUi()`
3. **Connecter** le bouton à une fonction simple

### 🚧 TP2 - Compilation avec pyuic6
**Durée** : 15 minutes

**Objectif** : Comprendre la compilation

1. **Compiler** l'interface du TP1 avec `pyuic6`
2. **Adapter** le code pour utiliser la classe générée
3. **Comparer** les deux approches

---

## 6. Points clés à retenir

### ✅ Concepts essentiels
- Qt Designer sépare **conception visuelle** et **logique métier**
- **Chargement dynamique** (`uic.loadUi`) : simple et rapide pour débuter
- **Compilation** (`pyuic6`) : meilleure pour la production

### ✅ Workflow de base
1. **Concevoir** l'interface dans Qt Designer
2. **Configurer** la propriété `objectName` des widgets
3. **Charger** ou **compiler** l'interface
4. **Connecter** les signaux aux slots en Python

### ✅ Deux méthodes d'intégration
- **`uic.loadUi()`** : Idéal pour apprendre et prototyper
- **`pyuic6`** : Recommandé pour les projets professionnels

---

## Prochaine étape

Dans le **Chapitre 5 - Gestion des événements avancée**, nous découvrirons :
- La création de signaux personnalisés
- La gestion avancée des événements clavier et souris
- Les filtres d'événements pour intercepter les interactions
- La communication inter-widgets sophistiquée
