# Chapitre 5 : Architecture MVC (Model-View) en Qt

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Comprendre les concepts fondamentaux de l'architecture Model-View de Qt
- Distinguer les responsabilités du modèle et de la vue dans une application Qt
- Implémenter des modèles personnalisés héritant de QAbstractListModel et QAbstractTableModel
- Créer des applications avec synchronisation automatique entre données et interface
- Gérer les signaux de modification de modèles pour des mises à jour en temps réel
- Implémenter la persistance de données dans une architecture Model-View
- Construire des interfaces complexes avec QListView

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Comprendre l'architecture Model-View

### 1.1 Qu'est-ce que l'architecture Model-View ?

L'architecture **Model-View** est un patron de conception qui sépare les données de leur présentation. Elle divise une application en deux composants interconnectés mais distincts

#### 🎯 **Le Modèle (Model)**
- **Responsabilité** : Gérer les données et la logique métier
- **Contient** : Les données brutes, leur structure et les règles de validation
- **Exemple** : Une liste de tâches, une base de données, un fichier JSON
- **Indépendance** : Ne connaît rien de l'interface utilisateur

#### 🖼️ **La Vue (View)**  
- **Responsabilité** : Présenter les données à l'utilisateur
- **Contient** : Les widgets d'affichage et d'interaction
- **Exemple** : QListView, QTableView, QTreeView
- **Flexibilité** : Plusieurs vues peuvent partager le même modèle

#### 🎪 **Où est passé le Controller ?**

**Question cruciale** : Dans le MVC traditionnel, on a trois composants distincts. Qu'est-il arrivé au **Controller** dans Qt ?

**MVC traditionnel** :
- **Model** : Gère les données et la logique métier
- **View** : Affiche les données à l'utilisateur  
- **Controller** : Gère les interactions utilisateur et coordonne Model/View

**Qt Model-View** :
- **Model** : Gère les données et la logique métier (identique)
- **View** : Affiche les données ET gère les interactions utilisateur

**Pourquoi cette fusion ?** Dans Qt, les widgets de vue (QListView, QTableView) gèrent naturellement :
- ✅ **L'affichage** des données (rôle de Vue)
- ✅ **Les interactions** clavier/souris (rôle de Contrôleur)
- ✅ **La sélection** d'éléments (rôle de Contrôleur)
- ✅ **L'édition** directe (rôle de Contrôleur)

**Le Controller existe toujours**, mais il est **intégré dans la View** ! C'est pourquoi Qt parle de **"Model-View"** plutôt que de **"Model-View-Controller"**.

### 1.2 Avantages de cette architecture

#### ✅ **Séparation des responsabilités**
```python
# ❌ Approche naïve - tout mélangé
class BadTodoApp:
    def __init__(self) -> None:
        self.todos = ["Acheter du lait", "Finir le projet"]  # Données
        self.list_widget = QListWidget()                     # Vue
        self.update_display()                                # Logique mélangée
    
    def add_todo(self, text: str) -> None:
        self.todos.append(text)           # Modification données
        item = QListWidgetItem(text)      # Mise à jour vue
        self.list_widget.addItem(item)    # Logique mélangée !

# ✅ Approche Model-View - séparation claire
class GoodTodoApp:
    def __init__(self) -> None:
        self.model = TodoModel()          # Modèle séparé
        self.view = QListView()           # Vue séparée
        self.view.setModel(self.model)    # Connexion automatique
    
    def add_todo(self, text: str) -> None:
        self.model.add_todo(text)         # Seule modification du modèle
        # La vue se met à jour automatiquement !
```

#### ✅ **Synchronisation automatique**
- Les modifications du modèle déclenchent automatiquement les mises à jour de la vue
- Plusieurs vues peuvent afficher les mêmes données en temps réel
- Aucun code de synchronisation manuelle à écrire

#### ✅ **Réutilisabilité et flexibilité**
- Un même modèle peut alimenter une QListView, une QTableView et une QTreeView
- Changement de vue sans modification du modèle
- Tests unitaires facilités (modèle indépendant de l'interface)

### 1.3 Premier exemple pratique

Pour illustrer la simplicité de l'architecture Model-View, commençons par l'exemple le plus basique possible :

```python
import sys
from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QApplication, QListView, QMainWindow

class SimpleListApp(QMainWindow):
    """Application basique avec une liste de textes"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Exemple Model-View simple")
        self.setGeometry(100, 100, 300, 400)
        
        # Données : simple liste de chaînes
        fruits = ["Pomme", "Banane", "Orange", "Fraise", "Kiwi"]
        
        # Créer le modèle avec les données
        self.model = QStringListModel(fruits)
        
        # Créer la vue et la connecter au modèle
        self.list_view = QListView()
        self.list_view.setModel(self.model)  # 🔑 Connexion automatique !
        
        # Définir la vue comme widget central
        self.setCentralWidget(self.list_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleListApp()
    window.show()
    sys.exit(app.exec())
```

**🔑 Points clés de cet exemple :**
- **Simplicité maximale** : 3 lignes pour connecter modèle et vue
- **Aucune méthode à surcharger** : `QStringListModel` gère tout automatiquement
- **Séparation immédiate** : Les données sont dans le modèle, l'affichage dans la vue
- **Connexion magique** : `setModel()` établit toute la communication automatiquement

---

## 2. Choisir et utiliser les modèles Qt

Qt propose plusieurs modèles prêts à l'emploi selon vos besoins. Choisir le bon modèle dès le départ vous fera gagner beaucoup de temps.

### 2.1 Les modèles disponibles dans Qt

| **Besoin** | **Modèle recommandé** | **Quand l'utiliser** |
|------------|----------------------|---------------------|
| Liste simple de textes | `QStringListModel` | Affichage basique d'une liste de chaînes |
| Liste complexe personnalisée | `QAbstractListModel` | Structures de données personnalisées |
| Tableau de données | `QAbstractTableModel` | Données en lignes/colonnes |
| Modèle polyvalent | `QStandardItemModel` | Prototypage rapide, données hiérarchiques |
| Fichiers/dossiers | `QFileSystemModel` | Explorer de fichiers |
| Base de données | `QSqlTableModel` | Accès direct aux tables SQL |
| Structure d'arbre | `QAbstractItemModel` | Données hiérarchiques complexes |

**🎯 Règle générale** : Commencez toujours par le modèle le plus simple qui répond à vos besoins, puis évoluez si nécessaire.

### 2.2 Exemple avancé : QAbstractListModel

Quand vous avez besoin de structures de données personnalisées, `QAbstractListModel` est votre allié. Créons une Todo List avec statut :

```python
from typing import Any
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from typing_extensions import override

class TodoModel(QAbstractListModel):
    """Modèle pour gérer une liste de tâches avec statut"""

    def __init__(self, todos: list[tuple[bool, str]] | None = None) -> None:
        super().__init__()
        # Structure : [(terminé, texte), (terminé, texte), ...]
        # où terminé = True (fait) ou False (à faire)
        self._todos = todos or []

    @override
    def columnCount(self, parent: QModelIndex | None = None) -> int:
        """🔴 OBLIGATOIRE : Nombre d'éléments dans la liste"""
        return 1

    @override
    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """🔴 OBLIGATOIRE : Nombre de colonnes dans la liste"""
        return len(self._todos)

    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """🔴 OBLIGATOIRE : Données à afficher pour un élément"""
        if not index.isValid() or index.row() >= len(self._todos):
            return None

        is_done, text = self._todos[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            # Texte à afficher : préfixe selon le statut
            prefix = "✅" if is_done else "📝"
            return f"{prefix} {text}"

        return None

    def add_todo(self, text: str) -> None:
        """Ajoute une nouvelle tâche"""
        if not text.strip():
            return

        row = len(self._todos)
        
        # 🚨 CRUCIAL : Notifier AVANT modification
        self.beginInsertRows(QModelIndex(), row, row)
        
        # Modification des données
        self._todos.append((False, text.strip()))
        
        # 🚨 CRUCIAL : Notifier APRÈS modification
        self.endInsertRows()
        # → La vue se met à jour automatiquement !

    def toggle_done(self, row: int) -> None:
        """Bascule le statut d'une tâche"""
        if 0 <= row < len(self._todos):
            is_done, text = self._todos[row]
            self._todos[row] = (not is_done, text)
            
            # Notifier que cette ligne a changé
            index = self.index(row, 0)
            self.dataChanged.emit(index, index)

    def remove_todo(self, row: int) -> None:
        """Supprime une tâche"""
        if 0 <= row < len(self._todos):
            # 🚨 CRUCIAL : Notifier AVANT suppression
            self.beginRemoveRows(QModelIndex(), row, row)
            
            # Suppression des données
            del self._todos[row]
            
            # 🚨 CRUCIAL : Notifier APRÈS suppression
            self.endRemoveRows()
```

**🎯 Méthodes obligatoires pour QAbstractListModel** :
- `rowCount()` : Indique combien d'éléments il y a
- `data()` : Fournit les données à afficher pour chaque élément

**🚨 Signaux cruciaux** :
- `beginInsertRows()` / `endInsertRows()` : Pour les ajouts
- `beginRemoveRows()` / `endRemoveRows()` : Pour les suppressions  
- `dataChanged.emit()` : Pour les modifications

### 2.3 Connecter le modèle à l'interface

Maintenant, créons une interface simple pour utiliser notre modèle :

```python
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QLineEdit, QPushButton, QListView
)

class TodoApp(QMainWindow):
    """Application Todo List complète"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ma Todo List")
        self.setGeometry(100, 100, 400, 500)

        # Créer le modèle avec quelques tâches d'exemple
        initial_todos = [
            (False, "Acheter du lait"),
            (True, "Finir le projet"),
            (False, "Appeler maman")
        ]
        self.model = TodoModel(initial_todos)
        
        self.setup_ui()
        self.connect_signals()

    def setup_ui(self) -> None:
        """Configure l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Zone de saisie
        input_layout = QHBoxLayout()

        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Nouvelle tâche...")
        input_layout.addWidget(self.todo_input)
        
        self.add_button = QPushButton("Ajouter")
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)

        # Liste des tâches
        self.list_view = QListView()
        self.list_view.setModel(self.model)  # 🔑 Connexion magique !
        layout.addWidget(self.list_view)

        # Boutons d'action
        action_layout = QHBoxLayout()

        self.toggle_button = QPushButton("Basculer statut")
        action_layout.addWidget(self.toggle_button)

        self.delete_button = QPushButton("Supprimer")
        action_layout.addWidget(self.delete_button)

        layout.addLayout(action_layout)

    def connect_signals(self) -> None:
        """Connecte les signaux aux actions"""
        self.add_button.clicked.connect(self.add_todo)
        self.todo_input.returnPressed.connect(self.add_todo)  # Entrée pour ajouter
        self.toggle_button.clicked.connect(self.toggle_todo)
        self.delete_button.clicked.connect(self.delete_todo)

        self.list_view.doubleClicked.connect(self.toggle_todo)

    def add_todo(self) -> None:
        """Ajoute une nouvelle tâche"""
        text = self.todo_input.text()
        if text.strip():
            self.model.add_todo(text)
            self.todo_input.clear()
    
    def toggle_todo(self) -> None:
        """Bascule le statut de la tâche sélectionnée"""
        indexes = self.list_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.model.toggle_done(row)

    def delete_todo(self) -> None:
        """Supprime la tâche sélectionnée"""
        indexes = self.list_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.model.remove_todo(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
```

### 2.4 Enrichir l'affichage avec les rôles

La méthode `data()` peut retourner différents types d'informations selon le **rôle** demandé. Améliorons notre Todo List :

```python
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt

class EnhancedTodoModel(TodoModel):
    """Modèle Todo avec affichage enrichi"""
    
    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Données enrichies avec couleurs et formatage"""
        if not index.isValid() or index.row() >= len(self._todos):
            return None

        is_done, text = self._todos[index.row()]

        match role:
            case Qt.ItemDataRole.DisplayRole:
                # Texte à afficher
                prefix = "✅" if is_done else "📝"
                return f"{prefix} {text}"
            
            case Qt.ItemDataRole.ForegroundRole:
                # Couleur du texte
                return QColor(Qt.GlobalColor.green if is_done else Qt.GlobalColor.red)
            
            case Qt.ItemDataRole.FontRole:
                # Style de police
                font = QFont()
                if is_done:
                    font.setStrikeOut(True)  # Barré pour les tâches terminées
                else:
                    font.setBold(True)  # Gras pour les tâches à faire
                return font
            
            case Qt.ItemDataRole.BackgroundRole:
                # Couleur de fond
                if is_done:
                    return QColor(240, 255, 240)  # Vert très clair
                return QColor(255, 250, 240)  # Jaune très clair
            
            case _:
                return None
```

**🎨 Rôles d'affichage principaux** :
- `DisplayRole` : Texte affiché
- `ForegroundRole` : Couleur du texte
- `BackgroundRole` : Couleur de fond
- `FontRole` : Style de police (gras, italique, etc.)
- `DecorationRole` : Icône à afficher

### 2.5 Bonnes pratiques et conseils

#### Les erreurs à éviter absolument

#### ❌ **Oublier les signaux de notification**
```python
# ❌ ERREUR : Modification sans notification
def add_todo_wrong(self, text: str) -> None:
    self._todos.append((False, text))
    # La vue ne se met PAS à jour !

# ✅ CORRECT : Toujours notifier les changements
def add_todo_correct(self, text: str) -> None:
    row = len(self._todos)
    self.beginInsertRows(QModelIndex(), row, row)  # AVANT
    self._todos.append((False, text))              # MODIFICATION
    self.endInsertRows()                           # APRÈS
```

#### ❌ **Mélanger logique métier et interface**
```python
# ❌ ERREUR : Logique dans l'interface
class BadTodoApp(QMainWindow):
    def add_todo(self) -> None:
        text = self.input.text()
        if len(text.strip()) == 0:  # Validation dans l'UI !
            return
        # Logique de sauvegarde dans l'UI !
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

# ✅ CORRECT : Logique dans le modèle
class GoodTodoApp(QMainWindow):
    def add_todo(self) -> None:
        text = self.input.text()
        self.model.add_todo(text)  # Le modèle gère tout
```

#### Conseils pour bien démarrer

#### 🎯 **Choisir le bon modèle**
1. **Liste de textes simples** → `QStringListModel`
2. **Données personnalisées** → `QAbstractListModel`
3. **Besoin de prototyper rapidement** → `QStandardItemModel`
4. **En cas de doute** → Commencez simple et évoluez !

#### 🔧 **Structure de code recommandée**
```
my_app/
├── main.py              # Point d'entrée
├── assets/              # Ressources (images, icônes)
│   ├── images/
│   └── icons/
├── src/
    ├── domain/          # Logique métier pure
    ├── models/          # Modèles Qt (QAbstractListModel, etc.)
    │   ├── __init__.py
    │   └── book_model.py
    ├── ui/
    │   ├── __init__.py
    │   ├── forms/       # Fichiers Qt Designer (.ui)
    │   │   └── main_window.ui
    │   ├── views/       # Classes Python des vues
    │   │   ├── __init__.py
    │   │   ├── generated/           # Fichiers compilés depuis .ui
    │   │   │   ├── __init__.py
    │   │   │   └── main_window_ui.py
    │   │   └── main_window.py       # Classe finale avec logique
    │   ├── widgets/     # Widgets personnalisés
    │   │   ├── __init__.py
    │   │   └── book_widget.py
    │   └── styles/
    │       └── app_style.qss        # Styles CSS/QSS
    └── utils/
        ├── __init__.py
        └── persistence.py           # Sauvegarde/chargement
```

#### Conseils de performance

#### ⚡ **Pour de gros volumes de données**
- Utilisez `beginResetModel()` / `endResetModel()` pour les changements massifs
- Groupez les modifications avec `dataChanged.emit(top_left, bottom_right)`
- Évitez les calculs complexes dans `data()` - précalculez si possible

---

## 3. Travaux pratiques

Les 4 TPs forment **une seule application** qui évolue progressivement : un **gestionnaire de bibliothèque personnelle**. Chaque TP ajoute des fonctionnalités en suivant la progression du cours.

### 🚧 TP1 - Modèle de base et première vue
**Durée** : 30 minutes  
**Objectif** : Créer les fondations avec un modèle minimal

**À réaliser** :
- Créer un modèle `BookModel` héritant de `QAbstractListModel`
- Implémenter les 2 méthodes obligatoires : `rowCount()` et `data()`
- Afficher une liste statique de 5 livres avec `QListView`
- Créer l'interface de base avec `QMainWindow`

**Concepts abordés** : Architecture Model-View de base, méthodes obligatoires

### 🚧 TP2 - Interactions et signaux
**Durée** : 30 minutes  
**Objectif** : Ajouter les interactions utilisateur de base

**À réaliser** :
- Ajouter un `QLineEdit` et un bouton "Ajouter un livre"
- Implémenter `add_book()` avec les signaux `beginInsertRows()` / `endInsertRows()`
- Ajouter un bouton "Supprimer" pour le livre sélectionné
- Implémenter `remove_book()` avec les signaux `beginRemoveRows()` / `endRemoveRows()`

**Concepts abordés** : Signaux de modification, synchronisation automatique vue-modèle

### 🚧 TP3 - Enrichissement visuel avec les rôles
**Durée** : 30 minutes
**Objectif** : Utiliser les rôles pour améliorer l'affichage

**À réaliser** :
- Étendre le modèle pour gérer auteur + statut (lu/non lu)
- Implémenter plusieurs rôles dans `data()` :
  - `DisplayRole` : "Titre par Auteur"
  - `ForegroundRole` : Couleur selon le statut
  - `FontRole` : Gras pour les livres non lus
  - `DecorationRole` : Icône 📖 ou ✅
- Ajouter un bouton "Marquer comme lu"

**Concepts abordés** : Rôles d'affichage, formatage conditionnel, `match/case`

### 🚧 TP4 - Persistance des données *(optionnel)*
**Durée** : 30 minutes
**Objectif** : Sauvegarder et charger les données

**À réaliser** :
- Implémenter `save_to_json()` pour sauvegarder la bibliothèque
- Implémenter `load_from_json()` pour charger au démarrage
- Sauvegarder automatiquement à chaque modification
- Gérer les erreurs de fichier avec des try/except
- Ajouter un compteur "X livres dans votre bibliothèque"

**Concepts abordés** : Persistance JSON, gestion d'erreurs, sauvegarde automatique

---

## 4. Points clés à retenir

### ✅ Choisir le bon modèle
- **QStringListModel** : Pour les listes simples de textes
- **QAbstractListModel** : Pour les structures de données personnalisées
- **Autres** : Voir le livre pyqt6 pour les autres structures.
- **Principe** : Commencer simple et évoluer selon les besoins

### ✅ Méthodes essentielles
- **`rowCount()`** : Nombre d'éléments (obligatoire)
- **`data()`** : Données à afficher avec support des rôles (obligatoire)
- **Signaux** : `beginInsertRows()` / `endInsertRows()` pour les modifications

### ✅ Architecture Model-View
- **Séparation stricte** : Le modèle gère les données, la vue gère l'affichage
- **Connexion simple** : `view.setModel(model)` suffit pour tout connecter
- **Synchronisation automatique** : Pas de code de mise à jour manuelle

### ✅ Bonnes pratiques
- **Ne jamais oublier** les signaux de notification
- **Séparer clairement** logique métier et interface utilisateur
- **Structurer le code** en modules séparés (models/, views/, etc.)

---

## Prochaine étape

Dans le **Chapitre 6 - Aspects avancés**, nous découvrirons :
- Les délégués personnalisés pour l'édition avancée de données
- L'intégration avec des bases de données via les modèles SQL de Qt
- Les techniques d'optimisation pour de gros volumes de données
- Les modèles proxy pour le filtrage et la transformation de données
