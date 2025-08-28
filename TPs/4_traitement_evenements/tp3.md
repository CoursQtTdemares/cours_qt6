# TP3 - Interface glisser-déposer

**Durée** : 30 minutes

**Objectif** : Implémenter une interface de gestion de fichiers avec glisser-déposer, en gérant différents types de données et validations.

**Pré-requis** : TP1 et TP2 terminés, notions d'événements souris avancés.

## 1) Interface de gestionnaire de fichiers

- **Action** : Créez un projet `tp_drag_drop` avec deux zones principales : "Source" et "Destination".
- **Piste** : Utilisez un layout horizontal avec deux `QFrame` de couleurs différentes.
- **Validation** : Deux zones distinctes visuellement séparées.

## 2) Zone source avec éléments draggables

- **Action** : Dans la zone source, créez des éléments représentant des fichiers (icône + nom).
- **Indice** : Utilisez `QLabel` avec `setAcceptDrops(False)` mais activez le drag. Recherchez `QDrag` et `QMimeData`.
- **Validation** : Éléments visuels représentant des fichiers dans la zone source.

## 3) Activation du glisser-déposer

- **Action** : Implémentez `mousePressEvent()` et `mouseMoveEvent()` pour démarrer un drag.
- **Piste** : Vérifiez la distance avec `QApplication.startDragDistance()` avant de commencer le drag.
- **Validation** : Le glisser se déclenche après un mouvement suffisant.

## 4) Données de transfert

- **Action** : Configurez les `QMimeData` avec le nom du fichier et son type.
- **Indice** : Utilisez `setText()` pour le nom et `setData()` pour un type MIME personnalisé.
- **Validation** : Les données du fichier sont attachées au drag.

## 5) Zone de destination

- **Action** : Implémentez `dragEnterEvent()`, `dragMoveEvent()` et `dropEvent()` dans la zone destination.
- **Piste** : Acceptez le drop avec `event.acceptProposedAction()` si les données sont valides.
- **Validation** : La zone destination réagit visuellement au survol et accepte le drop.

## 6) Validation des types

- **Action** : N'acceptez que certains types de fichiers (ex: images, documents texte).
- **Indice** : Vérifiez l'extension du fichier dans `dragEnterEvent()` avant d'accepter.
- **Validation** : Seuls les fichiers autorisés peuvent être déposés.

## 7) Feedback visuel

- **Action** : Changez l'apparence de la zone de destination pendant le survol (couleur, bordure).
- **Piste** : Modifiez le style dans `dragEnterEvent()` et restaurez-le dans `dragLeaveEvent()`.
- **Validation** : Feedback visuel clair pendant les opérations de glisser-déposer.

## 8) Affichage des fichiers déposés

- **Action** : Affichez la liste des fichiers déposés avec leur icône et métadonnées.
- **Indice** : Utilisez `QListWidget` avec `QListWidgetItem` personnalisés.
- **Validation** : Les fichiers déposés apparaissent dans une liste organisée.

---

## Exercices supplémentaires

- **Drag externe** : Acceptez les fichiers glissés depuis l'explorateur système (piste: `QUrl` et `hasUrls()`).
- **Prévisualisation** : Affichez un aperçu du fichier lors du survol (miniature pour images, premières lignes pour texte).
- **Actions multiples** : Supportez copier/déplacer/lier selon les touches modificatrices (Ctrl, Shift).
- **Corbeille** : Ajoutez une zone "corbeille" pour supprimer des éléments par glisser-déposer.
