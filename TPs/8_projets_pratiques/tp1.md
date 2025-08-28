# TP1 - Application complète de gestion de contacts

**Durée** : 60 minutes

**Objectif** : Développer une application de carnet d'adresses avec toutes les fonctionnalités, en implémentant la persistance, validation et interface complète.

**Pré-requis** : Tous les chapitres précédents maîtrisés.

## 1) Architecture et structure du projet

- **Action** : Créez un projet `carnet_adresses` avec architecture MVC complète.
- **Piste** : Dossiers `models/`, `views/`, `controllers/`, `data/`, tests et configuration avec `uv`.
- **Validation** : Structure de projet professionnelle avec tous les composants organisés.

## 2) Modèle de données Contact

- **Action** : Implémentez un modèle `Contact` complet avec tous les champs nécessaires.
- **Indice** : Nom, prénom, entreprise, email, téléphone, adresse, notes, photo, dates importantes.
- **Validation** : Classe Contact avec validation, sérialisation JSON et gestion des erreurs.

## 3) Interface principale avec Qt Designer

- **Action** : Créez l'interface principale avec Designer : liste, détails, recherche, boutons d'action.
- **Piste** : Layout à 3 zones : liste des contacts, détails du contact sélectionné, outils de gestion.
- **Validation** : Interface professionnelle générée avec Designer et intégrée.

## 4) Système de persistance avec SQLite

- **Action** : Implémentez la sauvegarde en base SQLite avec migration de schéma.
- **Indice** : Utilisez `sqlite3` ou `SQLAlchemy`, gérez les versions de schéma et migrations.
- **Validation** : Données persistantes avec support de montée de version.

## 5) Fonctionnalités CRUD complètes

- **Action** : Implémentez toutes les opérations : Créer, Lire, Modifier, Supprimer avec validation.
- **Piste** : Formulaires de saisie, confirmation de suppression, validation en temps réel.
- **Validation** : Gestion complète du cycle de vie des contacts avec sécurité.

## 6) Recherche et filtrage avancés

- **Action** : Ajoutez recherche textuelle, filtres par entreprise/ville, tri par colonnes.
- **Indice** : `QSortFilterProxyModel` avec recherche multi-critères et expressions régulières.
- **Validation** : Recherche rapide et flexible dans toute la base de contacts.

## 7) Import/Export de données

- **Action** : Supportez l'import/export depuis CSV, vCard et autres formats standards.
- **Piste** : Parsers pour différents formats, gestion des erreurs d'import, mapping des champs.
- **Validation** : Échange de données avec d'autres applications de contacts.

## 8) Fonctionnalités avancées

- **Action** : Ajoutez photos de contacts, groupes, favoris, historique des modifications.
- **Indice** : Stockage d'images, catégorisation, système de tags, audit trail.
- **Validation** : Application riche avec fonctionnalités de carnet d'adresses moderne.

---

## Livrables attendus

- **Code source** : Projet complet avec architecture professionnelle
- **Base de données** : Schéma SQLite optimisé avec données de test
- **Documentation** : README avec installation et utilisation
- **Tests** : Suite de tests couvrant les fonctionnalités principales