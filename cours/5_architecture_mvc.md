# Chapitre 5 : Architecture MVC en Qt

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Comprendre les concepts fondamentaux de l'architecture Modèle-Vue-Contrôleur
- Implémenter des modèles de données personnalisés avec QAbstractTableModel
- Créer des vues tabulaires et arborescentes avec QTableView et QTreeView
- Gérer la synchronisation automatique entre modèles et vues
- Utiliser les modèles prédéfinis de Qt (QStringListModel, QStandardItemModel)
- Implémenter l'édition de données avec des délégués personnalisés
- Appliquer les bonnes pratiques de l'architecture MVC dans Qt

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Introduction à l'architecture MVC

### 1.1 Concepts principaux

L'architecture Modèle-Vue-Contrôleur sépare les responsabilités pour créer des applications maintenables :

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, 
    QTableView, QTreeView, QListView, QPushButton, QHBoxLayout
)
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, pyqtSignal
from PyQt6.QtGui import QStandardItemModel, QStandardItem
import sys

class MVCConceptDemo(QMainWindow):
    """Démonstration des concepts MVC de base"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Architecture MVC - Concepts de base")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()
        self.setup_mvc_components()
    
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Contrôles (Contrôleur)
        controls_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Ajouter données")
        self.add_button.clicked.connect(self.add_sample_data)
        controls_layout.addWidget(self.add_button)
        
        self.clear_button = QPushButton("Effacer")
        self.clear_button.clicked.connect(self.clear_data)
        controls_layout.addWidget(self.clear_button)
        
        layout.addLayout(controls_layout)
        
        # Vues multiples du même modèle
        views_layout = QHBoxLayout()
        
        # Vue tableau
        self.table_view = QTableView()
        views_layout.addWidget(self.table_view)
        
        # Vue liste
        self.list_view = QListView()
        views_layout.addWidget(self.list_view)
        
        layout.addLayout(views_layout)
    
    def setup_mvc_components(self):
        """Configure les composants MVC"""
        # Modèle de données (partagé entre les vues)
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['Nom', 'Âge', 'Ville'])
        
        # Connecter le modèle aux vues
        self.table_view.setModel(self.model)
        self.list_view.setModel(self.model)
        
        # Signal de modification du modèle
        self.model.itemChanged.connect(self.on_data_changed)
    
    def add_sample_data(self):
        """Ajoute des données d'exemple (Contrôleur)"""
        sample_data = [
            ['Alice', '25', 'Paris'],
            ['Bob', '30', 'Lyon'],
            ['Charlie', '35', 'Marseille']
        ]
        
        for row_data in sample_data:
            row = []
            for text in row_data:
                item = QStandardItem(text)
                row.append(item)
            self.model.appendRow(row)
    
    def clear_data(self):
        """Efface toutes les données"""
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Nom', 'Âge', 'Ville'])
    
    def on_data_changed(self, item):
        """Réaction aux changements de données"""
        print(f"Données modifiées: {item.text()} à la position ({item.row()}, {item.column()})")
```

### 1.2 Avantages de l'architecture MVC

```python
class MVCBenefitsDemo:
    """Démonstration des avantages de l'architecture MVC"""
    
    def __init__(self):
        self.demonstrate_separation()
        self.demonstrate_reusability()
        self.demonstrate_maintainability()
    
    def demonstrate_separation(self):
        """Séparation des responsabilités"""
        print("=== SÉPARATION DES RESPONSABILITÉS ===")
        print("• Modèle: Gère uniquement les données et la logique métier")
        print("• Vue: S'occupe uniquement de l'affichage")
        print("• Contrôleur: Coordonne les interactions utilisateur")
        print()
    
    def demonstrate_reusability(self):
        """Réutilisabilité des composants"""
        print("=== RÉUTILISABILITÉ ===")
        print("• Un même modèle peut alimenter plusieurs vues")
        print("• Une vue peut afficher différents modèles")
        print("• Les composants sont interchangeables")
        print()
    
    def demonstrate_maintainability(self):
        """Facilité de maintenance"""
        print("=== MAINTENABILITÉ ===")
        print("• Modifications de l'affichage sans impact sur les données")
        print("• Changements de structure de données isolés")
        print("• Tests unitaires facilités par la séparation")
        print()

# Exemple d'utilisation
# demo = MVCBenefitsDemo()
```

---

## 2. Modèles de données avec QAbstractTableModel

### 2.1 Implémentation d'un modèle personnalisé

```python
from PyQt6.QtCore import QAbstractTableModel, QVariant
from typing import List, Any

class PersonModel(QAbstractTableModel):
    """Modèle personnalisé pour gérer des données de personnes"""
    
    def __init__(self, data: List[dict] = None):
        super().__init__()
        self._data = data or []
        self._headers = ['Prénom', 'Nom', 'Âge', 'Email', 'Ville']
    
    # === Méthodes obligatoires ===
    
    def rowCount(self, parent=QModelIndex()):
        """Retourne le nombre de lignes"""
        return len(self._data)
    
    def columnCount(self, parent=QModelIndex()):
        """Retourne le nombre de colonnes"""
        return len(self._headers)
    
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        """Retourne les données pour un index donné"""
        if not index.isValid():
            return QVariant()
        
        if index.row() >= len(self._data) or index.row() < 0:
            return QVariant()
        
        person = self._data[index.row()]
        column_keys = ['prenom', 'nom', 'age', 'email', 'ville']
        
        if role == Qt.ItemDataRole.DisplayRole:
            # Données à afficher
            key = column_keys[index.column()]
            return person.get(key, '')
        
        elif role == Qt.ItemDataRole.EditRole:
            # Données pour l'édition
            key = column_keys[index.column()]
            return person.get(key, '')
        
        elif role == Qt.ItemDataRole.TextAlignmentRole:
            # Alignement du texte
            if index.column() == 2:  # Colonne âge
                return Qt.AlignmentFlag.AlignCenter
            return Qt.AlignmentFlag.AlignLeft
        
        elif role == Qt.ItemDataRole.BackgroundRole:
            # Couleur de fond conditionnelle
            if index.column() == 2:  # Colonne âge
                age = person.get('age', 0)
                if isinstance(age, (int, str)) and int(age) >= 65:
                    return QColor(255, 235, 235)  # Rouge clair pour seniors
        
        return QVariant()
    
    def headerData(self, section: int, orientation: Qt.Orientation, 
                   role: int = Qt.ItemDataRole.DisplayRole):
        """Retourne les en-têtes de colonnes/lignes"""
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            if section < len(self._headers):
                return self._headers[section]
        
        elif orientation == Qt.Orientation.Vertical and role == Qt.ItemDataRole.DisplayRole:
            return str(section + 1)  # Numérotation des lignes
        
        return QVariant()
    
    # === Méthodes pour l'édition ===
    
    def flags(self, index: QModelIndex):
        """Définit les drapeaux pour chaque cellule"""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        
        # Toutes les cellules sont sélectionnables et éditables
        return (Qt.ItemFlag.ItemIsEnabled | 
                Qt.ItemFlag.ItemIsSelectable | 
                Qt.ItemFlag.ItemIsEditable)
    
    def setData(self, index: QModelIndex, value: Any, 
                role: int = Qt.ItemDataRole.EditRole):
        """Modifie les données"""
        if index.isValid() and role == Qt.ItemDataRole.EditRole:
            person = self._data[index.row()]
            column_keys = ['prenom', 'nom', 'age', 'email', 'ville']
            key = column_keys[index.column()]
            
            # Validation des données
            if key == 'age':
                try:
                    value = int(value)
                    if value < 0 or value > 150:
                        return False
                except ValueError:
                    return False
            
            elif key == 'email':
                if '@' not in str(value):
                    return False
            
            # Mise à jour des données
            person[key] = value
            
            # Notification du changement
            self.dataChanged.emit(index, index, [role])
            return True
        
        return False
    
    # === Méthodes pour ajouter/supprimer des données ===
    
    def insertRows(self, row: int, count: int, parent=QModelIndex()):
        """Insère des lignes vides"""
        self.beginInsertRows(parent, row, row + count - 1)
        
        for i in range(count):
            empty_person = {
                'prenom': '',
                'nom': '',
                'age': 0,
                'email': '',
                'ville': ''
            }
            self._data.insert(row + i, empty_person)
        
        self.endInsertRows()
        return True
    
    def removeRows(self, row: int, count: int, parent=QModelIndex()):
        """Supprime des lignes"""
        if row < 0 or row + count > len(self._data):
            return False
        
        self.beginRemoveRows(parent, row, row + count - 1)
        
        for i in range(count):
            del self._data[row]
        
        self.endRemoveRows()
        return True
    
    def add_person(self, person_data: dict):
        """Ajoute une nouvelle personne"""
        row = len(self._data)
        self.beginInsertRows(QModelIndex(), row, row)
        self._data.append(person_data)
        self.endInsertRows()
    
    def get_person(self, row: int) -> dict:
        """Récupère les données d'une personne"""
        if 0 <= row < len(self._data):
            return self._data[row].copy()
        return {}
    
    def get_all_data(self) -> List[dict]:
        """Récupère toutes les données"""
        return self._data.copy()

class PersonTableDemo(QMainWindow):
    """Démonstration du modèle PersonModel"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modèle de données personnalisé")
        self.setup_ui()
        self.setup_model()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Vue tableau
        self.table_view = QTableView()
        layout.addWidget(self.table_view)
        
        # Contrôles
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("Ajouter personne")
        add_btn.clicked.connect(self.add_person)
        controls_layout.addWidget(add_btn)
        
        remove_btn = QPushButton("Supprimer sélection")
        remove_btn.clicked.connect(self.remove_selected)
        controls_layout.addWidget(remove_btn)
        
        layout.addLayout(controls_layout)
    
    def setup_model(self):
        """Configure le modèle avec des données d'exemple"""
        sample_data = [
            {'prenom': 'Jean', 'nom': 'Dupont', 'age': 32, 'email': 'jean@email.com', 'ville': 'Paris'},
            {'prenom': 'Marie', 'nom': 'Martin', 'age': 28, 'email': 'marie@email.com', 'ville': 'Lyon'},
            {'prenom': 'Pierre', 'nom': 'Durand', 'age': 67, 'email': 'pierre@email.com', 'ville': 'Marseille'}
        ]
        
        self.model = PersonModel(sample_data)
        self.table_view.setModel(self.model)
        
        # Configuration de la vue
        self.table_view.resizeColumnsToContents()
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    
    def add_person(self):
        """Ajoute une nouvelle personne"""
        new_person = {
            'prenom': 'Nouveau',
            'nom': 'Utilisateur',
            'age': 25,
            'email': 'nouveau@email.com',
            'ville': 'Ville'
        }
        self.model.add_person(new_person)
    
    def remove_selected(self):
        """Supprime les lignes sélectionnées"""
        selection = self.table_view.selectionModel()
        if selection.hasSelection():
            indexes = selection.selectedRows()
            
            # Trier par ordre décroissant pour supprimer de bas en haut
            rows = sorted([index.row() for index in indexes], reverse=True)
            
            for row in rows:
                self.model.removeRows(row, 1)
```

---

## 3. Vues de données : QTableView et QTreeView

### 3.1 Configuration avancée de QTableView

```python
from PyQt6.QtWidgets import QHeaderView, QAbstractItemView

class AdvancedTableDemo(QMainWindow):
    """Démonstration avancée de QTableView"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView Avancé")
        self.setup_ui()
        self.setup_advanced_table()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.table_view = QTableView()
        layout.addWidget(self.table_view)
        
        # Contrôles de configuration
        config_layout = QHBoxLayout()
        
        self.sort_btn = QPushButton("Activer tri")
        self.sort_btn.clicked.connect(self.toggle_sorting)
        config_layout.addWidget(self.sort_btn)
        
        self.filter_btn = QPushButton("Activer filtre")
        self.filter_btn.clicked.connect(self.toggle_filtering)
        config_layout.addWidget(self.filter_btn)
        
        layout.addLayout(config_layout)
    
    def setup_advanced_table(self):
        """Configure une table avec fonctionnalités avancées"""
        # Modèle avec plus de données
        self.model = PersonModel(self.generate_large_dataset())
        self.table_view.setModel(self.model)
        
        # === Configuration de la vue ===
        
        # Sélection
        self.table_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_view.setSelectionMode(
            QAbstractItemView.SelectionMode.ExtendedSelection
        )
        
        # En-têtes
        horizontal_header = self.table_view.horizontalHeader()
        horizontal_header.setStretchLastSection(True)
        horizontal_header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        
        vertical_header = self.table_view.verticalHeader()
        vertical_header.setVisible(True)
        vertical_header.setDefaultSectionSize(25)
        
        # Tri
        self.table_view.setSortingEnabled(True)
        
        # Alternance des couleurs de lignes
        self.table_view.setAlternatingRowColors(True)
        
        # Grille
        self.table_view.setShowGrid(True)
        
        # === Signaux et connexions ===
        
        selection_model = self.table_view.selectionModel()
        selection_model.selectionChanged.connect(self.on_selection_changed)
        
        self.table_view.doubleClicked.connect(self.on_double_click)
    
    def generate_large_dataset(self) -> List[dict]:
        """Génère un jeu de données plus important"""
        import random
        
        prenoms = ['Jean', 'Marie', 'Pierre', 'Sophie', 'Paul', 'Claire', 'Luc', 'Anne']
        noms = ['Dupont', 'Martin', 'Durand', 'Moreau', 'Laurent', 'Simon', 'Michel', 'Garcia']
        villes = ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice', 'Nantes', 'Bordeaux', 'Lille']
        
        data = []
        for i in range(50):  # 50 personnes
            person = {
                'prenom': random.choice(prenoms),
                'nom': random.choice(noms),
                'age': random.randint(18, 75),
                'email': f'user{i}@example.com',
                'ville': random.choice(villes)
            }
            data.append(person)
        
        return data
    
    def toggle_sorting(self):
        """Active/désactive le tri"""
        current = self.table_view.isSortingEnabled()
        self.table_view.setSortingEnabled(not current)
        
        status = "désactivé" if current else "activé"
        self.sort_btn.setText(f"Tri {status}")
    
    def toggle_filtering(self):
        """Active/désactive le filtrage (via proxy model)"""
        from PyQt6.QtCore import QSortFilterProxyModel
        
        if isinstance(self.table_view.model(), QSortFilterProxyModel):
            # Retour au modèle original
            self.table_view.setModel(self.model)
            self.filter_btn.setText("Activer filtre")
        else:
            # Application du proxy de filtrage
            proxy_model = QSortFilterProxyModel()
            proxy_model.setSourceModel(self.model)
            proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
            proxy_model.setFilterKeyColumn(4)  # Filtrer sur la colonne ville
            proxy_model.setFilterFixedString("Paris")  # Afficher seulement Paris
            
            self.table_view.setModel(proxy_model)
            self.filter_btn.setText("Désactiver filtre")
    
    def on_selection_changed(self, selected, deselected):
        """Réaction aux changements de sélection"""
        selection = self.table_view.selectionModel()
        selected_rows = len(selection.selectedRows())
        print(f"Nombre de lignes sélectionnées: {selected_rows}")
    
    def on_double_click(self, index):
        """Réaction au double-clic"""
        if index.isValid():
            person = self.model.get_person(index.row())
            QMessageBox.information(
                self, 
                "Détails", 
                f"Personne: {person['prenom']} {person['nom']}\n"
                f"Âge: {person['age']} ans\n"
                f"Email: {person['email']}\n"
                f"Ville: {person['ville']}"
            )
```

### 3.2 Implémentation de QTreeView avec modèle hiérarchique

```python
class TreeNode:
    """Nœud pour structure arborescente"""
    
    def __init__(self, data: List[str], parent=None):
        self.data = data
        self.parent = parent
        self.children = []
    
    def add_child(self, child):
        """Ajoute un enfant"""
        child.parent = self
        self.children.append(child)
    
    def child_count(self):
        """Nombre d'enfants"""
        return len(self.children)
    
    def child(self, row: int):
        """Récupère un enfant par index"""
        if 0 <= row < len(self.children):
            return self.children[row]
        return None
    
    def row(self):
        """Position dans la liste des enfants du parent"""
        if self.parent:
            return self.parent.children.index(self)
        return 0

class TreeModel(QAbstractItemModel):
    """Modèle pour données hiérarchiques"""
    
    def __init__(self, headers: List[str]):
        super().__init__()
        self.headers = headers
        self.root_node = TreeNode(headers)
        self.setup_sample_data()
    
    def setup_sample_data(self):
        """Crée une structure d'exemple"""
        # Entreprise
        company = TreeNode(['Entreprise ABC', 'Siège social', '500 employés'])
        self.root_node.add_child(company)
        
        # Départements
        it_dept = TreeNode(['Informatique', 'Développement', '50 employés'])
        company.add_child(it_dept)
        
        hr_dept = TreeNode(['Ressources Humaines', 'Gestion du personnel', '10 employés'])
        company.add_child(hr_dept)
        
        sales_dept = TreeNode(['Ventes', 'Commerce', '30 employés'])
        company.add_child(sales_dept)
        
        # Équipes IT
        frontend_team = TreeNode(['Frontend', 'Interfaces utilisateur', '15 devs'])
        it_dept.add_child(frontend_team)
        
        backend_team = TreeNode(['Backend', 'Services et API', '20 devs'])
        it_dept.add_child(backend_team)
        
        # Développeurs Frontend
        dev1 = TreeNode(['Alice Martin', 'Senior Developer', 'React/Vue.js'])
        frontend_team.add_child(dev1)
        
        dev2 = TreeNode(['Bob Durand', 'Junior Developer', 'Angular'])
        frontend_team.add_child(dev2)
        
        # Développeurs Backend
        dev3 = TreeNode(['Claire Simon', 'Lead Developer', 'Python/Django'])
        backend_team.add_child(dev3)
        
        dev4 = TreeNode(['David Garcia', 'DevOps Engineer', 'Docker/K8s'])
        backend_team.add_child(dev4)
    
    # === Méthodes obligatoires pour QAbstractItemModel ===
    
    def index(self, row: int, column: int, parent=QModelIndex()):
        """Crée un index pour un élément"""
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()
        
        child_node = parent_node.child(row)
        if child_node:
            return self.createIndex(row, column, child_node)
        
        return QModelIndex()
    
    def parent(self, index):
        """Retourne l'index du parent"""
        if not index.isValid():
            return QModelIndex()
        
        child_node = index.internalPointer()
        parent_node = child_node.parent
        
        if parent_node == self.root_node or parent_node is None:
            return QModelIndex()
        
        return self.createIndex(parent_node.row(), 0, parent_node)
    
    def rowCount(self, parent=QModelIndex()):
        """Nombre de lignes (enfants)"""
        if parent.column() > 0:
            return 0
        
        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()
        
        return parent_node.child_count()
    
    def columnCount(self, parent=QModelIndex()):
        """Nombre de colonnes"""
        return len(self.headers)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Données pour un index"""
        if not index.isValid():
            return QVariant()
        
        node = index.internalPointer()
        
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() < len(node.data):
                return node.data[index.column()]
        
        elif role == Qt.ItemDataRole.DecorationRole and index.column() == 0:
            # Icônes selon le niveau
            if node.parent == self.root_node:
                return "🏢"  # Entreprise
            elif node.parent and node.parent.parent == self.root_node:
                return "🏛️"  # Département
            elif node.child_count() > 0:
                return "👥"  # Équipe
            else:
                return "👤"  # Personne
        
        return QVariant()
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """En-têtes de colonnes"""
        if (orientation == Qt.Orientation.Horizontal and 
            role == Qt.ItemDataRole.DisplayRole):
            if section < len(self.headers):
                return self.headers[section]
        
        return QVariant()
    
    def flags(self, index):
        """Drapeaux pour les éléments"""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

class TreeViewDemo(QMainWindow):
    """Démonstration de QTreeView"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vue arborescente hiérarchique")
        self.setup_ui()
        self.setup_tree()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)
        
        # Contrôles
        controls_layout = QHBoxLayout()
        
        expand_btn = QPushButton("Tout développer")
        expand_btn.clicked.connect(self.tree_view.expandAll)
        controls_layout.addWidget(expand_btn)
        
        collapse_btn = QPushButton("Tout réduire")
        collapse_btn.clicked.connect(self.tree_view.collapseAll)
        controls_layout.addWidget(collapse_btn)
        
        layout.addLayout(controls_layout)
    
    def setup_tree(self):
        """Configure la vue arborescente"""
        self.model = TreeModel(['Nom', 'Type', 'Détails'])
        self.tree_view.setModel(self.model)
        
        # Configuration de la vue
        self.tree_view.setRootIsDecorated(True)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        
        # Ajuster les colonnes
        self.tree_view.resizeColumnToContents(0)
        self.tree_view.resizeColumnToContents(1)
        
        # Développer le premier niveau
        self.tree_view.expandToDepth(1)
        
        # Connexions
        self.tree_view.clicked.connect(self.on_item_clicked)
    
    def on_item_clicked(self, index):
        """Réaction au clic sur un élément"""
        if index.isValid():
            node = index.internalPointer()
            level = self.get_node_level(node)
            
            print(f"Élément cliqué: {node.data[0]} (niveau {level})")
    
    def get_node_level(self, node):
        """Calcule le niveau d'un nœud"""
        level = 0
        current = node
        while current.parent and current.parent != self.model.root_node:
            level += 1
            current = current.parent
        return level
```

---

## 4. Modèles prédéfinis et QStandardItemModel

### 4.1 Utilisation de QStringListModel

```python
from PyQt6.QtCore import QStringListModel

class StringListDemo(QWidget):
    """Démonstration de QStringListModel"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStringListModel - Liste simple")
        self.setup_ui()
        self.setup_string_model()
    
    def setup_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Vue liste
        list_layout = QVBoxLayout()
        list_layout.addWidget(QLabel("Liste de tâches:"))
        
        self.list_view = QListView()
        list_layout.addWidget(self.list_view)
        
        layout.addLayout(list_layout)
        
        # Contrôles
        controls_layout = QVBoxLayout()
        
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Nouvelle tâche...")
        self.task_input.returnPressed.connect(self.add_task)
        controls_layout.addWidget(self.task_input)
        
        add_btn = QPushButton("Ajouter tâche")
        add_btn.clicked.connect(self.add_task)
        controls_layout.addWidget(add_btn)
        
        remove_btn = QPushButton("Supprimer sélection")
        remove_btn.clicked.connect(self.remove_selected)
        controls_layout.addWidget(remove_btn)
        
        clear_btn = QPushButton("Tout effacer")
        clear_btn.clicked.connect(self.clear_all)
        controls_layout.addWidget(clear_btn)
        
        controls_layout.addStretch()
        layout.addLayout(controls_layout)
    
    def setup_string_model(self):
        """Configure le modèle de chaînes"""
        initial_tasks = [
            "Réviser le cours PyQt6",
            "Faire les exercices pratiques", 
            "Implémenter l'architecture MVC",
            "Tester les modèles personnalisés",
            "Documenter le code"
        ]
        
        self.model = QStringListModel(initial_tasks)
        self.list_view.setModel(self.model)
        
        # Configuration de la vue
        self.list_view.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
    
    def add_task(self):
        """Ajoute une nouvelle tâche"""
        text = self.task_input.text().strip()
        if text:
            # Récupérer la liste actuelle
            string_list = self.model.stringList()
            string_list.append(text)
            
            # Mettre à jour le modèle
            self.model.setStringList(string_list)
            
            # Effacer le champ
            self.task_input.clear()
    
    def remove_selected(self):
        """Supprime l'élément sélectionné"""
        selection = self.list_view.selectionModel()
        if selection.hasSelection():
            index = selection.currentIndex()
            if index.isValid():
                self.model.removeRow(index.row())
    
    def clear_all(self):
        """Efface toutes les tâches"""
        self.model.setStringList([])
```

### 4.2 QStandardItemModel avancé

```python
class StandardItemModelDemo(QMainWindow):
    """Démonstration avancée de QStandardItemModel"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStandardItemModel - Fonctionnalités avancées")
        self.setup_ui()
        self.setup_standard_model()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Vues multiples du même modèle
        views_layout = QHBoxLayout()
        
        # Vue tableau
        table_layout = QVBoxLayout()
        table_layout.addWidget(QLabel("Vue Tableau:"))
        self.table_view = QTableView()
        table_layout.addWidget(self.table_view)
        views_layout.addLayout(table_layout)
        
        # Vue arbre
        tree_layout = QVBoxLayout()
        tree_layout.addWidget(QLabel("Vue Arbre:"))
        self.tree_view = QTreeView()
        tree_layout.addWidget(self.tree_view)
        views_layout.addLayout(tree_layout)
        
        layout.addLayout(views_layout)
        
        # Contrôles
        controls_layout = QHBoxLayout()
        
        add_parent_btn = QPushButton("Ajouter parent")
        add_parent_btn.clicked.connect(self.add_parent_item)
        controls_layout.addWidget(add_parent_btn)
        
        add_child_btn = QPushButton("Ajouter enfant")
        add_child_btn.clicked.connect(self.add_child_item)
        controls_layout.addWidget(add_child_btn)
        
        checkable_btn = QPushButton("Élément cochable")
        checkable_btn.clicked.connect(self.add_checkable_item)
        controls_layout.addWidget(checkable_btn)
        
        layout.addLayout(controls_layout)
    
    def setup_standard_model(self):
        """Configure le modèle standard"""
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(['Nom', 'Statut', 'Progression'])
        
        # Connecter aux deux vues
        self.table_view.setModel(self.model)
        self.tree_view.setModel(self.model)
        
        # Configuration des vues
        self.table_view.setAlternatingRowColors(True)
        self.tree_view.setAlternatingRowColors(True)
        
        # Données d'exemple
        self.create_sample_hierarchy()
        
        # Développer l'arbre
        self.tree_view.expandAll()
    
    def create_sample_hierarchy(self):
        """Crée une hiérarchie d'exemple"""
        # Projet principal
        project_item = QStandardItem("Projet PyQt6")
        project_item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DirIcon))
        
        status_item = QStandardItem("En cours")
        status_item.setForeground(QColor(255, 165, 0))  # Orange
        
        progress_item = QStandardItem("75%")
        progress_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.model.appendRow([project_item, status_item, progress_item])
        
        # Sous-tâches
        subtasks = [
            ("Interface utilisateur", "Terminé", "100%", QColor(0, 128, 0)),
            ("Modèles de données", "En cours", "60%", QColor(255, 165, 0)),
            ("Tests unitaires", "À faire", "0%", QColor(255, 0, 0))
        ]
        
        for name, status, progress, color in subtasks:
            subtask_item = QStandardItem(name)
            subtask_item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_FileIcon))
            
            status_sub = QStandardItem(status)
            status_sub.setForeground(color)
            
            progress_sub = QStandardItem(progress)
            progress_sub.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            project_item.appendRow([subtask_item, status_sub, progress_sub])
        
        # Élément cochable
        checkable_item = QStandardItem("Tâche optionnelle")
        checkable_item.setCheckable(True)
        checkable_item.setCheckState(Qt.CheckState.Checked)
        
        optional_status = QStandardItem("Optionnel")
        optional_progress = QStandardItem("—")
        
        self.model.appendRow([checkable_item, optional_status, optional_progress])
    
    def add_parent_item(self):
        """Ajoute un élément parent"""
        parent_item = QStandardItem("Nouveau projet")
        status_item = QStandardItem("Planifié")
        progress_item = QStandardItem("0%")
        
        self.model.appendRow([parent_item, status_item, progress_item])
    
    def add_child_item(self):
        """Ajoute un enfant à l'élément sélectionné"""
        selection = self.tree_view.selectionModel()
        if selection.hasSelection():
            index = selection.currentIndex()
            parent_item = self.model.itemFromIndex(index)
            
            if parent_item and parent_item.column() == 0:  # Première colonne
                child_item = QStandardItem("Nouvelle sous-tâche")
                child_status = QStandardItem("À faire")
                child_progress = QStandardItem("0%")
                
                parent_item.appendRow([child_item, child_status, child_progress])
                
                # Développer le parent
                parent_index = self.model.indexFromItem(parent_item)
                self.tree_view.expand(parent_index)
    
    def add_checkable_item(self):
        """Ajoute un élément avec case à cocher"""
        checkable_item = QStandardItem("Élément cochable")
        checkable_item.setCheckable(True)
        checkable_item.setCheckState(Qt.CheckState.Unchecked)
        
        # Connecter le signal de changement d'état
        checkable_item.itemChanged.connect(self.on_check_changed)
        
        status_item = QStandardItem("Variable")
        progress_item = QStandardItem("—")
        
        self.model.appendRow([checkable_item, status_item, progress_item])
    
    def on_check_changed(self, item):
        """Réaction au changement d'état de case à cocher"""
        if item.isCheckable():
            state = "Coché" if item.checkState() == Qt.CheckState.Checked else "Décoché"
            print(f"Élément '{item.text()}' est maintenant: {state}")
```

---

## 5. Délégués et édition personnalisée

### 5.1 Délégué personnalisé pour l'édition

```python
from PyQt6.QtWidgets import QStyledItemDelegate, QComboBox, QSpinBox, QDateEdit
from PyQt6.QtCore import QDate

class CustomDelegate(QStyledItemDelegate):
    """Délégué personnalisé pour différents types d'édition"""
    
    def createEditor(self, parent, option, index):
        """Crée l'éditeur approprié selon la colonne"""
        column = index.column()
        
        if column == 1:  # Colonne âge - SpinBox
            editor = QSpinBox(parent)
            editor.setRange(0, 120)
            editor.setSuffix(" ans")
            return editor
        
        elif column == 2:  # Colonne statut - ComboBox
            editor = QComboBox(parent)
            editor.addItems(["Actif", "Inactif", "En attente", "Suspendu"])
            return editor
        
        elif column == 3:  # Colonne date - DateEdit
            editor = QDateEdit(parent)
            editor.setDate(QDate.currentDate())
            editor.setCalendarPopup(True)
            return editor
        
        # Par défaut, utiliser l'éditeur standard
        return super().createEditor(parent, option, index)
    
    def setEditorData(self, editor, index):
        """Charge les données dans l'éditeur"""
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        
        if isinstance(editor, QSpinBox):
            try:
                editor.setValue(int(value))
            except (ValueError, TypeError):
                editor.setValue(0)
        
        elif isinstance(editor, QComboBox):
            text = str(value)
            index_pos = editor.findText(text)
            if index_pos >= 0:
                editor.setCurrentIndex(index_pos)
        
        elif isinstance(editor, QDateEdit):
            if isinstance(value, QDate):
                editor.setDate(value)
            else:
                editor.setDate(QDate.currentDate())
        
        else:
            super().setEditorData(editor, index)
    
    def setModelData(self, editor, model, index):
        """Sauvegarde les données de l'éditeur vers le modèle"""
        if isinstance(editor, QSpinBox):
            value = editor.value()
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        
        elif isinstance(editor, QComboBox):
            value = editor.currentText()
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        
        elif isinstance(editor, QDateEdit):
            value = editor.date()
            model.setData(index, value, Qt.ItemDataRole.EditRole)
        
        else:
            super().setModelData(editor, model, index)
    
    def updateEditorGeometry(self, editor, option, index):
        """Met à jour la géométrie de l'éditeur"""
        editor.setGeometry(option.rect)

class DelegateDemo(QMainWindow):
    """Démonstration des délégués personnalisés"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Délégués personnalisés")
        self.setup_ui()
        self.setup_delegate_model()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Instructions
        info_label = QLabel("""
Instructions:
• Colonne 0: Texte libre
• Colonne 1: Âge (SpinBox avec limite)
• Colonne 2: Statut (ComboBox prédéfini)
• Colonne 3: Date (DateEdit avec calendrier)

Double-cliquez pour éditer.
        """)
        layout.addWidget(info_label)
        
        # Vue avec délégué
        self.table_view = QTableView()
        layout.addWidget(self.table_view)
    
    def setup_delegate_model(self):
        """Configure le modèle et le délégué"""
        # Modèle avec données d'exemple
        self.model = QStandardItemModel(0, 4)
        self.model.setHorizontalHeaderLabels(['Nom', 'Âge', 'Statut', 'Date inscription'])
        
        # Données d'exemple
        sample_data = [
            ['Alice Dupont', 28, 'Actif', QDate(2023, 1, 15)],
            ['Bob Martin', 35, 'En attente', QDate(2023, 2, 20)],
            ['Claire Simon', 42, 'Inactif', QDate(2023, 3, 10)]
        ]
        
        for row_data in sample_data:
            row = []
            for value in row_data:
                item = QStandardItem(str(value))
                # Stocker la valeur originale pour l'édition
                if isinstance(value, (int, QDate)):
                    item.setData(value, Qt.ItemDataRole.EditRole)
                row.append(item)
            self.model.appendRow(row)
        
        # Appliquer le modèle à la vue
        self.table_view.setModel(self.model)
        
        # Installer le délégué personnalisé
        delegate = CustomDelegate()
        self.table_view.setItemDelegate(delegate)
        
        # Configuration de la vue
        self.table_view.resizeColumnsToContents()
        self.table_view.setAlternatingRowColors(True)
```

---

## 6. Synchronisation et mise à jour automatique

### 6.1 Observateur de modèle avancé

```python
class ModelObserver(QObject):
    """Observateur pour surveiller les changements de modèle"""
    
    # Signaux pour notifier les changements
    data_changed_signal = pyqtSignal(QModelIndex, QModelIndex)
    rows_inserted_signal = pyqtSignal(QModelIndex, int, int)
    rows_removed_signal = pyqtSignal(QModelIndex, int, int)
    
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.connect_signals()
        self.change_log = []
    
    def connect_signals(self):
        """Connecte aux signaux du modèle"""
        self.model.dataChanged.connect(self.on_data_changed)
        self.model.rowsInserted.connect(self.on_rows_inserted)
        self.model.rowsRemoved.connect(self.on_rows_removed)
        self.model.modelReset.connect(self.on_model_reset)
    
    def on_data_changed(self, top_left, bottom_right, roles=None):
        """Réaction aux changements de données"""
        change = {
            'type': 'data_changed',
            'timestamp': QTime.currentTime(),
            'top_left': (top_left.row(), top_left.column()),
            'bottom_right': (bottom_right.row(), bottom_right.column()),
            'roles': roles or []
        }
        self.change_log.append(change)
        self.data_changed_signal.emit(top_left, bottom_right)
        
        print(f"Données modifiées: lignes {top_left.row()}-{bottom_right.row()}, "
              f"colonnes {top_left.column()}-{bottom_right.column()}")
    
    def on_rows_inserted(self, parent, first, last):
        """Réaction à l'insertion de lignes"""
        change = {
            'type': 'rows_inserted',
            'timestamp': QTime.currentTime(),
            'parent': parent,
            'first': first,
            'last': last
        }
        self.change_log.append(change)
        self.rows_inserted_signal.emit(parent, first, last)
        
        print(f"Lignes insérées: {first}-{last}")
    
    def on_rows_removed(self, parent, first, last):
        """Réaction à la suppression de lignes"""
        change = {
            'type': 'rows_removed',
            'timestamp': QTime.currentTime(),
            'parent': parent,
            'first': first,
            'last': last
        }
        self.change_log.append(change)
        self.rows_removed_signal.emit(parent, first, last)
        
        print(f"Lignes supprimées: {first}-{last}")
    
    def on_model_reset(self):
        """Réaction à la réinitialisation du modèle"""
        change = {
            'type': 'model_reset',
            'timestamp': QTime.currentTime()
        }
        self.change_log.append(change)
        
        print("Modèle réinitialisé")
    
    def get_change_statistics(self):
        """Retourne les statistiques de changements"""
        stats = {}
        for change in self.change_log:
            change_type = change['type']
            stats[change_type] = stats.get(change_type, 0) + 1
        return stats

class SynchronizedViewsDemo(QMainWindow):
    """Démonstration de vues synchronisées"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vues synchronisées avec observateur")
        self.setup_ui()
        self.setup_synchronized_model()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Vue principale
        main_view_layout = QHBoxLayout()
        
        # Table principale
        self.main_table = QTableView()
        main_view_layout.addWidget(self.main_table)
        
        # Vue synchronisée
        self.sync_table = QTableView()
        main_view_layout.addWidget(self.sync_table)
        
        layout.addLayout(main_view_layout)
        
        # Log des changements
        self.change_log = QTextEdit()
        self.change_log.setMaximumHeight(150)
        layout.addWidget(self.change_log)
        
        # Contrôles
        controls_layout = QHBoxLayout()
        
        add_btn = QPushButton("Ajouter ligne")
        add_btn.clicked.connect(self.add_row)
        controls_layout.addWidget(add_btn)
        
        remove_btn = QPushButton("Supprimer sélection")
        remove_btn.clicked.connect(self.remove_selected)
        controls_layout.addWidget(remove_btn)
        
        stats_btn = QPushButton("Statistiques")
        stats_btn.clicked.connect(self.show_statistics)
        controls_layout.addWidget(stats_btn)
        
        layout.addLayout(controls_layout)
    
    def setup_synchronized_model(self):
        """Configure le modèle et les vues synchronisées"""
        # Modèle partagé
        self.model = PersonModel([
            {'prenom': 'Alice', 'nom': 'Dupont', 'age': 30, 'email': 'alice@test.com', 'ville': 'Paris'},
            {'prenom': 'Bob', 'nom': 'Martin', 'age': 25, 'email': 'bob@test.com', 'ville': 'Lyon'}
        ])
        
        # Connecter les deux vues au même modèle
        self.main_table.setModel(self.model)
        self.sync_table.setModel(self.model)
        
        # Configuration des vues
        for table in [self.main_table, self.sync_table]:
            table.setAlternatingRowColors(True)
            table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            table.resizeColumnsToContents()
        
        # Observateur de modèle
        self.observer = ModelObserver(self.model)
        
        # Connexions pour le log
        self.observer.data_changed_signal.connect(self.log_data_change)
        self.observer.rows_inserted_signal.connect(self.log_rows_inserted)
        self.observer.rows_removed_signal.connect(self.log_rows_removed)
    
    def add_row(self):
        """Ajoute une nouvelle ligne"""
        new_person = {
            'prenom': 'Nouveau',
            'nom': 'Utilisateur',
            'age': 20,
            'email': 'nouveau@test.com',
            'ville': 'Ville'
        }
        self.model.add_person(new_person)
    
    def remove_selected(self):
        """Supprime la ligne sélectionnée"""
        selection = self.main_table.selectionModel()
        if selection.hasSelection():
            row = selection.currentIndex().row()
            self.model.removeRows(row, 1)
    
    def log_data_change(self, top_left, bottom_right):
        """Log des changements de données"""
        timestamp = QTime.currentTime().toString("hh:mm:ss")
        message = f"[{timestamp}] Données modifiées: ({top_left.row()}, {top_left.column()})"
        self.change_log.append(message)
    
    def log_rows_inserted(self, parent, first, last):
        """Log des insertions de lignes"""
        timestamp = QTime.currentTime().toString("hh:mm:ss")
        message = f"[{timestamp}] Lignes ajoutées: {first}-{last}"
        self.change_log.append(message)
    
    def log_rows_removed(self, parent, first, last):
        """Log des suppressions de lignes"""
        timestamp = QTime.currentTime().toString("hh:mm:ss")
        message = f"[{timestamp}] Lignes supprimées: {first}-{last}"
        self.change_log.append(message)
    
    def show_statistics(self):
        """Affiche les statistiques de changements"""
        stats = self.observer.get_change_statistics()
        
        message = "Statistiques des changements:\n\n"
        for change_type, count in stats.items():
            message += f"• {change_type}: {count}\n"
        
        if not stats:
            message += "Aucun changement détecté."
        
        QMessageBox.information(self, "Statistiques", message)
```

---

## 7. Travaux pratiques

### 🚧 TP1 - Modèle de gestion de tâches
**Durée** : 30 minutes
- Créer un modèle personnalisé pour une application de gestion de tâches
- Implémenter l'ajout, suppression et modification de tâches avec priorités

### 🚧 TP2 - Vue hiérarchique de projets
**Durée** : 30 minutes  
- Développer une structure arborescente pour organiser projets/tâches/sous-tâches
- Utiliser QTreeView avec un modèle personnalisé hiérarchique

### 🚧 TP3 - Délégués d'édition avancés
**Durée** : 30 minutes
- Créer des délégués personnalisés pour différents types de données
- Implémenter validation et contraintes d'édition

### 🚧 TP4 - Synchronisation multi-vues
**Durée** : 30 minutes
- Créer une application avec plusieurs vues synchronisées du même modèle
- Implémenter un système de notifications de changements

---

## 8. Points clés à retenir

### ✅ Architecture MVC
- **Séparation claire** des responsabilités entre données, affichage et contrôle
- **Réutilisabilité** : un modèle peut servir plusieurs vues
- **Maintenabilité** améliorée grâce au découplage des composants

### ✅ Modèles personnalisés
- Hériter de `QAbstractTableModel` pour des besoins spécifiques
- Implémenter les méthodes obligatoires : `rowCount()`, `columnCount()`, `data()`
- Gérer les rôles d'affichage (`DisplayRole`, `EditRole`, etc.)

### ✅ Vues et interaction
- `QTableView` pour les données tabulaires avec tri et filtrage
- `QTreeView` pour les structures hiérarchiques
- Configuration fine de l'apparence et du comportement des vues

### ✅ Délégués et édition
- Personnaliser l'édition avec `QStyledItemDelegate`
- Créer des éditeurs spécialisés selon le type de données
- Validation des saisies et contraintes métier

### ✅ Synchronisation
- Les signaux du modèle permettent la mise à jour automatique des vues
- Observer les changements pour implémenter la logique métier
- Partage de modèles entre vues pour la cohérence des données

---

## Prochaine étape

Dans le **Chapitre 6 - Utilisation du Qt Designer**, nous découvrirons :
- L'interface et les outils du Qt Designer
- La création d'interfaces graphiques visuelles 
- L'intégration avec VSCode et la génération de code Python
- Les techniques de promotion de widgets et la personnalisation avancée
