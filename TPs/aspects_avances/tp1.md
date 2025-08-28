# TP1 - Application MDI complète

**Durée** : 30 minutes

**Objectif** : Créer une application MDI avec différents types de documents et implémenter la gestion des fenêtres et des menus.

**Pré-requis** : Tous les chapitres précédents maîtrisés.

## 1) Structure MDI de base

- **Action** : Créez un projet `tp_mdi_complete` avec `QMainWindow` et `QMdiArea` comme widget central.
- **Piste** : Configurez le `QMdiArea` en mode onglets avec `setViewMode(QMdiArea.ViewMode.TabbedView)`.
- **Validation** : Fenêtre principale avec zone MDI en onglets.

## 2) Types de documents multiples

- **Action** : Créez 3 types de documents : Éditeur de texte, Calculatrice, Visionneuse d'image.
- **Indice** : Chaque type hérite d'une classe `MDIDocument` de base avec interface commune.
- **Validation** : Trois types de documents distincts créables depuis des menus.

## 3) Menu et actions de documents

- **Action** : Implémentez un menu "Fichier" avec "Nouveau" et sous-menu des types de documents.
- **Piste** : Actions séparées pour chaque type : "Nouveau Texte", "Nouvelle Calculatrice", etc.
- **Validation** : Menu permettant la création de tous les types de documents.

## 4) Gestion des fenêtres MDI

- **Action** : Ajoutez un menu "Fenêtres" avec Cascade, Mosaïque, Fermer tout, Fermer actif.
- **Indice** : Utilisez les méthodes built-in de `QMdiArea` : `cascadeSubWindows()`, `tileSubWindows()`.
- **Validation** : Gestion complète de l'organisation des sous-fenêtres.

## 5) Liste des fenêtres ouvertes

- **Action** : Ajoutez au menu "Fenêtres" une liste dynamique des documents ouverts.
- **Piste** : Connectez `subWindowActivated` pour maintenir la liste à jour.
- **Validation** : Menu dynamique permettant de basculer entre les documents.

## 6) Barre d'état contextuelle

- **Action** : La barre d'état doit afficher des informations selon la fenêtre active.
- **Indice** : Chaque type de document met à jour la barre d'état différemment.
- **Validation** : Barre d'état changeant selon le document actif.

## 7) Sauvegarde d'état MDI

- **Action** : Sauvegardez et restaurez l'état des fenêtres (position, taille, documents ouverts).
- **Piste** : Utilisez `QSettings` et gérez `closeEvent` de la fenêtre principale.
- **Validation** : Application qui retrouve son état MDI au redémarrage.

## 8) Gestion des modifications

- **Action** : Implémentez un système de détection des modifications avec confirmation avant fermeture.
- **Indice** : Signal `modificationChanged` et gestion dans `closeEvent` des sous-fenêtres.
- **Validation** : Demande de confirmation si des documents sont modifiés.

---

## Exercices supplémentaires

- **Onglets détachables** : Permettez de détacher les onglets en fenêtres indépendantes.
- **Sessions** : Sauvegardez/chargez des sessions complètes de travail.
- **Recherche globale** : Fonction de recherche dans tous les documents texte ouverts.
- **Plugin architecture** : Préparez l'architecture pour ajouter facilement de nouveaux types de documents.