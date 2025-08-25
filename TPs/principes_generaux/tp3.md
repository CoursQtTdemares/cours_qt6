# TP3 - Menus contextuels avancés

**Durée** : 20 minutes

**Objectif** : Créer des menus contextuels intelligents qui s'adaptent au contexte d'utilisation et gérer différents types d'interactions utilisateur.

**Pré-requis** : TP1 et TP2 terminés avec une interface stylisée.

## 1) Activation des menus contextuels

- **Action** : Activez les menus contextuels sur votre fenêtre principale et le widget central.
- **Indice** : 
  - Utilisez `setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)`
  - Connectez le signal `customContextMenuRequested` à un gestionnaire
  - Testez le clic droit pour déclencher le signal
- **Validation** : Le clic droit déclenche votre gestionnaire (même avec un simple `print()` pour commencer)

## 2) Menu contextuel de base

- **Action** : Créez un menu contextuel simple avec les actions courantes (Couper, Copier, Coller).
- **Piste** : 
  - Utilisez `QMenu` et `addAction()` pour construire le menu
  - Affichez le menu avec `exec()` à la position du clic
  - Implémentez des gestionnaires basiques qui affichent des messages
- **Validation** : Le clic droit affiche un menu avec des actions fonctionnelles

## 3) Logique conditionnelle

- **Action** : Rendez les actions du menu contextuel intelligentes selon le contexte.
- **Indice** : 
  - Désactivez "Couper" et "Copier" s'il n'y a pas de sélection
  - Désactivez "Coller" si le presse-papier est vide
  - Utilisez `setEnabled(False)` sur les actions concernées
- **Validation** : Les actions indisponibles sont grisées dans le menu

## 4) Sous-menus contextuels

- **Action** : Ajoutez un sous-menu "Format" avec des options de mise en forme.
- **Piste** : 
  - Utilisez `addMenu()` pour créer un sous-menu
  - Ajoutez des actions comme "Gras", "Italique", "Couleur du texte"
  - Gérez l'état checkable pour certaines options (gras, italique)
- **Validation** : Le sous-menu s'ouvre au survol et les options sont interactives

## 5) Menus contextuels différenciés

- **Action** : Créez des menus contextuels différents selon la zone cliquée.
- **Indice** : 
  - Identifiez le widget enfant sous la souris avec `childAt()`
  - Affichez un menu différent pour la barre d'outils vs le widget central
  - Par exemple : menu "Personnaliser la barre d'outils" vs menu "Édition de texte"
- **Validation** : Le contenu du menu change selon la zone cliquée

## 6) Séparateurs et organisation

- **Action** : Organisez vos menus contextuels avec des séparateurs logiques.
- **Piste** : 
  - Groupez les actions par catégorie (Édition / Format / Affichage)
  - Utilisez `addSeparator()` entre les groupes
  - Ordonnez les actions par fréquence d'usage (les plus courantes en haut)
- **Validation** : Les menus sont bien structurés et faciles à naviguer

## 7) Raccourcis dans les menus contextuels

- **Action** : Affichez les raccourcis clavier dans les menus contextuels.
- **Indice** : 
  - Réutilisez les mêmes `QAction` que dans vos menus principaux
  - Les raccourcis s'affichent automatiquement s'ils sont définis sur l'action
  - Assurez-vous que les raccourcis fonctionnent même depuis le menu contextuel
- **Validation** : Les raccourcis sont visibles et cohérents avec les menus principaux

---

## Exercices supplémentaires

- **Menu contextuel dynamique** : Ajoutez/supprimez des actions selon l'état de l'application (document ouvert, sélection active, etc.).
- **Icônes dans les menus** : Ajoutez des icônes aux actions du menu contextuel pour une meilleure identification visuelle.
- **Position intelligente** : Ajustez la position du menu si il sort de l'écran (piste: `QApplication.desktop().screenGeometry()`).
- **Menu contextuel sur différents widgets** : Étendez les menus contextuels aux barres d'outils avec des options de personnalisation.
- **Actions récentes** : Ajoutez une section "Actions récentes" dans le menu contextuel.
- **Menu contextuel stylisé** : Appliquez des styles CSS spécifiques aux menus contextuels pour les harmoniser avec vos thèmes.
