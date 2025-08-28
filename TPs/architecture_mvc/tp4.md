# TP4 - Synchronisation multi-vues

**Durée** : 30 minutes

**Objectif** : Créer une application avec plusieurs vues synchronisées du même modèle et implémenter un système de notifications de changements.

**Pré-requis** : TP1 à TP3 terminés, maîtrise des modèles/vues/délégués.

## 1) Application multi-vues

- **Action** : Créez un projet `tp_sync_views` avec une fenêtre contenant 3 vues du même modèle de données.
- **Piste** : `QTableView`, `QListView`, et `QTreeView` côte à côte partageant le même modèle.
- **Validation** : Trois vues distinctes affichant les mêmes données.

## 2) Modèle de données unifié

- **Action** : Créez un modèle de contacts avec nom, email, téléphone, groupe, photo.
- **Indice** : Le modèle doit être compatible avec les 3 types de vues (table, liste, arbre).
- **Validation** : Modèle fonctionnel dans les trois vues simultanément.

## 3) Synchronisation de sélection

- **Action** : Implémentez la synchronisation des sélections entre les trois vues.
- **Piste** : Connectez les signaux `selectionChanged` des `QSelectionModel` de chaque vue.
- **Validation** : Sélectionner dans une vue met à jour les autres vues.

## 4) Observateur de changements

- **Action** : Créez une classe `ModelObserver` qui surveille et log tous les changements du modèle.
- **Indice** : Connectez aux signaux `dataChanged`, `rowsInserted`, `rowsRemoved` du modèle.
- **Validation** : Log détaillé de toutes les modifications dans une zone de texte.

## 5) Panneau de statistiques

- **Action** : Ajoutez un panneau affichant des statistiques en temps réel (nombre total, par groupe, etc.).
- **Piste** : Mettez à jour les statistiques à chaque modification du modèle.
- **Validation** : Statistiques actualisées automatiquement lors des changements.

## 6) Vue filtrée indépendante

- **Action** : Ajoutez une 4e vue avec un `QSortFilterProxyModel` filtrant par groupe.
- **Indice** : Cette vue montre seulement un sous-ensemble mais reste synchronisée.
- **Validation** : Vue filtrée mise à jour quand le modèle source change.

## 7) Notifications système

- **Action** : Implémentez un système de notifications pour les actions importantes (ajout, suppression).
- **Piste** : Utilisez `QMessageBox` ou `QSystemTrayIcon` pour notifier les changements.
- **Validation** : Notifications visuelles des modifications importantes.

## 8) Historique des modifications

- **Action** : Maintenez un historique des modifications avec possibilité d'annuler (Undo).
- **Indice** : Stockez les états précédents et permettez la restauration.
- **Validation** : Fonction Undo opérationnelle sur les dernières modifications.

---

## Exercices supplémentaires

- **Synchronisation réseau** : Simulez la synchronisation avec un serveur distant (timer + changements aléatoires).
- **Conflit de modifications** : Gérez les conflits quand plusieurs utilisateurs modifient les mêmes données.
- **Vue temps réel** : Ajoutez une vue graphique (graphique en barres) mise à jour en temps réel.
- **Sauvegarde automatique** : Sauvegardez automatiquement à chaque modification avec horodatage.
