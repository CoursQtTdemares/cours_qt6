# TP4 - Persistance des données

**Durée** : 30 minutes

**Objectif** : Sauvegarder et charger les données automatiquement en JSON avec gestion d'erreurs et compteur temps réel.

**Pré-requis** : TP1, TP2 et TP3 terminés et fonctionnels.

## 1) Imports pour persistance

- **Action** : Ajoutez les imports `json` et `os` au début du fichier.
- **Piste** : `import json, os` en haut du fichier.
- **Validation** : Imports ajoutés sans erreur.

## 2) Sérialisation Book

- **Action** : Ajoutez `to_dict()` et `from_dict()` à la classe Book.
- **Piste** : Convertir en dictionnaire avec title, author, is_read.
- **Validation** : Méthodes de conversion JSON fonctionnelles.

## 3) Sauvegarde JSON

- **Action** : Implémentez `save_to_json()` dans BookModel avec gestion d'erreurs.
- **Piste** : Utilisez `json.dump()` avec `ensure_ascii=False`.
- **Validation** : Fichier bibliotheque.json créé et lisible.

## 4) Chargement JSON

- **Action** : Implémentez `load_from_json()` avec signaux `beginResetModel()`.
- **Piste** : Utilisez `beginResetModel()` → chargement → `endResetModel()`.
- **Validation** : Données rechargées automatiquement au démarrage.

## 5) Sauvegarde automatique

- **Action** : Ajoutez `self.save_to_json()` à la fin de add_book, remove_book et mark_as_read.
- **Piste** : Ligne finale de chaque méthode de modification.
- **Validation** : Sauvegarde automatique à chaque modification.

## 6) Chargement au démarrage

- **Action** : Appelez `load_from_json()` dans __init__ de LibraryMainWindow.
- **Piste** : Après création du modèle : `self.book_model.load_from_json()`.
- **Validation** : Application restore les données précédentes.

## 7) Compteur de livres

- **Action** : Ajoutez un QLabel affichant "📊 X livres (Y lus, Z non lus)".
- **Piste** : `self.count_label = QLabel()` et méthode `update_count()`.
- **Validation** : Statistiques visibles en temps réel.

## 8) Mise à jour du compteur

- **Action** : Appelez `update_count()` après chaque modification (ajout/suppression/statut).
- **Piste** : Ajoutez l'appel dans toutes les méthodes de la fenêtre qui modifient.
- **Validation** : Compteur mis à jour automatiquement.

---

## Exercices supplémentaires

- **Sauvegarde manuelle** : Ajoutez menu "Fichier > Sauvegarder".
- **Backup automatique** : Créez des copies de sauvegarde horodatées.
- **Import/Export** : Permettez d'importer/exporter la bibliothèque.