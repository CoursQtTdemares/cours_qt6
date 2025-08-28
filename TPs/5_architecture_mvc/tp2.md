# TP2 - Vue hiérarchique de projets

**Durée** : 30 minutes  

**Objectif** : Développer une structure arborescente pour organiser projets/tâches/sous-tâches en utilisant QTreeView avec un modèle personnalisé hiérarchique.

**Pré-requis** : TP1 terminé, compréhension des modèles de base.

## 1) Architecture hiérarchique

- **Action** : Créez un projet `tp_project_tree` avec une classe `ProjectTreeModel` héritant de `QAbstractItemModel`.
- **Piste** : Structure : Projets → Catégories → Tâches → Sous-tâches.
- **Validation** : Modèle hiérarchique de base configuré.

## 2) Classe de nœud Project/Task

- **Action** : Créez une classe `TreeItem` représentant un élément avec parent/enfants.
- **Indice** : Chaque item a : données (nom, type, statut), parent, liste d'enfants, méthodes de navigation.
- **Validation** : Structure de nœud fonctionnelle pour l'arbre.

## 3) Méthodes de navigation

- **Action** : Implémentez `index()`, `parent()`, `rowCount()`, `columnCount()` du modèle.
- **Piste** : `index()` doit créer des index avec `createIndex(row, column, item)`.
- **Validation** : Navigation dans l'arbre fonctionnelle (expand/collapse).

## 4) Affichage des données

- **Action** : Implémentez `data()` pour afficher icônes et texte selon le type d'élément.
- **Indice** : Projets = 🗂️, Catégories = 📁, Tâches = ☐, Tâches terminées = ✅.
- **Validation** : Arbre avec icônes différenciées par type d'élément.

## 5) Modification de structure

- **Action** : Ajoutez des méthodes pour créer/supprimer des projets, catégories et tâches.
- **Piste** : Utilisez `beginInsertRows()` et `endInsertRows()` pour notifier les changements.
- **Validation** : Possibilité de modifier la structure de l'arbre dynamiquement.

## 6) Interface de gestion

- **Action** : Créez une interface avec `QTreeView` et boutons contextuels selon la sélection.
- **Indice** : Menu contextuel différent pour chaque niveau (projet/catégorie/tâche).
- **Validation** : Interface adaptée au type d'élément sélectionné.

## 7) Gestion des états

- **Action** : Implémentez le changement d'état des tâches (à faire → en cours → terminé) avec propagation.
- **Piste** : Marquer un projet comme terminé si toutes ses tâches le sont.
- **Validation** : États cohérents dans toute la hiérarchie.

## 8) Statistiques visuelles

- **Action** : Affichez des statistiques par projet (nombre de tâches, pourcentage d'avancement).
- **Indice** : Calculez et affichez dans une colonne dédiée ou un tooltip.
- **Validation** : Informations de progression visibles pour chaque projet.

---

## Exercices supplémentaires

- **Glisser-déposer** : Permettez de réorganiser les éléments par drag&drop dans l'arbre.
- **Recherche dans l'arbre** : Ajoutez une fonction de recherche qui développe et surligne les résultats.
- **Export hiérarchique** : Exportez la structure complète en format XML ou JSON indenté.
- **Vue Gantt simple** : Ajoutez une vue parallèle montrant les projets sous forme de diagramme de Gantt.
