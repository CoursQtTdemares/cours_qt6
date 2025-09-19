# TP1 - Modèle de base et première vue

**Durée** : 30 minutes

**Objectif** : Créer les fondations d'un gestionnaire de bibliothèque avec un modèle minimal et affichage via QListView.

**Pré-requis** : Chapitres 1-4 maîtrisés, notions de base sur l'architecture Model-View.

## 1) Créer le projet

- **Action** : Créez un projet `library_manager` avec un fichier `main.py`.
- **Piste** : Utilisez `uv init` puis `uv add PyQt6`.
- **Validation** : Projet créé avec PyQt6 installé et importable.

## 2) Classe Book simple

- **Action** : Créez une classe `Book` avec un attribut `title` uniquement.
- **Piste** : `def __init__(self, title: str): self.title = title`.
- **Validation** : Classe Book définie et instanciable.

## 3) Modèle BookModel de base

- **Action** : Créez `BookModel` héritant de `QAbstractListModel` avec 5 livres statiques.
- **Piste** : Implémentez `rowCount()` et `data()` pour `DisplayRole` uniquement.
- **Validation** : Modèle fonctionnel retournant le nombre et les titres des livres.

## 4) Interface MainWindow

- **Action** : Créez `LibraryMainWindow` héritant de `QMainWindow` avec titre et taille 400x300.
- **Piste** : `setWindowTitle()` et `setGeometry(100, 100, 400, 300)`.
- **Validation** : Fenêtre principale configurée et affichable.

## 5) Vue avec QListView

- **Action** : Ajoutez un `QListView` connecté au modèle avec `setModel()`.
- **Piste** : `self.book_view = QListView()` puis `self.book_view.setModel(self.book_model)`.
- **Validation** : Liste des 5 livres visible dans l'interface.

## 6) Layout et titre

- **Action** : Organisez l'interface avec layout vertical et ajoutez un titre "📚 Ma Bibliothèque".
- **Piste** : `QVBoxLayout` avec `QLabel` pour le titre et la liste view.
- **Validation** : Interface propre avec titre et liste des livres.

## 7) Application complète

- **Action** : Créez la fonction `main()` avec boucle d'événements PyQt6.
- **Piste** : `QApplication(sys.argv)`, `window.show()`, `sys.exit(app.exec())`.
- **Validation** : Application lance et affiche la fenêtre avec les livres.

## 8) Test de l'architecture

- **Action** : Modifiez temporairement la liste des livres et vérifiez la mise à jour automatique.
- **Piste** : Ajoutez un livre dans `__init__` du modèle et observez l'affichage.
- **Validation** : Compréhension de la connexion modèle-vue.

---

## Exercices supplémentaires

- **Style CSS** : Ajoutez des styles pour embellir le titre et la liste.
- **Données dynamiques** : Ajoutez des livres via du code Python.
- **Sélection** : Affichez le livre sélectionné dans la barre de statut.