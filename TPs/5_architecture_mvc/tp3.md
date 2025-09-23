# TP3 - Enrichissement visuel avec les rôles

**Durée** : 30 minutes

**Objectif** : Utiliser les rôles pour améliorer l'affichage avec auteur, statut de lecture, couleurs et icônes.

**Pré-requis** : TP1 et TP2 terminés et fonctionnels.

## 1) Extension de la classe Book

- **Action** : Ajoutez `author` et `is_read` (booléen) à la classe Book.
- **Piste** : `def __init__(self, title: str, author: str = "Auteur inconnu"): ...`
- **Validation** : Classe Book étendue avec auteur et statut de lecture.

## 2) Données initiales enrichies

- **Action** : Mettez à jour les 5 livres avec auteur et statut dans `BookModel`.
- **Piste** : `Book("Le Petit Prince", "Antoine de Saint-Exupéry")`.
- **Validation** : Liste initiale avec auteurs définis.

## 3) DisplayRole enrichi

- **Action** : Modifiez `data()` pour afficher "Titre par Auteur" avec `match/case`.
- **Piste** : `match role: case Qt.ItemDataRole.DisplayRole: return f"{book.title} par {book.author}"`.
- **Validation** : Format "Titre par Auteur" affiché pour chaque livre.

## 4) ForegroundRole pour les couleurs

- **Action** : Ajoutez couleur grise pour livres lus, noire pour non lus.
- **Piste** : Utilisez `QColor(128, 128, 128)` pour le gris.
- **Validation** : Différenciation visuelle par couleur selon statut.

## 5) FontRole pour la typographie

- **Action** : Livres non lus en gras, livres lus en police normale.
- **Piste** : `font.setBold(True)` selon `book.is_read`.
- **Validation** : Police différente selon le statut de lecture.

## 6) Bouton "Marquer comme lu"

- **Action** : Ajoutez bouton vert "Marquer comme lu" à côté de supprimer.
- **Piste** : Style CSS avec background-color: #27ae60.
- **Validation** : Bouton vert visible avec style moderne.

## 7) Méthode de changement de statut

- **Action** : Implémentez `mark_as_read(row)` avec signal `dataChanged`.
- **Piste** : `self.dataChanged.emit(index, index)` pour notifier.
- **Validation** : Possibilité de marquer un livre comme lu avec mise à jour visuelle.

---

## Exercices supplémentaires

- **ToolTipRole** : Ajoutez des info-bulles avec détails du livre.
- **BackgroundRole** : Colorez le fond selon la priorité des livres.
- **Bouton toggle** : Permettez de basculer entre lu/non lu.