# Chapitre 8 : Projets pratiques et intégration

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Développer une application PyQt6 complète de A à Z
- Appliquer les bonnes pratiques et patterns de développement Qt
- Structurer un projet Qt professionnel avec architecture modulaire
- Implémenter des tests unitaires et d'intégration pour PyQt6
- Déboguer efficacement les applications Qt complexes
- Packager et distribuer une application PyQt6 pour différentes plateformes
- Optimiser les performances et gérer la production

## Durée estimée : 4h00
- **Théorie** : 1h00
- **Travaux pratiques** : 3h00

---

## 1. Développement d'une application complète

### 1.1 Architecture du projet

```python
# Structure de projet professionnel recommandée:
"""
mon_projet_qt/
├── src/                          # Code source principal
│   ├── __init__.py
│   ├── main.py                   # Point d'entrée
│   ├── core/                     # Logique métier
│   │   ├── __init__.py
│   │   ├── models.py             # Modèles de données
│   │   ├── services.py           # Services métier
│   │   └── config.py             # Configuration
│   ├── gui/                      # Interface utilisateur
│   │   ├── __init__.py
│   │   ├── main_window.py        # Fenêtre principale
│   │   ├── dialogs/              # Boîtes de dialogue
│   │   ├── widgets/              # Widgets personnalisés
│   │   └── resources/            # Ressources Qt
│   └── utils/                    # Utilitaires
│       ├── __init__.py
│       ├── helpers.py
│       └── constants.py
├── ui/                           # Fichiers Qt Designer
│   ├── main_window.ui
│   └── dialogs/
├── resources/                    # Ressources externes
│   ├── icons/
│   ├── images/
│   └── translations/
├── tests/                        # Tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_gui.py
├── docs/                         # Documentation
├── requirements.txt              # Dépendances
├── pyproject.toml               # Configuration projet
└── README.md
"""

# Exemple de main.py structuré
import sys
import logging
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTranslator, QLocale
from src.gui.main_window import MainWindow
from src.core.config import AppConfig

def setup_logging():
    """Configure le système de logs"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def setup_application():
    """Configure l'application Qt"""
    app = QApplication(sys.argv)
    
    # Métadonnées de l'application
    app.setApplicationName(AppConfig.APP_NAME)
    app.setApplicationVersion(AppConfig.VERSION)
    app.setOrganizationName(AppConfig.ORGANIZATION)
    
    # Style et thème
    app.setStyle('Fusion')  # Style moderne
    
    return app

def load_translations(app):
    """Charge les traductions"""
    translator = QTranslator()
    locale = QLocale.system().name()
    
    translation_file = f"resources/translations/app_{locale}.qm"
    if Path(translation_file).exists():
        translator.load(translation_file)
        app.installTranslator(translator)
    
    return translator

def main():
    """Point d'entrée principal"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        app = setup_application()
        translator = load_translations(app)
        
        # Fenêtre principale
        window = MainWindow()
        window.show()
        
        logger.info("Application démarrée avec succès")
        return app.exec()
        
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 1.2 Exemple d'application : Gestionnaire de tâches

```python
# src/core/models.py
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional

class TaskStatus(Enum):
    TODO = "À faire"
    IN_PROGRESS = "En cours"
    DONE = "Terminé"
    CANCELLED = "Annulé"

class Priority(Enum):
    LOW = "Basse"
    MEDIUM = "Moyenne"
    HIGH = "Élevée"
    URGENT = "Urgente"

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.TODO
    priority: Priority = Priority.MEDIUM
    created_at: datetime = None
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

# src/core/services.py
from PyQt6.QtCore import QObject, pyqtSignal
from typing import List
import json
from pathlib import Path

class TaskService(QObject):
    """Service de gestion des tâches"""
    
    task_added = pyqtSignal(object)
    task_updated = pyqtSignal(object)
    task_deleted = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.tasks: List[Task] = []
        self.next_id = 1
        self.data_file = Path("tasks.json")
        self.load_tasks()
    
    def add_task(self, title: str, description: str = "", 
                 priority: Priority = Priority.MEDIUM) -> Task:
        """Ajoute une nouvelle tâche"""
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority
        )
        
        self.tasks.append(task)
        self.next_id += 1
        
        self.task_added.emit(task)
        self.save_tasks()
        
        return task
    
    def update_task(self, task_id: int, **kwargs) -> bool:
        """Met à jour une tâche"""
        task = self.get_task(task_id)
        if not task:
            return False
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        if kwargs.get('status') == TaskStatus.DONE and not task.completed_at:
            task.completed_at = datetime.now()
        
        self.task_updated.emit(task)
        self.save_tasks()
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Supprime une tâche"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.task_deleted.emit(task_id)
            self.save_tasks()
            return True
        return False
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Récupère une tâche par ID"""
        return next((t for t in self.tasks if t.id == task_id), None)
    
    def get_all_tasks(self) -> List[Task]:
        """Récupère toutes les tâches"""
        return self.tasks.copy()
    
    def save_tasks(self):
        """Sauvegarde les tâches"""
        data = []
        for task in self.tasks:
            task_dict = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status.name,
                'priority': task.priority.name,
                'created_at': task.created_at.isoformat(),
                'due_date': task.due_date.isoformat() if task.due_date else None,
                'completed_at': task.completed_at.isoformat() if task.completed_at else None
            }
            data.append(task_dict)
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_tasks(self):
        """Charge les tâches"""
        if not self.data_file.exists():
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            for task_dict in data:
                task = Task(
                    id=task_dict['id'],
                    title=task_dict['title'],
                    description=task_dict['description'],
                    status=TaskStatus[task_dict['status']],
                    priority=Priority[task_dict['priority']],
                    created_at=datetime.fromisoformat(task_dict['created_at']),
                    due_date=datetime.fromisoformat(task_dict['due_date']) if task_dict['due_date'] else None,
                    completed_at=datetime.fromisoformat(task_dict['completed_at']) if task_dict['completed_at'] else None
                )
                self.tasks.append(task)
                self.next_id = max(self.next_id, task.id + 1)
                
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")

# src/gui/main_window.py
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
    QPushButton, QTableView, QHeaderView, QMessageBox
)
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from src.core.services import TaskService
from src.core.models import Task, TaskStatus, Priority

class TaskTableModel(QAbstractTableModel):
    """Modèle pour l'affichage des tâches"""
    
    def __init__(self, task_service: TaskService):
        super().__init__()
        self.task_service = task_service
        self.tasks = []
        
        # Connexions aux signaux du service
        self.task_service.task_added.connect(self.refresh_data)
        self.task_service.task_updated.connect(self.refresh_data)
        self.task_service.task_deleted.connect(self.refresh_data)
        
        self.refresh_data()
    
    def refresh_data(self):
        """Actualise les données"""
        self.beginResetModel()
        self.tasks = self.task_service.get_all_tasks()
        self.endResetModel()
    
    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)
    
    def columnCount(self, parent=QModelIndex()):
        return 5  # ID, Titre, Statut, Priorité, Date création
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        
        task = self.tasks[index.row()]
        column = index.column()
        
        if role == Qt.ItemDataRole.DisplayRole:
            if column == 0:
                return task.id
            elif column == 1:
                return task.title
            elif column == 2:
                return task.status.value
            elif column == 3:
                return task.priority.value
            elif column == 4:
                return task.created_at.strftime("%d/%m/%Y")
        
        return None
    
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            headers = ["ID", "Titre", "Statut", "Priorité", "Créé le"]
            return headers[section]
        return None

class MainWindow(QMainWindow):
    """Fenêtre principale de l'application"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionnaire de Tâches")
        self.setGeometry(100, 100, 800, 600)
        
        # Services
        self.task_service = TaskService()
        
        # Interface
        self.setup_ui()
        self.setup_menu()
    
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Boutons d'action
        buttons_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Ajouter tâche")
        self.add_button.clicked.connect(self.add_task)
        buttons_layout.addWidget(self.add_button)
        
        self.edit_button = QPushButton("Modifier")
        self.edit_button.clicked.connect(self.edit_task)
        buttons_layout.addWidget(self.edit_button)
        
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.clicked.connect(self.delete_task)
        buttons_layout.addWidget(self.delete_button)
        
        layout.addLayout(buttons_layout)
        
        # Table des tâches
        self.table_view = QTableView()
        self.table_model = TaskTableModel(self.task_service)
        self.table_view.setModel(self.table_model)
        
        # Configuration de la table
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.horizontalHeader().setStretchLastSection(True)
        
        layout.addWidget(self.table_view)
    
    def setup_menu(self):
        """Configure les menus"""
        menubar = self.menuBar()
        
        # Menu Fichier
        file_menu = menubar.addMenu("&Fichier")
        file_menu.addAction("&Quitter", self.close, "Ctrl+Q")
        
        # Menu Aide
        help_menu = menubar.addMenu("&Aide")
        help_menu.addAction("À &propos", self.show_about)
    
    def add_task(self):
        """Ajoute une nouvelle tâche"""
        from src.gui.dialogs.task_dialog import TaskDialog
        
        dialog = TaskDialog(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            title, description, priority = dialog.get_task_data()
            self.task_service.add_task(title, description, priority)
    
    def edit_task(self):
        """Modifie la tâche sélectionnée"""
        selection = self.table_view.selectionModel()
        if not selection.hasSelection():
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner une tâche.")
            return
        
        row = selection.currentIndex().row()
        task = self.table_model.tasks[row]
        
        from src.gui.dialogs.task_dialog import TaskDialog
        
        dialog = TaskDialog(self, task)
        if dialog.exec() == dialog.DialogCode.Accepted:
            title, description, priority = dialog.get_task_data()
            self.task_service.update_task(
                task.id,
                title=title,
                description=description,
                priority=priority
            )
    
    def delete_task(self):
        """Supprime la tâche sélectionnée"""
        selection = self.table_view.selectionModel()
        if not selection.hasSelection():
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner une tâche.")
            return
        
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Voulez-vous vraiment supprimer cette tâche ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            row = selection.currentIndex().row()
            task = self.table_model.tasks[row]
            self.task_service.delete_task(task.id)
    
    def show_about(self):
        """Affiche la boîte À propos"""
        QMessageBox.about(
            self,
            "À propos",
            "Gestionnaire de Tâches v1.0\n\n"
            "Application de démonstration PyQt6\n"
            "Développée pour le cours Qt Programming"
        )
```

---

## 2. Bonnes pratiques et patterns

### 2.1 Patterns de conception Qt

```python
# Pattern Observer avec signaux Qt
class EventBus(QObject):
    """Bus d'événements centralisé"""
    
    # Événements globaux de l'application
    user_logged_in = pyqtSignal(str)  # username
    user_logged_out = pyqtSignal()
    theme_changed = pyqtSignal(str)   # theme_name
    language_changed = pyqtSignal(str)  # language_code
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Pattern Singleton pour configuration
class AppConfig:
    """Configuration globale de l'application (Singleton)"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.APP_NAME = "Mon Application"
        self.VERSION = "1.0.0"
        self.ORGANIZATION = "Mon Entreprise"
        self.DEBUG = False
        
        self._initialized = True

# Pattern Factory pour création de widgets
class WidgetFactory:
    """Factory pour créer des widgets standardisés"""
    
    @staticmethod
    def create_button(text, button_type="primary", icon=None):
        """Crée un bouton standardisé"""
        button = QPushButton(text)
        
        styles = {
            "primary": """
                QPushButton {
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """,
            "secondary": """
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #545b62;
                }
            """,
            "danger": """
                QPushButton {
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #c82333;
                }
            """
        }
        
        button.setStyleSheet(styles.get(button_type, styles["primary"]))
        
        if icon:
            button.setIcon(icon)
        
        return button
    
    @staticmethod
    def create_input_field(placeholder="", validator=None):
        """Crée un champ de saisie standardisé"""
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        
        if validator:
            line_edit.setValidator(validator)
        
        style = """
            QLineEdit {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #007bff;
                outline: none;
                box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
            }
        """
        line_edit.setStyleSheet(style)
        
        return line_edit

# Pattern Command pour annuler/refaire
class Command:
    """Interface pour les commandes"""
    
    def execute(self):
        raise NotImplementedError
    
    def undo(self):
        raise NotImplementedError

class AddTaskCommand(Command):
    """Commande d'ajout de tâche"""
    
    def __init__(self, task_service, title, description, priority):
        self.task_service = task_service
        self.title = title
        self.description = description
        self.priority = priority
        self.task_id = None
    
    def execute(self):
        task = self.task_service.add_task(self.title, self.description, self.priority)
        self.task_id = task.id
    
    def undo(self):
        if self.task_id:
            self.task_service.delete_task(self.task_id)

class CommandManager:
    """Gestionnaire de commandes avec undo/redo"""
    
    def __init__(self):
        self.history = []
        self.current_index = -1
    
    def execute_command(self, command):
        """Exécute une commande et l'ajoute à l'historique"""
        command.execute()
        
        # Supprimer les commandes après l'index actuel
        self.history = self.history[:self.current_index + 1]
        
        # Ajouter la nouvelle commande
        self.history.append(command)
        self.current_index += 1
    
    def undo(self):
        """Annule la dernière commande"""
        if self.current_index >= 0:
            command = self.history[self.current_index]
            command.undo()
            self.current_index -= 1
            return True
        return False
    
    def redo(self):
        """Refait la prochaine commande"""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            command = self.history[self.current_index]
            command.execute()
            return True
        return False
```

### 2.2 Gestion des erreurs et logging

```python
import logging
from functools import wraps
from PyQt6.QtWidgets import QMessageBox

def error_handler(func):
    """Décorateur pour gérer les erreurs"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger = logging.getLogger(func.__module__)
            logger.error(f"Erreur dans {func.__name__}: {e}", exc_info=True)
            
            # Afficher un message d'erreur à l'utilisateur
            if hasattr(args[0], 'parent') or hasattr(args[0], 'window'):
                parent = args[0].parent() if hasattr(args[0], 'parent') else args[0].window()
                QMessageBox.critical(
                    parent,
                    "Erreur",
                    f"Une erreur s'est produite :\n{str(e)}"
                )
    return wrapper

class ErrorReporter:
    """Système de rapport d'erreurs"""
    
    @staticmethod
    def setup_exception_handler():
        """Configure le gestionnaire d'exceptions global"""
        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            
            logger = logging.getLogger("global")
            logger.critical(
                "Exception non gérée",
                exc_info=(exc_type, exc_value, exc_traceback)
            )
            
            # Afficher une boîte de dialogue d'erreur critique
            app = QApplication.instance()
            if app:
                QMessageBox.critical(
                    None,
                    "Erreur Critique",
                    f"Une erreur critique s'est produite :\n\n"
                    f"{exc_type.__name__}: {exc_value}\n\n"
                    f"L'application va se fermer."
                )
        
        sys.excepthook = handle_exception

class PerformanceMonitor:
    """Monitoring des performances"""
    
    def __init__(self):
        self.timers = {}
    
    def start_timer(self, name):
        """Démarre un timer"""
        import time
        self.timers[name] = time.time()
    
    def end_timer(self, name):
        """Termine un timer et log le résultat"""
        if name in self.timers:
            import time
            duration = time.time() - self.timers[name]
            del self.timers[name]
            
            logger = logging.getLogger("performance")
            logger.info(f"{name} terminé en {duration:.3f}s")
            
            if duration > 1.0:  # Plus d'1 seconde
                logger.warning(f"Opération lente détectée: {name} ({duration:.3f}s)")
            
            return duration
        return None

def performance_monitor(operation_name):
    """Décorateur pour monitorer les performances"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            monitor = PerformanceMonitor()
            monitor.start_timer(operation_name)
            
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                monitor.end_timer(operation_name)
        
        return wrapper
    return decorator
```

---

## 3. Tests et debugging

### 3.1 Tests unitaires avec pytest

```python
# tests/test_models.py
import pytest
from datetime import datetime
from src.core.models import Task, TaskStatus, Priority

class TestTask:
    """Tests pour le modèle Task"""
    
    def test_task_creation(self):
        """Test de création d'une tâche"""
        task = Task(
            id=1,
            title="Test tâche",
            description="Description test"
        )
        
        assert task.id == 1
        assert task.title == "Test tâche"
        assert task.status == TaskStatus.TODO
        assert task.priority == Priority.MEDIUM
        assert isinstance(task.created_at, datetime)
    
    def test_task_completion(self):
        """Test de complétion d'une tâche"""
        task = Task(id=1, title="Test")
        
        # Marquer comme terminé
        task.status = TaskStatus.DONE
        task.completed_at = datetime.now()
        
        assert task.status == TaskStatus.DONE
        assert task.completed_at is not None
    
    @pytest.mark.parametrize("priority,expected", [
        (Priority.LOW, "Basse"),
        (Priority.MEDIUM, "Moyenne"),
        (Priority.HIGH, "Élevée"),
        (Priority.URGENT, "Urgente")
    ])
    def test_priority_values(self, priority, expected):
        """Test des valeurs de priorité"""
        assert priority.value == expected

# tests/test_services.py
import pytest
from unittest.mock import Mock, patch
from src.core.services import TaskService
from src.core.models import Priority

class TestTaskService:
    """Tests pour TaskService"""
    
    @pytest.fixture
    def task_service(self):
        """Fixture pour créer un service de test"""
        with patch.object(TaskService, 'load_tasks'):
            with patch.object(TaskService, 'save_tasks'):
                service = TaskService()
                service.tasks = []
                service.next_id = 1
                return service
    
    def test_add_task(self, task_service):
        """Test d'ajout de tâche"""
        # Mock du signal
        task_service.task_added = Mock()
        
        task = task_service.add_task("Test tâche", "Description", Priority.HIGH)
        
        assert task.id == 1
        assert task.title == "Test tâche"
        assert task.priority == Priority.HIGH
        assert len(task_service.tasks) == 1
        task_service.task_added.emit.assert_called_once_with(task)
    
    def test_update_task(self, task_service):
        """Test de mise à jour de tâche"""
        # Ajouter une tâche
        task = task_service.add_task("Test", "Desc")
        
        # Mock du signal
        task_service.task_updated = Mock()
        
        # Mettre à jour
        success = task_service.update_task(task.id, title="Nouveau titre")
        
        assert success
        assert task.title == "Nouveau titre"
        task_service.task_updated.emit.assert_called_once_with(task)
    
    def test_delete_task(self, task_service):
        """Test de suppression de tâche"""
        # Ajouter une tâche
        task = task_service.add_task("Test")
        
        # Mock du signal
        task_service.task_deleted = Mock()
        
        # Supprimer
        success = task_service.delete_task(task.id)
        
        assert success
        assert len(task_service.tasks) == 0
        task_service.task_deleted.emit.assert_called_once_with(task.id)

# tests/test_gui.py
import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from src.gui.main_window import MainWindow

@pytest.fixture(scope="session")
def qapp():
    """Fixture pour QApplication"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    # app.quit()  # Décommenté si nécessaire

class TestMainWindow:
    """Tests pour la fenêtre principale"""
    
    def test_window_creation(self, qapp):
        """Test de création de la fenêtre"""
        window = MainWindow()
        
        assert window.windowTitle() == "Gestionnaire de Tâches"
        assert window.task_service is not None
        assert window.table_view is not None
    
    def test_add_button_click(self, qapp, mocker):
        """Test du clic sur le bouton Ajouter"""
        window = MainWindow()
        
        # Mock de la boîte de dialogue
        mock_dialog = mocker.patch('src.gui.dialogs.task_dialog.TaskDialog')
        mock_dialog.return_value.exec.return_value = mock_dialog.return_value.DialogCode.Accepted
        mock_dialog.return_value.get_task_data.return_value = ("Test", "Desc", Priority.MEDIUM)
        
        # Simuler le clic
        QTest.mouseClick(window.add_button, Qt.MouseButton.LeftButton)
        
        # Vérifier que la boîte de dialogue a été appelée
        mock_dialog.assert_called_once()

# Configuration pytest (pytest.ini ou pyproject.toml)
"""
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--verbose",
    "--tb=short"
]
markers = [
    "slow: marque les tests lents",
    "integration: tests d'intégration",
    "gui: tests d'interface graphique"
]
"""
```

### 3.2 Debugging avancé

```python
class DebugHelper:
    """Utilitaires de debugging pour Qt"""
    
    @staticmethod
    def dump_widget_tree(widget, indent=0):
        """Affiche la hiérarchie des widgets"""
        space = "  " * indent
        print(f"{space}{widget.__class__.__name__}: {widget.objectName()}")
        
        for child in widget.children():
            if hasattr(child, 'children'):
                DebugHelper.dump_widget_tree(child, indent + 1)
    
    @staticmethod
    def monitor_signals(obj, signal_name):
        """Monitore les émissions d'un signal"""
        signal = getattr(obj, signal_name)
        
        def debug_handler(*args, **kwargs):
            print(f"Signal {signal_name} émis avec args: {args}, kwargs: {kwargs}")
        
        signal.connect(debug_handler)
    
    @staticmethod
    def log_paint_events(widget):
        """Log les événements de peinture"""
        original_paint_event = widget.paintEvent
        
        def debug_paint_event(event):
            print(f"paintEvent sur {widget.__class__.__name__}: {event.rect()}")
            original_paint_event(event)
        
        widget.paintEvent = debug_paint_event

class MemoryProfiler:
    """Profiler mémoire pour applications Qt"""
    
    def __init__(self):
        self.widgets_count = {}
    
    def snapshot(self):
        """Prend un instantané de l'utilisation mémoire"""
        import gc
        from collections import defaultdict
        
        widget_counts = defaultdict(int)
        
        for obj in gc.get_objects():
            if hasattr(obj, '__class__') and obj.__class__.__module__.startswith('PyQt6'):
                widget_counts[obj.__class__.__name__] += 1
        
        return dict(widget_counts)
    
    def compare_snapshots(self, before, after):
        """Compare deux instantanés"""
        all_classes = set(before.keys()) | set(after.keys())
        
        print("Différences d'objets Qt:")
        for class_name in sorted(all_classes):
            before_count = before.get(class_name, 0)
            after_count = after.get(class_name, 0)
            diff = after_count - before_count
            
            if diff != 0:
                print(f"  {class_name}: {before_count} → {after_count} ({diff:+d})")

# Exemple d'utilisation du debugging
def debug_session_example():
    """Exemple de session de debugging"""
    app = QApplication([])
    
    # Profiler mémoire
    profiler = MemoryProfiler()
    before = profiler.snapshot()
    
    # Créer l'interface
    window = MainWindow()
    
    # Debug de la hiérarchie
    print("Hiérarchie des widgets:")
    DebugHelper.dump_widget_tree(window)
    
    # Monitorer les signaux
    DebugHelper.monitor_signals(window.task_service, 'task_added')
    
    # Instantané après création
    after = profiler.snapshot()
    profiler.compare_snapshots(before, after)
    
    window.show()
    
    # Démarrer avec debugging activé
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    return app.exec()
```

---

## 4. Packaging et distribution

### 4.1 Configuration avec PyInstaller

```python
# build_config.py - Script de configuration de build
import PyInstaller.__main__
import sys
from pathlib import Path

def build_application():
    """Configure et lance PyInstaller"""
    
    # Chemins
    project_root = Path(__file__).parent
    main_script = project_root / "src" / "main.py"
    icon_file = project_root / "resources" / "icons" / "app.ico"
    
    # Arguments PyInstaller
    args = [
        str(main_script),
        '--name=GestionnaireTaches',
        '--windowed',  # Pas de console
        f'--icon={icon_file}',
        '--onefile',   # Un seul exécutable
        '--clean',     # Nettoyer avant build
        
        # Données à inclure
        f'--add-data={project_root}/ui;ui',
        f'--add-data={project_root}/resources;resources',
        
        # Modules cachés
        '--hidden-import=PyQt6.QtCore',
        '--hidden-import=PyQt6.QtWidgets',
        '--hidden-import=PyQt6.QtGui',
        
        # Exclusions
        '--exclude-module=tkinter',
        '--exclude-module=matplotlib',
        
        # Options de compilation
        '--optimize=2',
        '--strip',  # Supprimer les symboles de debug
        
        # Répertoire de sortie
        '--distpath=dist',
        '--workpath=build',
        '--specpath=build'
    ]
    
    # Ajouter des options spécifiques à l'OS
    if sys.platform == "win32":
        args.extend([
            '--version-file=version_info.txt',
            '--uac-admin',  # Si privilèges admin nécessaires
        ])
    elif sys.platform == "darwin":
        args.extend([
            '--osx-bundle-identifier=com.monentreprise.gestionnairetaches',
            '--target-arch=universal2',  # Support Intel + Apple Silicon
        ])
    
    print("Démarrage du build avec PyInstaller...")
    print(f"Arguments: {' '.join(args)}")
    
    PyInstaller.__main__.run(args)

def create_version_info():
    """Crée le fichier d'informations de version pour Windows"""
    version_info = """
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Mon Entreprise'),
        StringStruct(u'FileDescription', u'Gestionnaire de Tâches'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'GestionnaireTaches'),
        StringStruct(u'LegalCopyright', u'© 2024 Mon Entreprise'),
        StringStruct(u'OriginalFilename', u'GestionnaireTaches.exe'),
        StringStruct(u'ProductName', u'Gestionnaire de Tâches'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    
    with open('version_info.txt', 'w') as f:
        f.write(version_info)

if __name__ == "__main__":
    create_version_info()
    build_application()

# setup.py - Alternative avec setuptools
from setuptools import setup, find_packages

setup(
    name="gestionnaire-taches",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.4.0",
        "PyQt6-Qt6>=6.4.0",
        "PyQt6-sip>=13.4.0"
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-qt>=4.0.0',
            'pytest-mock>=3.10.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
            'mypy>=0.950'
        ],
        'build': [
            'PyInstaller>=5.0.0',
            'auto-py-to-exe>=2.20.0'  # Interface graphique pour PyInstaller
        ]
    },
    entry_points={
        'console_scripts': [
            'gestionnaire-taches=src.main:main',
        ],
    },
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Application de gestion de tâches avec PyQt6",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/votre-nom/gestionnaire-taches",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
```

### 4.2 Scripts de déploiement

```bash
#!/bin/bash
# deploy.sh - Script de déploiement multi-plateforme

set -e  # Arrêter en cas d'erreur

PROJECT_NAME="gestionnaire-taches"
VERSION="1.0.0"

echo "🚀 Déploiement de $PROJECT_NAME v$VERSION"

# Nettoyage
echo "🧹 Nettoyage..."
rm -rf build/ dist/ *.spec

# Installation des dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt
pip install PyInstaller

# Tests
echo "🧪 Exécution des tests..."
python -m pytest tests/ -v

# Build
echo "🔨 Build de l'application..."
python build_config.py

# Vérification
echo "✅ Vérification du build..."
if [ -f "dist/$PROJECT_NAME" ] || [ -f "dist/$PROJECT_NAME.exe" ]; then
    echo "✅ Build réussi!"
    
    # Taille du fichier
    if command -v du &> /dev/null; then
        echo "📊 Taille de l'exécutable: $(du -h dist/$PROJECT_NAME* | cut -f1)"
    fi
else
    echo "❌ Échec du build!"
    exit 1
fi

# Package pour distribution
echo "📦 Création du package de distribution..."
cd dist/
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows - Créer un ZIP
    powershell Compress-Archive -Path $PROJECT_NAME.exe -DestinationPath ../$PROJECT_NAME-$VERSION-windows.zip
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - Créer un DMG
    hdiutil create -volname "$PROJECT_NAME" -srcfolder $PROJECT_NAME.app -ov -format UDZO ../$PROJECT_NAME-$VERSION-macos.dmg
else
    # Linux - Créer un TAR.GZ
    tar -czf ../$PROJECT_NAME-$VERSION-linux.tar.gz $PROJECT_NAME
fi
cd ..

echo "🎉 Déploiement terminé!"
echo "📁 Fichiers de distribution disponibles dans le répertoire courant"
```

---

## 5. Travaux pratiques

### 🚧 TP1 - Application complète de gestion de contacts
**Durée** : 60 minutes
- Développer une application de carnet d'adresses avec toutes les fonctionnalités
- Implémenter la persistance, validation et interface complète

### 🚧 TP2 - Tests et debugging complets
**Durée** : 45 minutes  
- Écrire une suite de tests complète pour l'application
- Implémenter les outils de debugging et monitoring

### 🚧 TP3 - Optimisation et patterns avancés
**Durée** : 45 minutes
- Refactoriser avec les patterns de conception appropriés
- Optimiser les performances et la mémoire

### 🚧 TP4 - Packaging et distribution
**Durée** : 30 minutes
- Packager l'application pour votre plateforme
- Créer un installeur et tester la distribution

---

## 6. Points clés à retenir

### ✅ Architecture professionnelle
- **Structure modulaire** claire séparant logique métier et interface
- **Patterns de conception** appropriés pour la maintenabilité
- **Gestion d'erreurs** robuste avec logging complet

### ✅ Qualité de code
- **Tests automatisés** pour valider les fonctionnalités
- **Documentation** claire et à jour
- **Standards de codage** cohérents

### ✅ Déploiement
- **Packaging** automatisé avec PyInstaller
- **Distribution** multi-plateforme
- **Versioning** et gestion des releases

### ✅ Maintenance
- **Monitoring** des performances en production
- **Debugging** efficace avec outils appropriés
- **Évolutivité** préparée dès la conception

---

## Conclusion de la formation

Félicitations ! Vous avez maintenant acquis toutes les compétences nécessaires pour développer des applications PyQt6 professionnelles :

- ✅ **Maîtrise des concepts fondamentaux** de Qt et PyQt6
- ✅ **Création d'interfaces** modernes et responsives
- ✅ **Architecture MVC** pour des applications maintenables
- ✅ **Techniques avancées** (threads, dessin, internationalisation)
- ✅ **Développement professionnel** avec tests et déploiement

Vous êtes désormais prêt à créer des applications desktop robustes et élégantes avec Python et Qt !
