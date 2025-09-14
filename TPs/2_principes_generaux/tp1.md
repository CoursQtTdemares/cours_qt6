# TP1 - Application avec interface complète

**Durée** : 45 minutes

**Objectif** : Créer une application PyQt6 structurée avec `QMainWindow`, incluant des barres de menus, d'outils et de statut, et implémenter les actions de base (Nouveau, Ouvrir, Sauvegarder).

**Pré-requis** : Chapitre 1 terminé et environnement PyQt6 fonctionnel.

## 1) Créer la structure du projet

- **Action** : Créez un nouveau dossier `tp_interface_complete` et initialisez un projet `uv` avec PyQt6.
- **Indice** : 
  - Utilisez `uv init` puis `uv add PyQt6`
  - Créez un fichier `main.py` ("hello world") et un dossier `src` avec un fichier `src/main_window.py`
- **Validation** : Le projet se lance sans erreur avec `uv run main.py`

## 2) Classe MainWindow héritant de QMainWindow

- **Action** : Dans `main_window.py`, créez une classe `MainWindow` qui hérite de `QMainWindow`.
- **Piste** : 
  - Définissez un titre de fenêtre et une taille initiale (800x600)
  - Ajoutez un widget central simple (QLabel avec un message d'accueil)
- **Validation** : La fenêtre s'affiche avec le titre et les dimensions spécifiées

## 3) Barre de menus avec menu "Fichier"

- **Action** : Ajoutez une barre de menus avec un menu "Fichier" contenant les actions Nouveau, Ouvrir, Sauvegarder et Quitter.
- **Indice** : 
  - Utilisez `self.menuBar().addMenu()` pour créer le menu
  - Créez des `QAction` avec raccourcis clavier (Ctrl+N, Ctrl+O, Ctrl+S, Ctrl+Q)
  - Connectez chaque action à une méthode (même si elle ne fait qu'afficher un message pour l'instant)
- **Validation** : Les menus sont visibles, les raccourcis clavier fonctionnent

## 4) Barre d'outils synchronisée

- **Action** : Créez une barre d'outils avec les mêmes actions que le menu Fichier.
- **Piste** : 
  - Réutilisez les mêmes objets `QAction` pour le menu et la barre d'outils
  - Ajoutez des icônes si possible, sinon utilisez du texte
  - Séparez les groupes d'actions avec `addSeparator()`
- **Validation** : Cliquer sur un bouton de la barre d'outils ou sur un élément de menu produit le même résultat

## 5) Barre de statut informative

- **Action** : Configurez une barre de statut qui affiche des messages lors des actions et des informations permanentes.
- **Indice** : 
  - Utilisez `self.statusBar().showMessage()` pour les messages temporaires
  - Ajoutez un widget permanent (QLabel) pour afficher l'état de l'application
  - Modifiez les gestionnaires d'actions pour afficher des messages appropriés
- **Validation** : Les actions affichent des messages dans la barre de statut

## 6) Gestion de l'état des actions

- **Action** : Implémentez une logique pour activer/désactiver les actions selon le contexte.
- **Piste** : 
  - L'action "Sauvegarder" doit être désactivée au démarrage
  - Activez-la après avoir "créé" ou "ouvert" un document
  - Utilisez `setEnabled(True/False)` sur les actions
- **Validation** : L'action Sauvegarder n'est disponible que quand c'est logique

## 7) Messages d'aide contextuelle

- **Action** : Ajoutez des messages d'aide qui s'affichent dans la barre de statut au survol des actions.
- **Indice** : Utilisez `setStatusTip()` sur chaque action avec un texte descriptif
- **Validation** : Survoler un bouton ou un élément de menu affiche l'aide correspondante

---

## Exercices supplémentaires

- **Menu Édition** : Ajoutez un menu "Édition" avec les actions Couper, Copier, Coller (désactivées par défaut).
- **Menu Affichage** : Créez un menu permettant de masquer/afficher la barre d'outils et la barre de statut.
- **Icônes personnalisées** : Téléchargez ou créez des icônes simples et appliquez-les aux actions.
- **Dialogue de confirmation** : Ajoutez une confirmation avant de quitter l'application (piste: `QMessageBox`).
- **Position de fenêtre** : Sauvegardez et restaurez la position/taille de la fenêtre entre les sessions (piste: `QSettings`).
