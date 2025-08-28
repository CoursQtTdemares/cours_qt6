# TP3 - Gestionnaire de fichiers avancé

**Durée** : 30 minutes

**Objectif** : Créer un explorateur de fichiers avec threads et intégrer la gestion des styles et thèmes.

**Pré-requis** : TP1 et TP2 terminés, notions de threading Qt.

## 1) Interface d'explorateur

- **Action** : Créez un projet `tp_file_explorer` avec interface à deux panneaux : arbre + liste.
- **Piste** : `QSplitter` horizontal avec `QTreeView` (dossiers) et `QListView` (fichiers).
- **Validation** : Interface d'explorateur classique avec navigation fonctionnelle.

## 2) Modèle de système de fichiers

- **Action** : Utilisez `QFileSystemModel` pour afficher l'arborescence et les fichiers.
- **Indice** : Configurez les filtres, colonnes visibles, et tri par défaut.
- **Validation** : Navigation dans le système de fichiers avec métadonnées (taille, date).

## 3) Prévisualisation de fichiers

- **Action** : Ajoutez un panneau de prévisualisation pour images et texte.
- **Piste** : `QLabel` pour images, `QTextEdit` en lecture seule pour texte.
- **Validation** : Prévisualisation automatique lors de la sélection de fichiers.

## 4) Opérations sur fichiers en arrière-plan

- **Action** : Implémentez copie, déplacement, suppression de fichiers avec `QThread`.
- **Indice** : Classe `FileOperationWorker` héritant de `QThread` avec signaux de progression.
- **Validation** : Opérations de fichiers non bloquantes avec barre de progression.

## 5) Recherche de fichiers threadée

- **Action** : Ajoutez une fonction de recherche de fichiers par nom/contenu en arrière-plan.
- **Piste** : Thread de recherche avec `QDirIterator` et signaux pour les résultats.
- **Validation** : Recherche rapide et responsive avec résultats en temps réel.

## 6) Système de thèmes complet

- **Action** : Implémentez un système de thèmes (clair, sombre, coloré) pour l'explorateur.
- **Indice** : Classes CSS pour chaque thème, menu de sélection dynamique.
- **Validation** : Changement de thème instantané affectant toute l'interface.

## 7) Gestion des favoris et historique

- **Action** : Ajoutez des favoris de dossiers et un historique de navigation.
- **Piste** : Stockage avec `QSettings`, boutons de navigation précédent/suivant.
- **Validation** : Navigation rapide vers dossiers favoris et historique fonctionnel.

## 8) Plugins et extensions

- **Action** : Préparez une architecture de plugins pour ajouter des prévisualisateurs.
- **Indice** : Interface de plugin pour différents types de fichiers, chargement dynamique.
- **Validation** : Architecture extensible permettant d'ajouter facilement de nouveaux types.

---

## Exercices supplémentaires

- **Synchronisation réseau** : Ajoutez la navigation sur serveurs FTP/SFTP.
- **Compression intégrée** : Support de création/extraction d'archives ZIP.
- **Comparaison de dossiers** : Outil de comparaison et synchronisation entre dossiers.
- **Indexation** : Système d'indexation pour recherche ultra-rapide dans le contenu.
