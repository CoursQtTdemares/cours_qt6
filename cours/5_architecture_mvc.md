# Chapitre 5 : Architecture MVC (Model-View) en Qt

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Comprendre les concepts fondamentaux de l'architecture Model-View de Qt
- Distinguer les responsabilités du modèle et de la vue dans une application Qt
- Implémenter des modèles personnalisés héritant de QAbstractListModel et QAbstractTableModel
- Créer des applications avec synchronisation automatique entre données et interface
- Gérer les signaux de modification de modèles pour des mises à jour en temps réel
- Implémenter la persistance de données dans une architecture Model-View
- Construire des interfaces complexes avec QListView et QTableView

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

### 1.3 Le fonctionnement en pratique

```python
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtWidgets import QApplication, QListView, QMainWindow, QVBoxLayout, QWidget
import sys
from typing import Any

class SimpleModel(QAbstractListModel):
    """Modèle simple pour démonstration"""
    
    def __init__(self, data: list[str] = None) -> None:
        super().__init__()
        self._data = data or []
    
    def rowCount(self, parent=None) -> int:
        """Nombre d'éléments dans le modèle"""
        return len(self._data)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> Any:
        """Données à afficher pour un index donné"""
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()]
        return None
    
    def add_item(self, text: str) -> None:
        """Ajoute un élément au modèle"""
        row = len(self._data)
        self.beginInsertRows(None, row, row)  # Notification de début
        self._data.append(text)
        self.endInsertRows()                  # Notification de fin
        # La vue se met à jour automatiquement !

class ModelViewDemo(QMainWindow):
    """Démonstration de l'architecture Model-View"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Architecture Model-View")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()
    
    def setup_ui(self) -> None:
        """Configure l'interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Créer le modèle avec des données initiales
        initial_data = ["Premier élément", "Deuxième élément", "Troisième élément"]
        self.model = SimpleModel(initial_data)
        
        # Créer la vue et la connecter au modèle
        self.list_view = QListView()
        self.list_view.setModel(self.model)  # 🔑 Connexion magique !
        
        layout.addWidget(self.list_view)
        
        # Démonstration : ajouter un élément après 2 secondes
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(2000, lambda: self.model.add_item("Nouvel élément !"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelViewDemo()
    window.show()
    sys.exit(app.exec())
```

**🔑 Points clés de cet exemple :**
- Le modèle gère les données (`self._data`)
- La vue affiche automatiquement les données du modèle
- `setModel()` établit la connexion entre modèle et vue
- Les signaux `beginInsertRows()` / `endInsertRows()` notifient automatiquement la vue
- Aucune logique de mise à jour manuelle dans la vue !

---

## 2. Créer une application Todo List complète

Pour bien comprendre l'architecture Model-View, nous allons construire une **application de gestion de tâches** (Todo List) complète. Cette application illustrera parfaitement la séparation entre les données et leur présentation.

### 2.1 Architecture de l'application

Notre Todo List comprendra :
- **Modèle** : `TodoModel` héritant de `QAbstractListModel`
- **Vue** : `QListView` pour afficher la liste des tâches
- **Interface** : Boutons pour ajouter, supprimer et marquer comme terminé
- **Persistance** : Sauvegarde automatique des données

### 2.2 Conception du modèle de données

```python
from typing import Any

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from typing_extensions import override


class TodoModel(QAbstractListModel):
    """Modèle pour gérer une liste de tâches"""

    def __init__(self, todos: list[tuple[bool, str]] | None = None) -> None:
        super().__init__()
        # Structure : [(status, text), (status, text), ...]
        # où status = True (terminé) ou False (à faire)
        self.todos = todos or []

    @override
    def rowCount(self, parent: QModelIndex | None = None) -> int:
        """Retourne le nombre de tâches dans le modèle"""
        return len(self.todos)

    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        """Retourne les données pour un index et un rôle donnés"""
        if not index.isValid():
            return None

        if index.row() >= len(self.todos):
            return None

        status, text = self.todos[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            # Texte à afficher
            return text + "status: " + str(status)

        return None

    def add_todo(self, text: str) -> None:
        """Ajoute une nouvelle tâche"""
        if not text.strip():
            return

        row = len(self.todos)
        self.beginInsertRows(QModelIndex(), row, row)
        self.todos.append((False, text.strip()))
        self.endInsertRows()

    def remove_todo(self, row: int) -> None:
        """Supprime une tâche"""
        if 0 <= row < len(self.todos):
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.todos[row]
            self.endRemoveRows()

    def mark_completed(self, row: int) -> None:
        """Marque une tâche comme terminée"""
        if 0 <= row < len(self.todos):
            _, text = self.todos[row]
            self.todos[row] = (True, text)
            # Notifier que les données ont changé
            index = self.index(row, 0)
            self.dataChanged.emit(index, index)
```

### 2.3 Interface utilisateur de l'application

```python
import json
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.model import TodoModel


class TodoMainWindow(QMainWindow):
    """Fenêtre principale de l'application Todo"""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ma Todo List")
        self.setGeometry(100, 100, 400, 500)

        # Créer le modèle
        self.model = TodoModel()

        # Configurer l'interface
        self.setup_ui()

        # Connecter les signaux
        self.connect_signals()

        # Charger les données sauvegardées
        self.load_data()

    def setup_ui(self) -> None:
        """Configure l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Titre
        title_label = QLabel("Ma Todo List")
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            color: #2c3e50;
        """)
        layout.addWidget(title_label)

        # Zone de saisie
        input_layout = QHBoxLayout()

        self.todo_edit = QLineEdit()
        self.todo_edit.setPlaceholderText("Nouvelle tâche...")
        input_layout.addWidget(self.todo_edit)

        self.add_button = QPushButton("+ Ajouter")
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)

        # Liste des tâches
        self.todo_view = QListView()
        self.todo_view.setModel(self.model)  # 🔑 Connexion modèle-vue
        layout.addWidget(self.todo_view)

        # Boutons d'action
        action_layout = QHBoxLayout()

        self.complete_button = QPushButton("Terminer")
        self.complete_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        action_layout.addWidget(self.complete_button)

        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        action_layout.addWidget(self.delete_button)

        layout.addLayout(action_layout)

    def connect_signals(self) -> None:
        """Connecte les signaux aux slots"""
        self.add_button.clicked.connect(self.add_todo)
        self.todo_edit.returnPressed.connect(self.add_todo)  # Entrée pour ajouter
        self.complete_button.clicked.connect(self.complete_todo)
        self.delete_button.clicked.connect(self.delete_todo)

    def add_todo(self) -> None:
        """Ajoute une nouvelle tâche"""
        text = self.todo_edit.text()
        if text.strip():
            self.model.add_todo(text)
            self.todo_edit.clear()
            self.save_data()  # Sauvegarde automatique

    def complete_todo(self) -> None:
        """Marque la tâche sélectionnée comme terminée"""
        indexes = self.todo_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.model.mark_completed(row)
            self.todo_view.clearSelection()
            self.save_data()

    def delete_todo(self) -> None:
        """Supprime la tâche sélectionnée"""
        indexes = self.todo_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.model.remove_todo(row)
            self.todo_view.clearSelection()
            self.save_data()

    def save_data(self) -> None:
        """Sauvegarde les données dans un fichier JSON"""
        try:
            with open("todos.json", "w", encoding="utf-8") as f:
                json.dump(self.model.todos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")

    def load_data(self) -> None:
        """Charge les données depuis le fichier JSON"""
        try:
            with open("todos.json", "r", encoding="utf-8") as f:
                todos = json.load(f)
                # Recréer le modèle avec les données chargées
                self.model = TodoModel(todos)
                self.todo_view.setModel(self.model)
        except FileNotFoundError:
            # Fichier n'existe pas encore, ce n'est pas un problème
            pass
        except Exception as e:
            print(f"Erreur lors du chargement : {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoMainWindow()
    window.show()
    sys.exit(app.exec())
```

### 2.4 Points clés de l'implémentation

#### 🎯 **Séparation claire des responsabilités**
- **TodoModel** : Gère uniquement les données et leur logique (ajout, suppression, modification)
- **TodoMainWindow** : Gère uniquement l'interface et les interactions utilisateur
- **Aucun mélange** : La vue ne modifie jamais directement les données

#### 🔄 **Synchronisation automatique**
- Modifier le modèle → La vue se met à jour instantanément
- `beginInsertRows()` / `endInsertRows()` → Notification automatique d'ajout
- `dataChanged.emit()` → Notification automatique de modification
- Aucun code de synchronisation manuelle nécessaire

#### 💾 **Persistance des données**
- Sauvegarde automatique à chaque modification
- Format JSON simple et lisible
- Rechargement automatique au démarrage
- Gestion d'erreurs robuste

#### 🎨 **Interface moderne**
- Styles CSS intégrés pour une apparence professionnelle
- Raccourcis clavier (Entrée pour ajouter)
- Feedback visuel immédiat

---

## 3. Comprendre les rôles et signaux des modèles

### 3.1 Signaux de notification du modèle

Les signaux sont le mécanisme par lequel le modèle informe les vues que les données ont changé. **Comprendre et utiliser correctement ces signaux est crucial** pour une synchronisation parfaite.

#### 🔔 **Signaux essentiels**

```python
class ModelSignalsDemo(QAbstractListModel):
    """Démonstration des signaux de modèle"""
    
    def __init__(self) -> None:
        super().__init__()
        self._data = []
    
    def add_item(self, item: str) -> None:
        """Ajouter un élément - Signal d'insertion"""
        row = len(self._data)
        
        # 🚨 OBLIGATOIRE : Notifier AVANT la modification
        self.beginInsertRows(None, row, row)
        
        # Modification des données
        self._data.append(item)
        
        # 🚨 OBLIGATOIRE : Notifier APRÈS la modification
        self.endInsertRows()
        # → La vue se met à jour automatiquement !
    
    def remove_item(self, row: int) -> bool:
        """Supprimer un élément - Signal de suppression"""
        if 0 <= row < len(self._data):
            
            # 🚨 OBLIGATOIRE : Notifier AVANT la suppression
            self.beginRemoveRows(None, row, row)
            
            # Suppression des données
            del self._data[row]
            
            # 🚨 OBLIGATOIRE : Notifier APRÈS la suppression
            self.endRemoveRows()
            return True
        return False
    
    def modify_item(self, row: int, new_value: str) -> bool:
        """Modifier un élément - Signal de changement"""
        if 0 <= row < len(self._data):
            
            # Modification des données
            self._data[row] = new_value
            
            # 🚨 OBLIGATOIRE : Notifier le changement
            index = self.index(row, 0)
            self.dataChanged.emit(index, index)
            # → Seule cette cellule se met à jour !
            return True
        return False
    
    def clear_all(self) -> None:
        """Vider le modèle - Signal de réinitialisation"""
        
        # 🚨 OBLIGATOIRE : Notifier AVANT la réinitialisation
        self.beginResetModel()
        
        # Vider les données
        self._data.clear()
        
        # 🚨 OBLIGATOIRE : Notifier APRÈS la réinitialisation
        self.endResetModel()
        # → Toute la vue se recharge !
```

#### ⚠️ **Erreurs courantes à éviter**

```python
# ❌ ERREUR : Oublier les signaux
def add_item_wrong(self, item: str) -> None:
    self._data.append(item)
    # La vue ne se met PAS à jour !

# ❌ ERREUR : Ordre incorrect des signaux
def add_item_wrong_order(self, item: str) -> None:
    self._data.append(item)        # Modification AVANT notification
    self.beginInsertRows(None, len(self._data)-1, len(self._data)-1)
    self.endInsertRows()
    # Comportement imprévisible !

# ❌ ERREUR : Signaux non appariés
def add_item_unmatched(self, item: str) -> None:
    self.beginInsertRows(None, 0, 0)
    self._data.append(item)
    # Oubli de endInsertRows() → Blocage de la vue !

# ✅ CORRECT : Ordre et appariement corrects
def add_item_correct(self, item: str) -> None:
    row = len(self._data)
    self.beginInsertRows(None, row, row)  # 1. Notification AVANT
    self._data.append(item)               # 2. Modification
    self.endInsertRows()                  # 3. Notification APRÈS
```

#### 🎯 **Optimisation des signaux**

```python
def update_multiple_items(self, updates: list[tuple[int, str]]) -> None:
    """Mise à jour optimisée de plusieurs éléments"""
    
    if not updates:
        return
    
    # Trier les mises à jour par index
    updates.sort(key=lambda x: x[0])
    
    # Grouper les mises à jour consécutives
    ranges = []
    start_row = updates[0][0]
    end_row = start_row
    
    for i, (row, value) in enumerate(updates):
        if i > 0 and row != end_row + 1:
            # Fin d'une série consécutive
            ranges.append((start_row, end_row))
            start_row = row
        end_row = row
        self._data[row] = value
    
    ranges.append((start_row, end_row))
    
    # Émettre un signal pour chaque série consécutive
    for start, end in ranges:
        start_index = self.index(start, 0)
        end_index = self.index(end, 0)
        self.dataChanged.emit(start_index, end_index)
```

### 3.2 Méthodes obligatoires vs optionnelles

#### 🔴 **Méthodes OBLIGATOIRES pour QAbstractListModel**

```python
class MinimalListModel(QAbstractListModel):
    """Modèle minimal fonctionnel"""
    
    def __init__(self, data: list[Any] = None) -> None:
        super().__init__()
        self._data = data or []
    
    def rowCount(self, parent=None) -> int:
        """🔴 OBLIGATOIRE : Nombre d'éléments"""
        return len(self._data)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> Any:
        """🔴 OBLIGATOIRE : Données pour affichage"""
        if role == Qt.ItemDataRole.DisplayRole and index.isValid():
            return self._data[index.row()]
        return None
```

#### 🟡 **Méthodes OPTIONNELLES mais utiles**

```python
class ExtendedListModel(MinimalListModel):
    """Modèle étendu avec fonctionnalités supplémentaires"""
    
    def flags(self, index) -> Qt.ItemFlag:
        """🟡 OPTIONNEL : Propriétés des éléments"""
        if index.isValid():
            return (Qt.ItemFlag.ItemIsEnabled | 
                   Qt.ItemFlag.ItemIsSelectable |
                   Qt.ItemFlag.ItemIsEditable)  # Éditable
        return Qt.ItemFlag.NoItemFlags
    
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole) -> bool:
        """🟡 OPTIONNEL : Permettre l'édition"""
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self._data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False
    
    def insertRows(self, row: int, count: int, parent=None) -> bool:
        """🟡 OPTIONNEL : Permettre l'ajout via la vue"""
        self.beginInsertRows(parent or None, row, row + count - 1)
        for i in range(count):
            self._data.insert(row + i, "Nouvel élément")
        self.endInsertRows()
        return True
    
    def removeRows(self, row: int, count: int, parent=None) -> bool:
        """🟡 OPTIONNEL : Permettre la suppression via la vue"""
        if row < 0 or row + count > len(self._data):
            return False
        
        self.beginRemoveRows(parent or None, row, row + count - 1)
        for i in range(count):
            del self._data[row]
        self.endRemoveRows()
        return True
```

---

## 4. Données tabulaires avec QTableView

`QTableView` est parfait pour afficher des données sous forme de tableau (lignes × colonnes), similaire à Excel. Cette vue utilise `QAbstractTableModel` comme base pour les modèles personnalisés.

### 4.1 Modèle de base pour QTableView

```python
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView
from typing import Any
import sys

class SimpleTableModel(QAbstractTableModel):
    """Modèle simple pour données tabulaires"""
    
    def __init__(self, data: list[list[Any]] = None) -> None:
        super().__init__()
        # Structure : [[ligne1_col1, ligne1_col2, ...], [ligne2_col1, ligne2_col2, ...], ...]
        self._data = data or []
    
    def rowCount(self, parent=None) -> int:
        """🔴 OBLIGATOIRE : Nombre de lignes"""
        return len(self._data)
    
    def columnCount(self, parent=None) -> int:
        """🔴 OBLIGATOIRE : Nombre de colonnes"""
        if self._data:
            return len(self._data[0])  # Utilise la première ligne pour déterminer le nombre de colonnes
        return 0
    
    def data(self, index: QModelIndex, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole) -> Any:
        """🔴 OBLIGATOIRE : Données pour une cellule"""
        if not index.isValid():
            return None
        

        match role:
            case Qt.ItemDataRole.DisplayRole:
                # index.row() → ligne, index.column() → colonne
                return self._data[index.row()][index.column()]
            case _:
                return None

class TableViewDemo(QMainWindow):
    """Démonstration simple de QTableView"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("QTableView - Données tabulaires")
        self.setGeometry(100, 100, 600, 400)
        
        # Données d'exemple
        sample_data = [
            [4, 1, 3, 3, 7],
            [9, 1, 5, 3, 8],
            [2, 1, 5, 3, 9],
            [6, 2, 7, 4, 6],
            [1, 8, 9, 2, 5]
        ]
        
        # Créer le modèle et la vue
        self.model = SimpleTableModel(sample_data)
        self.table = QTableView()
        self.table.setModel(self.model)
        
        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableViewDemo()
    window.show()
    sys.exit(app.exec())
```

### 4.2 Modèle avancé avec en-têtes et formatage

```python
from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QColor, QFont
from typing import Any

class AdvancedTableModel(QAbstractTableModel):
    """Modèle de tableau avancé avec en-têtes et formatage"""
    
    def __init__(self, data: list[dict[str, Any]] = None, headers: list[str] = None) -> None:
        super().__init__()
        self._data = data or []
        self._headers = headers or []
    
    def rowCount(self, parent=None) -> int:
        return len(self._data)
    
    def columnCount(self, parent=None) -> int:
        return len(self._headers)
    
    def data(self, index: QModelIndex, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid() or index.row() >= len(self._data):
            return None
        
        row_data = self._data[index.row()]
        column_key = self._headers[index.column()]
        value = row_data.get(column_key, '')
        

        match role:
            case Qt.ItemDataRole.DisplayRole:
                # Formatage spécial pour certains types
                if isinstance(value, float):
                    return f"{value:.2f}"
                return str(value)
            
            case Qt.ItemDataRole.BackgroundRole:
                # Couleur de fond conditionnelle
                if column_key == 'score' and isinstance(value, (int, float)):
                    if value >= 8:
                        return QColor(200, 255, 200)  # Vert clair pour les bonnes notes
                    elif value < 5:
                        return QColor(255, 200, 200)  # Rouge clair pour les mauvaises notes
            
            case Qt.ItemDataRole.TextAlignmentRole:
                # Alignement selon le type de données
                if isinstance(value, (int, float)):
                    return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
                return Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
            
            case Qt.ItemDataRole.FontRole:
                # Police spéciale pour certaines valeurs
                if column_key == 'nom' and isinstance(value, str):
                    font = QFont()
                    font.setBold(True)
                    return font
            
            case _:
                return None
    
    def headerData(self, section: int, orientation: Qt.Orientation, 
                   role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole) -> Any:
        """Définit les en-têtes de colonnes et lignes"""

        match role:
            case Qt.ItemDataRole.DisplayRole:
                if orientation == Qt.Orientation.Horizontal:
                    # En-têtes de colonnes
                    if section < len(self._headers):
                        return self._headers[section].title()
                else:
                    # En-têtes de lignes (numérotation)
                    return str(section + 1)
            
            case Qt.ItemDataRole.FontRole if orientation == Qt.Orientation.Horizontal:
                # Police des en-têtes (avec guard condition)
                font = QFont()
                font.setBold(True)
                return font
            
            case _:
                return None
    
    def add_row(self, row_data: dict[str, Any]) -> None:
        """Ajoute une ligne de données"""
        row = len(self._data)
        self.beginInsertRows(None, row, row)
        self._data.append(row_data)
        self.endInsertRows()
    
    def remove_row(self, row: int) -> bool:
        """Supprime une ligne"""
        if 0 <= row < len(self._data):
            self.beginRemoveRows(None, row, row)
            del self._data[row]
            self.endRemoveRows()
            return True
        return False

class StudentGradesApp(QMainWindow):
    """Application de gestion de notes d'étudiants"""
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Gestion des Notes - QTableView Avancé")
        self.setGeometry(100, 100, 700, 500)
        self.setup_ui()
    
    def setup_ui(self) -> None:
        # Données d'exemple
        students_data = [
            {'nom': 'Alice', 'prenom': 'Dupont', 'age': 20, 'score': 8.5, 'mention': 'Bien'},
            {'nom': 'Bob', 'prenom': 'Martin', 'age': 19, 'score': 6.2, 'mention': 'Assez Bien'},
            {'nom': 'Charlie', 'prenom': 'Durand', 'age': 21, 'score': 9.1, 'mention': 'Très Bien'},
            {'nom': 'Diana', 'prenom': 'Garcia', 'age': 20, 'score': 4.8, 'mention': 'Insuffisant'},
            {'nom': 'Eve', 'prenom': 'Laurent', 'age': 22, 'score': 7.3, 'mention': 'Bien'}
        ]
        
        headers = ['nom', 'prenom', 'age', 'score', 'mention']
        
        # Créer le modèle
        self.model = AdvancedTableModel(students_data, headers)
        
        # Créer et configurer la vue
        self.table = QTableView()
        self.table.setModel(self.model)
        
        # Configuration de la vue
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        
        # Ajuster la largeur des colonnes
        self.table.resizeColumnsToContents()
        
        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentGradesApp()
    window.show()
    sys.exit(app.exec())
```

### 4.3 Points clés pour QTableView

#### 🎯 **Différences avec QListView**
- **Deux dimensions** : `index.row()` ET `index.column()`
- **Méthode supplémentaire** : `columnCount()` obligatoire
- **En-têtes** : `headerData()` pour nommer les colonnes/lignes
- **Navigation** : L'utilisateur peut naviguer avec les flèches dans toutes les directions

#### 🔧 **Configuration typique de la vue**
```python
def configure_table_view(self, table: QTableView) -> None:
    """Configuration recommandée pour QTableView"""
    # Sélection par lignes entières
    table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
    
    # Alternance de couleurs pour faciliter la lecture
    table.setAlternatingRowColors(True)
    
    # Permettre le tri en cliquant sur les en-têtes
    table.setSortingEnabled(True)
    
    # Ajuster automatiquement la largeur des colonnes
    table.resizeColumnsToContents()
    
    # Étirer la dernière colonne pour remplir l'espace
    table.horizontalHeader().setStretchLastSection(True)
```

#### 📊 **Cas d'usage typiques**
- **Données de base de données** : Affichage de tables SQL
- **Feuilles de calcul simples** : Alternative à Excel pour des données structurées
- **Tableaux de bord** : Présentation de métriques et statistiques
- **Gestion de listes** : Inventaire, contacts, commandes, etc.

---

## 5. Travaux pratiques

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

### 🚧 TP4 - Persistance des données
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

## 6. Points clés à retenir

### ✅ Architecture Model-View
- **Séparation stricte** entre données (modèle) et présentation (vue)
- **Synchronisation automatique** via les signaux Qt
- **Réutilisabilité** : un modèle peut alimenter plusieurs vues
- **Maintenabilité** améliorée grâce au découplage

### ✅ Implémentation de modèles
- **Méthodes obligatoires** : `rowCount()`, `data()` (+ `columnCount()` pour tables)
- **Signaux cruciaux** : `beginInsertRows()` / `endInsertRows()`, `dataChanged`
- **Rôles multiples** : DisplayRole, BackgroundRole, FontRole, etc.
- **Ordre critique** : notification AVANT modification, puis modification, puis notification APRÈS

### ✅ Gestion des vues
- **QListView** : Parfait pour des listes simples et stylées
- **QTableView** : Idéal pour des données tabulaires complexes
- **Configuration** : Sélection, tri, couleurs alternées, redimensionnement
- **Interaction** : Gestion des sélections et des signaux de la vue

### ✅ Bonnes pratiques
- **Validation des données** dans le modèle, pas dans la vue
- **Gestion d'erreurs** robuste lors des modifications
- **Optimisation** : grouper les signaux pour les modifications multiples
- **Persistance** : sauvegarder automatiquement les modifications importantes

---

## Prochaine étape

Dans le **Chapitre 6 - Aspects avancés**, nous découvrirons :
- Les délégués personnalisés pour l'édition avancée de données
- L'intégration avec des bases de données via les modèles SQL de Qt
- Les techniques d'optimisation pour de gros volumes de données
- Les modèles proxy pour le filtrage et la transformation de données
