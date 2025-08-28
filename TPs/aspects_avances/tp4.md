# TP4 - Application multilingue

**Durée** : 30 minutes

**Objectif** : Internationaliser une application existante, créer les fichiers de traduction et les menus de langues.

**Pré-requis** : TP1 à TP3 terminés, notions d'internationalisation.

## 1) Préparation de l'application

- **Action** : Prenez une application existante (TP précédent) et préparez-la pour l'internationalisation.
- **Piste** : Remplacez tous les strings par des appels `self.tr()` ou `QCoreApplication.translate()`.
- **Validation** : Application avec strings externalisables identifiés et marqués.

## 2) Configuration Qt Linguist

- **Action** : Installez Qt Linguist et configurez le projet pour générer les fichiers .ts.
- **Indice** : Créez un fichier .pro ou utilisez `pylupdate6` pour extraire les strings.
- **Validation** : Fichiers .ts générés avec tous les strings à traduire.

## 3) Traductions en français et anglais

- **Action** : Traduisez l'application en français et anglais avec Qt Linguist.
- **Piste** : Ouvrez les fichiers .ts dans Linguist et complétez toutes les traductions.
- **Validation** : Fichiers .ts complètement traduits et compilés en .qm.

## 4) Gestionnaire de traductions

- **Action** : Créez une classe `TranslationManager` pour gérer le chargement des traductions.
- **Indice** : `QTranslator` avec méthodes pour charger/décharger les langues dynamiquement.
- **Validation** : Changement de langue en temps réel dans l'application.

## 5) Menu de sélection de langue

- **Action** : Ajoutez un menu "Langue" avec drapeaux et sélection de la langue active.
- **Piste** : Actions checkables avec icônes de drapeaux, une seule sélectionnée à la fois.
- **Validation** : Menu permettant de changer la langue avec feedback visuel.

## 6) Persistance de la langue

- **Action** : Sauvegardez le choix de langue et restaurez-le au redémarrage.
- **Indice** : `QSettings` pour stocker la langue sélectionnée.
- **Validation** : Application qui se lance dans la dernière langue sélectionnée.

## 7) Adaptation culturelle

- **Action** : Adaptez les formats de date, nombre et devise selon la langue.
- **Piste** : `QLocale` pour les formats régionaux, adaptation automatique.
- **Validation** : Affichage des données selon les conventions locales.

## 8) Langue système par défaut

- **Action** : Détectez automatiquement la langue du système au premier lancement.
- **Indice** : `QLocale.system().name()` pour détecter la langue, fallback vers anglais.
- **Validation** : Application qui se lance dans la langue du système si disponible.

---

## Exercices supplémentaires

- **Traduction contextuelle** : Implémentez des traductions différentes selon le contexte d'usage.
- **Pluriels complexes** : Gérez les règles de pluriel spécifiques à chaque langue.
- **Support RTL** : Ajoutez le support des langues droite-à-gauche (arabe, hébreu).
- **Traduction collaborative** : Système permettant aux utilisateurs de contribuer aux traductions.
