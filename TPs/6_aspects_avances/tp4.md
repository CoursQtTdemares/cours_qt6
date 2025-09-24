# TP4 - Internationalisation *(optionnel)*

**Durée** : 30 minutes

**Objectif** : Découvrir l'internationalisation pour supporter français et anglais.

**Pré-requis** : TP1, TP2 et TP3 terminés et fonctionnels.

## 1) Marquage des textes avec tr()

- **Action** : Remplacez les textes fixes par `self.tr()` dans la fenêtre principale et sous-fenêtres.
- **Piste** : `setWindowTitle(self.tr("Application Météo"))`, menus, boutons, etc.
- **Validation** : Tous les textes utilisateur marqués avec `tr()`.

## 2) Extraction et traduction

- **Action** : Utilisez `pylupdate6` pour extraire les chaînes et créez les traductions françaises.
- **Piste** : `pylupdate6 *.py -ts translations/app_fr.ts`, éditez le fichier .ts manuellement.
- **Validation** : Fichier de traduction français créé et rempli.

## 3) Compilation des traductions

- **Action** : Compilez le fichier .ts en .qm avec `lrelease`.
- **Piste** : `lrelease translations/app_fr.ts` génère `app_fr.qm`.
- **Validation** : Fichier .qm compilé disponible.

## 4) QTranslator dans l'application

- **Action** : Ajoutez `QTranslator` comme attribut et méthode `change_language()`.
- **Piste** : `self.translator = QTranslator()`, méthode qui charge et installe le traducteur.
- **Validation** : Traducteur prêt à charger des langues.

## 5) Menu Langue

- **Action** : Ajoutez un menu "Langue" avec actions "Français" et "English".
- **Piste** : Connectez chaque action à `change_language("fr")` ou `change_language("en")`.
- **Validation** : Menu Langue fonctionnel.

## 6) Test du changement dynamique

- **Action** : Testez le changement de langue en temps réel et ajoutez `retranslate_ui()`.
- **Piste** : Méthode qui remet à jour tous les textes avec `setText(self.tr(...))`.
- **Validation** : Changement de langue instantané dans toute l'interface.

---

## Exercices supplémentaires

- **Persistance** : Sauvegardez la langue choisie avec `QSettings`.
- **Espagnol** : Ajoutez une troisième langue.
- **Formats** : Utilisez `QLocale` pour formater les températures selon la région.