# TP3 - Internationalisation *(optionnel)*

**Durée** : 30 minutes

**Objectif** : Ajouter le support multilingue à l'application météo des TP1 et TP2.

**Pré-requis** : TP1 et TP2 terminés et fonctionnels.

## 1) Marquage des textes avec tr()

- **Action** : Remplacez les textes fixes par `self.tr()` dans l'application (bouton, titre, messages).
- **Piste** : `setWindowTitle(self.tr("Application Météo"))`, bouton avec `self.tr("Télécharger")`.
- **Validation** : Tous les textes utilisateur marqués avec `tr()`.

## 2) Extraction et traduction

- **Action** : Utilisez `pylupdate6` pour extraire les chaînes et créez les traductions françaises et anglaises.
- **Piste** : `pylupdate6 *.py -ts translations/app_fr.ts app_en.ts`, éditez les fichiers .ts manuellement.
- **Validation** : Fichiers de traduction créés et remplis.

## 3) Compilation des traductions

- **Action** : Compilez les fichiers .ts en .qm avec `lrelease`.
- **Piste** : `lrelease translations/app_fr.ts translations/app_en.ts` génère les .qm.
- **Validation** : Fichiers .qm compilés disponibles.

## 4) QTranslator dans l'application

- **Action** : Ajoutez `QTranslator` comme attribut et méthode `change_language()`.
- **Piste** : `self.translator = QTranslator()`, méthode qui charge et installe le traducteur.
- **Validation** : Traducteur prêt à charger des langues.

## 5) Menu Langue

- **Action** : Ajoutez un menu "Langue" avec actions "Français" et "English".
- **Piste** : `language_menu = menubar.addMenu(self.tr("Langue"))`, connectez aux méthodes de changement.
- **Validation** : Menu Langue fonctionnel.

## 6) Test du changement dynamique

- **Action** : Testez le changement de langue en temps réel et ajoutez `retranslate_ui()`.
- **Piste** : Méthode qui remet à jour bouton, titre, menu avec `setText(self.tr(...))`.
- **Validation** : Changement de langue instantané dans toute l'interface, textes du graphique inclus.

---

## Exercices supplémentaires

- **Persistance** : Sauvegardez la langue choisie avec `QSettings`.
- **Espagnol** : Ajoutez une troisième langue.
- **Formats** : Utilisez `QLocale` pour formater les températures selon la région (°C vs °F).
