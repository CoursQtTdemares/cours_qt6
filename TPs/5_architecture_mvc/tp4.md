# TP4 - Persistance des données

**Durée** : 30 minutes

**Objectif** : Sauvegarder et charger les données automatiquement en JSON avec une architecture modulaire et gestion d'erreurs.

**Pré-requis** : TP1, TP2 et TP3 terminés et fonctionnels.

## 1) Fichier de données initial

- **Action** : Créez un fichier `database.json` à la racine avec quelques livres de test.
- **Piste** : Format JSON avec title, author, is_read pour chaque livre.
- **Validation** : Fichier JSON valide avec 2-3 livres d'exemple.

## 2) Configuration du chemin

- **Action** : Ajoutez une constante pour le chemin du fichier dans vos constantes.
- **Piste** : `DATABASE_JSON_FILE_PATH = WORKSPACE_DIR / "database.json"`.
- **Validation** : Constante définie et accessible.

## 3) Sérialisation Book

- **Action** : Ajoutez `to_dict()` et `from_dict()` à la classe Book.
- **Piste** : Convertir en dictionnaire avec title, author, is_read.
- **Validation** : Méthodes de conversion JSON fonctionnelles.

## 4) Module database

- **Action** : Créez un module `database.py` avec fonctions `load()` et `save()`.
- **Piste** : `load()` retourne `list[Book]`, `save()` prend `list[Book]`.
- **Validation** : Module séparé avec responsabilités claires.

## 5) Chargement au démarrage

- **Action** : Chargez les données dans le constructeur de LibraryMainWindow.
- **Piste** : `books = database.load()` puis `self.model = BookModel(books)`.
- **Validation** : Application démarre avec les données du fichier JSON.

## 6) Sauvegarde après actions

- **Action** : Ajoutez `database.save(self.model.books)` après chaque modification.
- **Piste** : Dans delete_book, mark_as_read, add_book de la vue.
- **Validation** : Sauvegarde automatique à chaque changement.

---

## Exercices supplémentaires

- **Sauvegarde manuelle** : Ajoutez menu "Fichier > Sauvegarder".
- **Backup automatique** : Créez des copies de sauvegarde horodatées.
- **Import/Export** : Permettez d'importer/exporter la bibliothèque.