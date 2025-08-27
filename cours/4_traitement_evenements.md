# Chapitre 4 : Traitement des événements

## Objectifs pédagogiques

À l'issue de ce chapitre, vous serez capable de :
- Comprendre le système d'événements Qt et la boucle d'événements
- Maîtriser le paradigme signaux/slots pour la communication entre objets
- Gérer les événements clavier, souris et fenêtre
- Créer des signaux personnalisés et des connexions avancées
- Implémenter des événements personnalisés et des filtres d'événements
- Déboguer et optimiser la gestion d'événements
- Appliquer les bonnes pratiques de programmation événementielle

## Durée estimée : 4h00
- **Théorie** : 2h00
- **Travaux pratiques** : 2h00

---

## 1. Le système d'événements Qt

### 1.1 Comprendre la boucle d'événements

Qt fonctionne sur un modèle événementiel où l'application répond aux interactions utilisateur et aux événements système :

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QCloseEvent
import sys

class EventSystemDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Système d'événements Qt")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()
        self.setup_event_monitoring()
    
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.event_label = QLabel("En attente d'événements...")
        self.event_label.setWordWrap(True)
        layout.addWidget(self.event_label)
        
        self.counter_label = QLabel("Événements traités: 0")
        layout.addWidget(self.counter_label)
        
        self.event_count = 0
    
    def setup_event_monitoring(self):
        """Configure la surveillance des événements"""
        # Timer pour démontrer les événements périodiques
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_event)
        self.timer.start(2000)  # Toutes les 2 secondes
    
    def log_event(self, event_type, details=""):
        """Enregistre un événement pour démonstration"""
        self.event_count += 1
        message = f"[{self.event_count}] {event_type}"
        if details:
            message += f": {details}"
        
        self.event_label.setText(message)
        self.counter_label.setText(f"Événements traités: {self.event_count}")
        print(f"Événement: {message}")
    
    def on_timer_event(self):
        """Gestionnaire d'événement timer"""
        self.log_event("Timer", "Événement périodique automatique")

def main():
    """Fonction principale avec boucle d'événements"""
    app = QApplication(sys.argv)
    
    # Configuration de l'application
    app.setApplicationName("Demo Événements")
    app.setApplicationVersion("1.0")
    
    # Création de la fenêtre
    window = EventSystemDemo()
    window.show()
    
    # Démarrage de la boucle d'événements
    # Cette boucle traite continuellement les événements
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
```

### 1.2 Types d'événements fondamentaux

```python
from PyQt6.QtCore import QEvent

class EventTypesDemo(QMainWindow):
    """Démonstration des différents types d'événements"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Types d'événements")
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)
        layout.addWidget(self.log_widget)
    
    def log(self, message):
        """Ajoute un message au log"""
        self.log_widget.append(f"[{QTime.currentTime().toString()}] {message}")
    
    # === Événements de souris ===
    def mousePressEvent(self, event: QMouseEvent):
        """Gestion des clics de souris"""
        button_names = {
            Qt.MouseButton.LeftButton: "Gauche",
            Qt.MouseButton.RightButton: "Droite", 
            Qt.MouseButton.MiddleButton: "Milieu"
        }
        
        button = button_names.get(event.button(), "Autre")
        position = event.position()
        self.log(f"Clic {button} à la position ({position.x():.0f}, {position.y():.0f})")
        
        super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        """Gestion du double-clic"""
        self.log("Double-clic détecté")
        super().mouseDoubleClickEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        """Gestion du mouvement de souris (uniquement si bouton enfoncé)"""
        if event.buttons() != Qt.MouseButton.NoButton:
            position = event.position()
            self.log(f"Glissement vers ({position.x():.0f}, {position.y():.0f})")
        super().mouseMoveEvent(event)
    
    # === Événements de clavier ===
    def keyPressEvent(self, event: QKeyEvent):
        """Gestion des touches pressées"""
        key = event.key()
        text = event.text()
        
        # Touches spéciales
        special_keys = {
            Qt.Key.Key_Escape: "Échap",
            Qt.Key.Key_Return: "Entrée",
            Qt.Key.Key_Space: "Espace",
            Qt.Key.Key_Tab: "Tab",
            Qt.Key.Key_Backspace: "Retour arrière"
        }
        
        if key in special_keys:
            self.log(f"Touche spéciale: {special_keys[key]}")
        elif text and text.isprintable():
            self.log(f"Caractère saisi: '{text}'")
        else:
            self.log(f"Touche: Code {key}")
        
        # Vérifier les modificateurs
        modifiers = event.modifiers()
        if modifiers & Qt.KeyboardModifier.ControlModifier:
            self.log("  + Ctrl enfoncé")
        if modifiers & Qt.KeyboardModifier.ShiftModifier:
            self.log("  + Shift enfoncé")
        if modifiers & Qt.KeyboardModifier.AltModifier:
            self.log("  + Alt enfoncé")
        
        super().keyPressEvent(event)
    
    # === Événements de fenêtre ===
    def resizeEvent(self, event):
        """Gestion du redimensionnement"""
        old_size = event.oldSize()
        new_size = event.size()
        self.log(f"Redimensionnement: {old_size.width()}x{old_size.height()} → {new_size.width()}x{new_size.height()}")
        super().resizeEvent(event)
    
    def closeEvent(self, event: QCloseEvent):
        """Gestion de la fermeture"""
        reply = QMessageBox.question(
            self, 
            "Confirmation",
            "Voulez-vous vraiment fermer l'application ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log("Fermeture acceptée")
            event.accept()
        else:
            self.log("Fermeture annulée")
            event.ignore()
```

---

## 2. Le paradigme signaux/slots

### 2.1 Concept fondamental

Le système signaux/slots est le mécanisme de communication central de Qt :

```python
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QSpinBox

class SignalSlotDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signaux et Slots")
        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Émetteur de signal: bouton
        self.button = QPushButton("Cliquez-moi!")
        layout.addWidget(self.button)
        
        # Récepteur: label
        self.click_label = QLabel("Nombre de clics: 0")
        layout.addWidget(self.click_label)
        
        # Émetteur: champ de texte
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Tapez du texte...")
        layout.addWidget(self.text_input)
        
        # Récepteur: label d'écho
        self.echo_label = QLabel("Écho: ")
        layout.addWidget(self.echo_label)
        
        # Émetteur: spinbox
        self.number_spin = QSpinBox()
        self.number_spin.setRange(0, 100)
        layout.addWidget(self.number_spin)
        
        # Récepteur: label de calcul
        self.calc_label = QLabel("Carré: 0")
        layout.addWidget(self.calc_label)
        
        self.click_count = 0
    
    def setup_connections(self):
        """Configure les connexions signaux/slots"""
        # Connexion basique: signal → slot
        self.button.clicked.connect(self.on_button_clicked)
        
        # Connexion avec paramètre: texte → affichage
        self.text_input.textChanged.connect(self.on_text_changed)
        
        # Connexion avec calcul: nombre → carré
        self.number_spin.valueChanged.connect(self.calculate_square)
        
        # Connexion lambda pour actions simples
        self.button.clicked.connect(
            lambda: print("Bouton cliqué - log depuis lambda")
        )
    
    @pyqtSlot()
    def on_button_clicked(self):
        """Slot décoré pour les clics de bouton"""
        self.click_count += 1
        self.click_label.setText(f"Nombre de clics: {self.click_count}")
        
        # Changer l'apparence après 5 clics
        if self.click_count >= 5:
            self.button.setStyleSheet("background-color: green; color: white;")
            self.button.setText("Merci!")
    
    @pyqtSlot(str)
    def on_text_changed(self, text):
        """Slot avec paramètre pour les changements de texte"""
        self.echo_label.setText(f"Écho: {text}")
        
        # Validation en temps réel
        if len(text) > 20:
            self.text_input.setStyleSheet("background-color: #ffcccc;")
            self.echo_label.setText("Écho: Texte trop long!")
        else:
            self.text_input.setStyleSheet("")
    
    @pyqtSlot(int)
    def calculate_square(self, value):
        """Slot de calcul avec validation"""
        square = value * value
        self.calc_label.setText(f"Carré: {square}")
        
        # Couleur selon la valeur
        if square > 1000:
            color = "red"
        elif square > 100:
            color = "orange"
        else:
            color = "green"
        
        self.calc_label.setStyleSheet(f"color: {color}; font-weight: bold;")
```

### 2.2 Signaux personnalisés

```python
class CustomSignalDemo(QObject):
    """Classe démontrant les signaux personnalisés"""
    
    # Définition de signaux personnalisés
    data_processed = pyqtSignal(str, int)  # Signal avec paramètres
    error_occurred = pyqtSignal(str)       # Signal d'erreur
    progress_updated = pyqtSignal(int)     # Signal de progression
    
    def __init__(self):
        super().__init__()
        self.processing = False
    
    def process_data(self, data_list):
        """Traite des données et émet des signaux"""
        if self.processing:
            self.error_occurred.emit("Traitement déjà en cours")
            return
        
        self.processing = True
        total = len(data_list)
        
        for i, item in enumerate(data_list):
            # Simulation de traitement
            QThread.msleep(100)  # Pause de 100ms
            
            # Émission du signal de progression
            progress = int((i + 1) / total * 100)
            self.progress_updated.emit(progress)
            
            # Émission du signal de données traitées
            self.data_processed.emit(f"Traité: {item}", i + 1)
        
        self.processing = False

class SignalReceiverWidget(QWidget):
    """Widget qui reçoit et affiche les signaux"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Réception de signaux personnalisés")
        self.setup_ui()
        self.setup_processor()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Zone d'affichage des messages
        self.message_area = QTextEdit()
        self.message_area.setReadOnly(True)
        layout.addWidget(self.message_area)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        
        # Bouton de lancement
        self.start_button = QPushButton("Démarrer le traitement")
        self.start_button.clicked.connect(self.start_processing)
        layout.addWidget(self.start_button)
    
    def setup_processor(self):
        """Configure le processeur et les connexions"""
        self.processor = CustomSignalDemo()
        
        # Connexions des signaux personnalisés
        self.processor.data_processed.connect(self.on_data_processed)
        self.processor.error_occurred.connect(self.on_error)
        self.processor.progress_updated.connect(self.on_progress_updated)
    
    @pyqtSlot(str, int)
    def on_data_processed(self, message, count):
        """Réception des données traitées"""
        self.message_area.append(f"[{count}] {message}")
    
    @pyqtSlot(str)
    def on_error(self, error_message):
        """Réception des erreurs"""
        self.message_area.append(f"❌ ERREUR: {error_message}")
    
    @pyqtSlot(int)
    def on_progress_updated(self, progress):
        """Mise à jour de la progression"""
        self.progress_bar.setValue(progress)
    
    def start_processing(self):
        """Lance le traitement des données"""
        test_data = ["Fichier1.txt", "Image2.jpg", "Document3.pdf", 
                    "Audio4.mp3", "Video5.mp4"]
        
        self.message_area.clear()
        self.progress_bar.setValue(0)
        self.processor.process_data(test_data)
```

---

## 3. Connexions et déconnexions avancées

### 3.1 Types de connexions

```python
from PyQt6.QtCore import Qt

class AdvancedConnectionsDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexions avancées")
        self.setup_ui()
        self.demonstrate_connections()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)
        
        # Boutons pour démonstration
        self.signal_button = QPushButton("Émettre signal")
        layout.addWidget(self.signal_button)
        
        self.connect_button = QPushButton("Connecter slots")
        self.connect_button.clicked.connect(self.connect_slots)
        layout.addWidget(self.connect_button)
        
        self.disconnect_button = QPushButton("Déconnecter slots")
        self.disconnect_button.clicked.connect(self.disconnect_slots)
        layout.addWidget(self.disconnect_button)
        
        self.clear_button = QPushButton("Effacer log")
        self.clear_button.clicked.connect(self.log_area.clear)
        layout.addWidget(self.clear_button)
    
    def demonstrate_connections(self):
        """Démontre différents types de connexions"""
        
        # 1. Connexion directe (par défaut)
        self.signal_button.clicked.connect(
            self.slot_direct,
            Qt.ConnectionType.DirectConnection
        )
        
        # 2. Connexion en file (queued) - utile pour le threading
        self.signal_button.clicked.connect(
            self.slot_queued,
            Qt.ConnectionType.QueuedConnection
        )
        
        # 3. Connexion automatique (Qt choisit)
        self.signal_button.clicked.connect(
            self.slot_auto,
            Qt.ConnectionType.AutoConnection
        )
        
        # 4. Connexion unique (se déconnecte après le premier appel)
        self.signal_button.clicked.connect(
            self.slot_once,
            Qt.ConnectionType.SingleShotConnection
        )
    
    def log(self, message):
        """Ajoute un message au log avec timestamp"""
        from PyQt6.QtCore import QTime
        timestamp = QTime.currentTime().toString("hh:mm:ss.zzz")
        self.log_area.append(f"[{timestamp}] {message}")
    
    @pyqtSlot()
    def slot_direct(self):
        """Slot avec connexion directe"""
        self.log("🔗 Slot DIRECT exécuté")
    
    @pyqtSlot()
    def slot_queued(self):
        """Slot avec connexion en file"""
        self.log("⏰ Slot QUEUED exécuté")
    
    @pyqtSlot()
    def slot_auto(self):
        """Slot avec connexion automatique"""
        self.log("🤖 Slot AUTO exécuté")
    
    @pyqtSlot()
    def slot_once(self):
        """Slot qui ne s'exécute qu'une fois"""
        self.log("1️⃣ Slot ONCE exécuté (ne se répétera plus)")
    
    def connect_slots(self):
        """Connexion dynamique de slots"""
        # Connexion d'un nouveau slot
        self.signal_button.clicked.connect(self.dynamic_slot)
        self.log("✅ Slot dynamique connecté")
    
    def disconnect_slots(self):
        """Déconnexion de slots"""
        # Déconnexion d'un slot spécifique
        try:
            self.signal_button.clicked.disconnect(self.dynamic_slot)
            self.log("❌ Slot dynamique déconnecté")
        except TypeError:
            self.log("⚠️ Slot dynamique n'était pas connecté")
    
    @pyqtSlot()
    def dynamic_slot(self):
        """Slot connecté/déconnecté dynamiquement"""
        self.log("🔄 Slot DYNAMIQUE exécuté")
```

### 3.2 Gestion des connexions multiples

```python
class MultiConnectionManager(QObject):
    """Gestionnaire de connexions multiples"""
    
    # Signal avec surcharge (overload)
    value_changed = pyqtSignal([int], [str], [float])
    
    def __init__(self):
        super().__init__()
        self.connections = []
        self.setup_connections()
    
    def setup_connections(self):
        """Configure les connexions multiples pour un même signal"""
        
        # Connexion du signal surchargé à différents slots
        self.value_changed[int].connect(self.handle_int_value)
        self.value_changed[str].connect(self.handle_str_value)
        self.value_changed[float].connect(self.handle_float_value)
        
        # Stockage des connexions pour gestion ultérieure
        self.connections.extend([
            self.value_changed[int],
            self.value_changed[str], 
            self.value_changed[float]
        ])
    
    @pyqtSlot(int)
    def handle_int_value(self, value):
        """Traite les valeurs entières"""
        print(f"Valeur entière reçue: {value}")
    
    @pyqtSlot(str)
    def handle_str_value(self, value):
        """Traite les valeurs textuelles"""
        print(f"Valeur textuelle reçue: '{value}'")
    
    @pyqtSlot(float)
    def handle_float_value(self, value):
        """Traite les valeurs décimales"""
        print(f"Valeur décimale reçue: {value:.2f}")
    
    def emit_values(self):
        """Émets différents types de valeurs"""
        self.value_changed[int].emit(42)
        self.value_changed[str].emit("Hello World")
        self.value_changed[float].emit(3.14159)
    
    def disconnect_all(self):
        """Déconnecte toutes les connexions gérées"""
        for signal in self.connections:
            signal.disconnect()
        self.connections.clear()
        print("Toutes les connexions ont été supprimées")
```

---

## 4. Événements personnalisés et filtres

### 4.1 Création d'événements personnalisés

```python
from PyQt6.QtCore import QEvent

class CustomEvent(QEvent):
    """Événement personnalisé"""
    
    # Type d'événement personnalisé (doit être > QEvent.User)
    CustomEventType = QEvent.Type(QEvent.Type.User + 1)
    
    def __init__(self, data):
        super().__init__(self.CustomEventType)
        self.data = data

class NotificationEvent(QEvent):
    """Événement de notification"""
    
    NotificationType = QEvent.Type(QEvent.Type.User + 2)
    
    def __init__(self, title, message, severity="info"):
        super().__init__(self.NotificationType)
        self.title = title
        self.message = message
        self.severity = severity

class CustomEventDemo(QMainWindow):
    """Démonstration des événements personnalisés"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Événements personnalisés")
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Zone d'affichage des événements
        self.event_display = QTextEdit()
        self.event_display.setReadOnly(True)
        layout.addWidget(self.event_display)
        
        # Boutons pour déclencher des événements
        send_custom_btn = QPushButton("Envoyer événement personnalisé")
        send_custom_btn.clicked.connect(self.send_custom_event)
        layout.addWidget(send_custom_btn)
        
        send_notification_btn = QPushButton("Envoyer notification")
        send_notification_btn.clicked.connect(self.send_notification_event)
        layout.addWidget(send_notification_btn)
    
    def send_custom_event(self):
        """Envoie un événement personnalisé"""
        data = {"timestamp": QTime.currentTime(), "value": 42}
        event = CustomEvent(data)
        QApplication.postEvent(self, event)
    
    def send_notification_event(self):
        """Envoie un événement de notification"""
        event = NotificationEvent(
            "Information",
            "Ceci est un exemple de notification personnalisée",
            "info"
        )
        QApplication.postEvent(self, event)
    
    def customEvent(self, event):
        """Gestionnaire d'événements personnalisés"""
        if event.type() == CustomEvent.CustomEventType:
            self.handle_custom_event(event)
        elif event.type() == NotificationEvent.NotificationType:
            self.handle_notification_event(event)
        else:
            super().customEvent(event)
    
    def handle_custom_event(self, event):
        """Traite les événements personnalisés"""
        data = event.data
        message = f"📅 Événement personnalisé reçu:\n"
        message += f"   Heure: {data['timestamp'].toString()}\n"
        message += f"   Valeur: {data['value']}\n"
        self.event_display.append(message)
    
    def handle_notification_event(self, event):
        """Traite les événements de notification"""
        icons = {
            "info": "ℹ️",
            "warning": "⚠️", 
            "error": "❌",
            "success": "✅"
        }
        
        icon = icons.get(event.severity, "📢")
        message = f"{icon} {event.title}: {event.message}\n"
        self.event_display.append(message)
```

### 4.2 Filtres d'événements

```python
class EventFilterDemo(QMainWindow):
    """Démonstration des filtres d'événements"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtres d'événements")
        self.setup_ui()
        self.setup_event_filters()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Champ de texte avec filtre
        self.filtered_input = QLineEdit()
        self.filtered_input.setPlaceholderText("Seulement des chiffres autorisés")
        layout.addWidget(self.filtered_input)
        
        # Bouton avec filtre de double-clic
        self.protected_button = QPushButton("Double-cliquez pour activer")
        layout.addWidget(self.protected_button)
        
        # Zone de log
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)
    
    def setup_event_filters(self):
        """Configure les filtres d'événements"""
        # Installer des filtres sur les widgets
        self.filtered_input.installEventFilter(self)
        self.protected_button.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        """Filtre principal pour tous les événements"""
        
        # Filtre pour le champ de texte (seulement les chiffres)
        if obj == self.filtered_input:
            if event.type() == QEvent.Type.KeyPress:
                if self.filter_numeric_input(event):
                    return True  # Événement bloqué
        
        # Filtre pour le bouton (protection contre clic simple)
        elif obj == self.protected_button:
            if event.type() == QEvent.Type.MouseButtonPress:
                if self.filter_button_click(event):
                    return True  # Événement bloqué
        
        # Laisser passer l'événement normalement
        return super().eventFilter(obj, event)
    
    def filter_numeric_input(self, event):
        """Filtre pour autoriser seulement les chiffres"""
        key = event.key()
        text = event.text()
        
        # Autoriser les touches de contrôle
        control_keys = [
            Qt.Key.Key_Backspace, Qt.Key.Key_Delete, Qt.Key.Key_Left,
            Qt.Key.Key_Right, Qt.Key.Key_Home, Qt.Key.Key_End,
            Qt.Key.Key_Tab
        ]
        
        if key in control_keys:
            return False  # Laisser passer
        
        # Autoriser seulement les chiffres
        if text and not text.isdigit():
            self.log_area.append(f"❌ Caractère '{text}' bloqué (non numérique)")
            return True  # Bloquer l'événement
        
        return False  # Laisser passer
    
    def filter_button_click(self, event):
        """Filtre pour exiger un double-clic"""
        if event.button() == Qt.MouseButton.LeftButton:
            # Vérifier si c'est un simple clic
            current_time = QTime.currentTime()
            
            if not hasattr(self, 'last_click_time'):
                self.last_click_time = current_time
                self.log_area.append("⚠️ Simple clic détecté. Double-cliquez pour activer.")
                return True  # Bloquer le simple clic
            
            # Calculer le délai depuis le dernier clic
            elapsed = self.last_click_time.msecsTo(current_time)
            self.last_click_time = current_time
            
            if elapsed < 500:  # Double-clic dans les 500ms
                self.log_area.append("✅ Double-clic validé! Action autorisée.")
                self.protected_button.setText("Activé!")
                return False  # Laisser passer
            else:
                self.log_area.append("⚠️ Délai trop long. Double-cliquez rapidement.")
                return True  # Bloquer
        
        return False
```

---

## 5. Gestion d'événements complexes

### 5.1 Événements de glisser-déposer

```python
from PyQt6.QtCore import QMimeData
from PyQt6.QtGui import QDrag, QPainter
from PyQt6.QtWidgets import QLabel

class DragDropDemo(QWidget):
    """Démonstration du glisser-déposer"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glisser-Déposer")
        self.setAcceptDrops(True)  # Autoriser le dépôt
        self.setup_ui()
    
    def setup_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Zone source (draggable)
        self.source_area = DragLabel("📄 Glissez-moi!")
        self.source_area.setStyleSheet("""
            border: 2px solid blue;
            padding: 20px;
            background-color: lightblue;
            text-align: center;
        """)
        layout.addWidget(self.source_area)
        
        # Zone cible (drop zone)
        self.target_area = QLabel("🎯 Déposez ici!")
        self.target_area.setStyleSheet("""
            border: 2px dashed gray;
            padding: 20px;
            background-color: lightgray;
            text-align: center;
        """)
        self.target_area.setAcceptDrops(True)
        layout.addWidget(self.target_area)
        
        # Zone de log
        self.log_area = QTextEdit()
        self.log_area.setMaximumHeight(100)
        layout.addWidget(self.log_area)
    
    def dragEnterEvent(self, event):
        """Événement d'entrée du glisser"""
        if event.mimeData().hasText():
            event.acceptProposedAction()
            self.log_area.append("🔵 Glisser entré dans la zone")
        else:
            event.ignore()
    
    def dragMoveEvent(self, event):
        """Événement de mouvement du glisser"""
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        """Événement de dépôt"""
        if event.mimeData().hasText():
            text = event.mimeData().text()
            self.target_area.setText(f"✅ Reçu: {text}")
            self.log_area.append(f"🎯 Dépôt réussi: {text}")
            event.acceptProposedAction()
        else:
            event.ignore()

class DragLabel(QLabel):
    """Label qui peut être glissé"""
    
    def __init__(self, text):
        super().__init__(text)
        self.original_text = text
    
    def mousePressEvent(self, event):
        """Début du glisser"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.position().toPoint()
    
    def mouseMoveEvent(self, event):
        """Gestion du glisser"""
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        
        if not hasattr(self, 'drag_start_position'):
            return
        
        # Vérifier la distance minimale pour commencer le glisser
        if ((event.position().toPoint() - self.drag_start_position).manhattanLength() < 
            QApplication.startDragDistance()):
            return
        
        # Créer l'objet de glisser
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.original_text)
        drag.setMimeData(mime_data)
        
        # Exécuter le glisser
        drop_action = drag.exec(Qt.DropAction.MoveAction)
        
        if drop_action == Qt.DropAction.MoveAction:
            self.setText("📤 Glissé!")
```

### 5.2 Événements de timer avancés

```python
class AdvancedTimerDemo(QWidget):
    """Démonstration des timers avancés"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timers avancés")
        self.setup_ui()
        self.setup_timers()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Affichage du temps
        self.time_display = QLabel("00:00:00")
        self.time_display.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.time_display)
        
        # Contrôles
        controls_layout = QHBoxLayout()
        
        self.start_button = QPushButton("Démarrer")
        self.start_button.clicked.connect(self.start_timer)
        controls_layout.addWidget(self.start_button)
        
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_timer)
        controls_layout.addWidget(self.pause_button)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        controls_layout.addWidget(self.reset_button)
        
        layout.addLayout(controls_layout)
        
        # Zone d'événements
        self.events_area = QTextEdit()
        self.events_area.setMaximumHeight(150)
        layout.addWidget(self.events_area)
    
    def setup_timers(self):
        """Configure différents types de timers"""
        # Timer principal (1 seconde)
        self.main_timer = QTimer()
        self.main_timer.timeout.connect(self.update_display)
        self.main_timer.setInterval(1000)  # 1 seconde
        
        # Timer de notification (5 secondes)
        self.notification_timer = QTimer()
        self.notification_timer.timeout.connect(self.show_notification)
        self.notification_timer.setInterval(5000)  # 5 secondes
        
        # Timer single-shot pour actions différées
        self.delayed_timer = QTimer()
        self.delayed_timer.setSingleShot(True)
        self.delayed_timer.timeout.connect(self.delayed_action)
        
        # Variables de temps
        self.elapsed_seconds = 0
        self.is_running = False
    
    def start_timer(self):
        """Démarre le chronomètre"""
        if not self.is_running:
            self.main_timer.start()
            self.notification_timer.start()
            self.is_running = True
            
            self.events_area.append("▶️ Chronomètre démarré")
            
            # Programmer une action dans 10 secondes
            self.delayed_timer.start(10000)
            self.events_area.append("⏰ Action programmée dans 10 secondes")
    
    def pause_timer(self):
        """Met en pause ou reprend le chronomètre"""
        if self.is_running:
            self.main_timer.stop()
            self.notification_timer.stop()
            self.delayed_timer.stop()
            self.is_running = False
            self.events_area.append("⏸️ Chronomètre mis en pause")
        else:
            self.start_timer()
    
    def reset_timer(self):
        """Remet à zéro le chronomètre"""
        self.main_timer.stop()
        self.notification_timer.stop()
        self.delayed_timer.stop()
        self.elapsed_seconds = 0
        self.is_running = False
        self.update_display()
        self.events_area.append("🔄 Chronomètre remis à zéro")
    
    def update_display(self):
        """Met à jour l'affichage du temps"""
        self.elapsed_seconds += 1
        
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.time_display.setText(time_str)
    
    def show_notification(self):
        """Affiche une notification périodique"""
        self.events_area.append(f"🔔 Notification: {self.elapsed_seconds} secondes écoulées")
    
    def delayed_action(self):
        """Action exécutée après un délai"""
        self.events_area.append("🎯 Action différée exécutée!")
        QMessageBox.information(self, "Timer", "Action programmée exécutée!")
```

---

## 6. Débogage et optimisation des événements

### 6.1 Outils de débogage

```python
class EventDebugger(QObject):
    """Débogueur d'événements pour analyser les performances"""
    
    def __init__(self, target_widget):
        super().__init__()
        self.target = target_widget
        self.event_counts = {}
        self.start_time = QTime.currentTime()
        
        # Installer le filtre de débogage
        target_widget.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        """Filtre de débogage qui compte tous les événements"""
        event_type = event.type()
        
        # Compter les événements
        if event_type in self.event_counts:
            self.event_counts[event_type] += 1
        else:
            self.event_counts[event_type] = 1
        
        # Logger les événements critiques
        critical_events = [
            QEvent.Type.Paint,
            QEvent.Type.Resize,
            QEvent.Type.MouseButtonPress,
            QEvent.Type.KeyPress
        ]
        
        if event_type in critical_events:
            elapsed = self.start_time.msecsTo(QTime.currentTime())
            print(f"[{elapsed}ms] {event_type.name} sur {obj.__class__.__name__}")
        
        return False  # Ne pas bloquer les événements
    
    def get_statistics(self):
        """Retourne les statistiques d'événements"""
        total_events = sum(self.event_counts.values())
        elapsed = self.start_time.msecsTo(QTime.currentTime())
        
        stats = {
            'total_events': total_events,
            'elapsed_ms': elapsed,
            'events_per_second': total_events / (elapsed / 1000) if elapsed > 0 else 0,
            'event_breakdown': self.event_counts.copy()
        }
        
        return stats
    
    def print_report(self):
        """Affiche un rapport de débogage"""
        stats = self.get_statistics()
        
        print("\n" + "="*50)
        print("RAPPORT DE DÉBOGAGE D'ÉVÉNEMENTS")
        print("="*50)
        print(f"Durée: {stats['elapsed_ms']}ms")
        print(f"Total d'événements: {stats['total_events']}")
        print(f"Événements/seconde: {stats['events_per_second']:.2f}")
        print("\nRépartition par type:")
        
        for event_type, count in sorted(stats['event_breakdown'].items(), 
                                      key=lambda x: x[1], reverse=True):
            percentage = (count / stats['total_events']) * 100
            print(f"  {event_type.name}: {count} ({percentage:.1f}%)")

class PerformanceTestWidget(QWidget):
    """Widget pour tester les performances d'événements"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test de performance des événements")
        self.setup_ui()
        self.setup_debugger()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Zone de test avec beaucoup d'événements
        self.test_area = QTextEdit()
        self.test_area.setPlainText("Tapez ici pour générer des événements...")
        layout.addWidget(self.test_area)
        
        # Boutons de test
        buttons_layout = QHBoxLayout()
        
        spam_button = QPushButton("Spam d'événements")
        spam_button.clicked.connect(self.spam_events)
        buttons_layout.addWidget(spam_button)
        
        report_button = QPushButton("Rapport de débogage")
        report_button.clicked.connect(self.show_debug_report)
        buttons_layout.addWidget(report_button)
        
        layout.addLayout(buttons_layout)
    
    def setup_debugger(self):
        """Configure le débogueur d'événements"""
        self.debugger = EventDebugger(self)
    
    def spam_events(self):
        """Génère artificiellement beaucoup d'événements"""
        for i in range(100):
            # Simuler des événements de redimensionnement
            self.resize(self.width() + 1, self.height())
            self.resize(self.width() - 1, self.height())
            
            # Forcer le traitement des événements
            QApplication.processEvents()
    
    def show_debug_report(self):
        """Affiche le rapport de débogage"""
        self.debugger.print_report()
        
        # Afficher aussi dans une boîte de dialogue
        stats = self.debugger.get_statistics()
        message = f"""Statistiques d'événements:

Durée: {stats['elapsed_ms']}ms
Total: {stats['total_events']} événements
Fréquence: {stats['events_per_second']:.2f} événements/seconde

Top 5 des événements:"""
        
        top_events = sorted(stats['event_breakdown'].items(), 
                          key=lambda x: x[1], reverse=True)[:5]
        
        for event_type, count in top_events:
            percentage = (count / stats['total_events']) * 100
            message += f"\n• {event_type.name}: {count} ({percentage:.1f}%)"
        
        QMessageBox.information(self, "Rapport de performance", message)
```

---

## 7. Travaux pratiques

### 🚧 TP1 - Gestionnaire d'événements interactif
**Durée** : 30 minutes
- Créer une application qui capture et affiche tous types d'événements
- Implémenter des filtres d'événements personnalisés

### 🚧 TP2 - Système de signaux personnalisés
**Durée** : 30 minutes  
- Développer un système de communication entre composants
- Créer des signaux avec paramètres multiples et gestion d'erreurs

### 🚧 TP3 - Interface glisser-déposer
**Durée** : 30 minutes
- Implémenter une interface de gestion de fichiers avec glisser-déposer
- Gérer différents types de données et validations

### 🚧 TP4 - Application multi-timer avancée
**Durée** : 30 minutes
- Créer une application de gestion de timers multiples
- Intégrer notifications, événements programmés et sauvegarde d'état

---

## 8. Points clés à retenir

### ✅ Système d'événements Qt
- La boucle d'événements est le cœur de toute application Qt
- Chaque interaction génère des événements qui peuvent être capturés et traités
- Les filtres d'événements permettent un contrôle fin du comportement

### ✅ Paradigme signaux/slots
- Mécanisme de communication type-safe et découplé
- Les slots peuvent être des méthodes Python normales ou décorées avec `@pyqtSlot`
- Les connexions peuvent être configurées avec différents types (Direct, Queued, etc.)

### ✅ Événements personnalisés
- Permettent d'étendre le système d'événements pour des besoins spécifiques
- Utilisation de `QApplication.postEvent()` pour l'envoi asynchrone
- Implémentation via `customEvent()` dans les widgets récepteurs

### ✅ Optimisation et débogage
- Surveiller la fréquence des événements pour détecter les problèmes de performance
- Utiliser les filtres d'événements avec parcimonie pour éviter les ralentissements
- Préférer les signaux/slots aux événements quand c'est possible

---

## Prochaine étape

Dans le **Chapitre 5 - Architecture MVC en Qt**, nous découvrirons :
- Les concepts fondamentaux de l'architecture Modèle-Vue-Contrôleur
- L'implémentation de modèles de données avec QAbstractTableModel
- La création de vues personnalisées avec QTableView et QTreeView
- Les techniques avancées de liaison de données et de mise à jour automatique
