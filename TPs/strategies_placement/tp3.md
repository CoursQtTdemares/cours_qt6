# TP3 - Layouts imbriqués complexes

**Durée** : 30 minutes

**Objectif** : Créer une interface style IDE avec panneaux multiples et zones redimensionnables, en utilisant des layouts imbriqués.

**Pré-requis** : TP1 et TP2 terminés, compréhension des layouts de base.

## 1) Structure du projet IDE

- **Action** : Créez un projet `tp_ide_layout` avec une fenêtre principale `IDEWindow`.
- **Piste** : Utilisez `QMainWindow` pour bénéficier des zones prédéfinies.
- **Validation** : Fenêtre principale avec barre de menu et statut basiques.

## 2) Layout principal à trois zones

- **Action** : Créez un layout horizontal principal avec : sidebar gauche, zone centrale, panneau droit.
- **Indice** : Utilisez des proportions 1:3:1 avec `addWidget(widget, stretch_factor)`.
- **Validation** : Trois zones verticales distinctes visibles (utilisez des couleurs temporaires).

## 3) Sidebar de navigation (gauche)

- **Action** : Dans la zone gauche, créez un layout vertical avec titre "Explorateur" et liste des fichiers.
- **Piste** : `QListWidget` pour la liste, recherchez comment ajouter des éléments.
- **Validation** : Liste de fichiers factices affichée dans le panneau gauche.

## 4) Zone centrale divisée

- **Action** : Divisez la zone centrale horizontalement : éditeur en haut (75%), console en bas (25%).
- **Indice** : Layout vertical avec deux `QTextEdit`, l'un pour l'éditeur, l'autre pour la console.
- **Validation** : Zone d'édition principale et console distinctes et proportionnées.

## 5) Panneau de propriétés (droite)

- **Action** : Dans la zone droite, créez un layout vertical avec sections "Propriétés" et "Outline".
- **Piste** : Utilisez `QLabel` pour les titres de sections et `QTextEdit` ou `QListWidget` pour le contenu.
- **Validation** : Deux sections empilées verticalement dans le panneau droit.

## 6) Barre d'outils intégrée

- **Action** : Ajoutez une barre d'outils avec boutons : Nouveau, Ouvrir, Sauver, Exécuter.
- **Indice** : Utilisez la `QToolBar` de `QMainWindow` ou un layout horizontal avec `QPushButton`.
- **Validation** : Rangée de boutons accessibles en haut de l'interface.

## 7) Barre de statut informative

- **Action** : Configurez la barre de statut pour afficher : position curseur, mode, nombre de lignes.
- **Piste** : Recherchez `statusBar()` et comment ajouter des widgets permanents.
- **Validation** : Informations factices affichées dans la barre de statut.

## 8) Responsive adaptatif

- **Action** : Implémentez un mécanisme pour masquer les panneaux latéraux quand la fenêtre est trop petite.
- **Indice** : Surchargez `resizeEvent()` et utilisez `setVisible()` selon la largeur.
- **Validation** : Les panneaux latéraux disparaissent quand la fenêtre devient trop étroite.

---

## Exercices supplémentaires

- **Splitters** : Remplacez les layouts fixes par des `QSplitter` pour permettre le redimensionnement manuel.
- **Onglets éditeur** : Transformez la zone d'édition en `QTabWidget` pour supporter plusieurs fichiers ouverts.
- **Menu contextuel** : Ajoutez des menus contextuels sur la liste de fichiers (piste: `customContextMenuRequested`).
- **Dock widgets** : Remplacez les panneaux par des `QDockWidget` pour permettre leur détachement.
