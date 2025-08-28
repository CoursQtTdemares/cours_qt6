# TP1 - Modèle de gestion de tâches

**Durée** : 30 minutes

**Objectif** : Créer un modèle personnalisé pour une application de gestion de tâches, en implémentant l'ajout, suppression et modification de tâches avec priorités.

**Pré-requis** : Chapitres 1-4 maîtrisés, notions de base sur l'architecture MVC.

## 1) Structure du projet MVC

- **Action** : Créez un projet `tp_task_manager` avec une architecture claire : dossiers `models/`, `views/`, `controllers/`.
- **Validation** : Structure de projet organisée et PyQt6 installé.

## 2) Modèle de données Task

- **Action** : Créez une classe `TaskModel` héritant de `QAbstractTableModel` pour gérer des tâches.
- **Piste** : Une tâche contient : titre, description, priorité (1-5), statut (À faire/En cours/Terminé), date d'échéance.
- **Validation** : Classe de base du modèle avec structure de données définie.

## 3) Méthodes obligatoires du modèle

- **Action** : Implémentez `rowCount()`, `columnCount()`, `data()` et `headerData()`.
- **Indice** : `data()` doit gérer différents rôles : `DisplayRole`, `EditRole`, `BackgroundRole` pour les priorités.
- **Validation** : Le modèle peut être affiché dans une vue basique.

## 4) Gestion des priorités visuelles

- **Action** : Colorez les lignes selon la priorité (rouge = urgent, orange = haute, vert = basse).
- **Piste** : Utilisez `Qt.ItemDataRole.BackgroundRole` dans `data()` avec `QColor`.
- **Validation** : Les tâches s'affichent avec des couleurs de priorité.

## 5) Édition des données

- **Action** : Implémentez `flags()` et `setData()` pour permettre l'édition directe dans la vue.
- **Indice** : Validez les données (priorité entre 1-5, statut dans la liste autorisée).
- **Validation** : Double-clic permet d'éditer les cellules avec validation.

## 6) Ajout et suppression de tâches

- **Action** : Implémentez `insertRows()` et `removeRows()` pour gérer la structure dynamique.
- **Piste** : N'oubliez pas `beginInsertRows()` et `endInsertRows()` pour notifier les vues.
- **Validation** : Possibilité d'ajouter/supprimer des tâches programmatiquement.

## 7) Interface de gestion

- **Action** : Créez une vue avec `QTableView` et boutons pour ajouter, supprimer, marquer comme terminé.
- **Indice** : Connectez les boutons à des méthodes qui modifient le modèle.
- **Validation** : Interface fonctionnelle pour gérer les tâches.

## 8) Filtrage par statut

- **Action** : Ajoutez un `QComboBox` pour filtrer les tâches par statut (Toutes, À faire, En cours, Terminées).
- **Piste** : Utilisez `QSortFilterProxyModel` avec `setFilterKeyColumn()` et `setFilterFixedString()`.
- **Validation** : Le filtrage fonctionne et met à jour la vue en temps réel.

---

## Exercices supplémentaires

- **Tri avancé** : Activez le tri par colonnes avec des règles personnalisées (priorité > date > titre).
- **Données persistantes** : Sauvegardez/chargez les tâches dans un fichier JSON.
- **Validation métier** : Empêchez la création de tâches avec date d'échéance dans le passé.
- **Sous-tâches** : Transformez en modèle hiérarchique supportant des sous-tâches.
