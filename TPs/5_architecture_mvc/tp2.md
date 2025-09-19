# TP2 - Interactions et signaux

**Durée** : 30 minutes

**Objectif** : Ajouter les interactions utilisateur (ajout/suppression) en maîtrisant les signaux de notification.

**Pré-requis** : TP1 terminé et fonctionnel.

## 1) Zone de saisie

- **Action** : Ajoutez un `QLineEdit` et bouton "➕ Ajouter" avant la liste.
- **Piste** : Utilisez un `QHBoxLayout` pour placer côte à côte.
- **Validation** : Zone de saisie visible au-dessus de la liste.

## 2) Méthode d'ajout dans le modèle

- **Action** : Implémentez `add_book(title)` dans `BookModel` avec les signaux.
- **Piste** : `beginInsertRows()` → ajout → `endInsertRows()` (ordre crucial !).
- **Validation** : Méthode d'ajout avec signaux corrects.

## 3) Connexion du bouton d'ajout

- **Action** : Connectez le bouton et la touche Entrée à une méthode qui appelle le modèle.
- **Piste** : `clicked.connect()` et `returnPressed.connect()`.
- **Validation** : Possibilité d'ajouter des livres via bouton ou Entrée.

## 4) Test de synchronisation

- **Action** : Testez l'ajout et vérifiez que la vue se met à jour automatiquement.
- **Piste** : Ajoutez plusieurs livres et observez la mise à jour instantanée.
- **Validation** : Nouveau livre apparaît instantanément sans code supplémentaire.

## 5) Bouton de suppression

- **Action** : Ajoutez un bouton "🗑️ Supprimer sélectionné" avec style rouge.
- **Piste** : Utilisez `setStyleSheet()` avec background-color: #e74c3c.
- **Validation** : Bouton de suppression stylé visible sous la liste.

## 6) Méthode de suppression

- **Action** : Implémentez `remove_book(row)` dans le modèle avec signaux.
- **Piste** : `beginRemoveRows()` → suppression → `endRemoveRows()`.
- **Validation** : Méthode de suppression avec signaux corrects.

## 7) Connexion suppression

- **Action** : Connectez le bouton pour supprimer l'élément sélectionné.
- **Piste** : Utilisez `selectedIndexes()` pour récupérer la sélection.
- **Validation** : Possibilité de supprimer le livre sélectionné.

## 8) Test complet

- **Action** : Testez le cycle ajout/suppression complet.
- **Piste** : Ajoutez 3 livres, sélectionnez-en un, supprimez-le, vérifiez la synchronisation.
- **Validation** : Toutes les interactions fonctionnent avec synchronisation parfaite.

---

## Exercices supplémentaires

- **Validation** : Empêchez l'ajout de livres avec titre vide.
- **Raccourcis** : Ajoutez Suppr au clavier pour supprimer.
- **Confirmation** : Demandez confirmation avant suppression.