# TP2 - Personnalisation avec CSS

**Durée** : 30 minutes

**Objectif** : Appliquer des styles CSS personnalisés à une application PyQt6 et implémenter un système de thèmes dynamiques (clair/sombre).

**Pré-requis** : TP1 terminé avec une application QMainWindow fonctionnelle.

## 1) Fichier CSS externe

- **Action** : Créez un fichier `styles.css` dans votre projet et chargez-le dans votre application.
- **Indice** : 
  - Placez le fichier dans un dossier `resources/`
  - Lisez le contenu du fichier et appliquez-le avec `setStyleSheet()`
  - Gérez les erreurs si le fichier n'existe pas
- **Validation** : Les styles sont appliqués au démarrage de l'application

## 2) Styles de base pour QMainWindow

- **Action** : Stylisez la fenêtre principale avec une couleur de fond et des bordures.
- **Piste** : 
  - Utilisez le sélecteur `QMainWindow` en CSS
  - Définissez `background-color`, `border`, et éventuellement une image de fond
  - Testez différentes couleurs pour voir l'effet
- **Validation** : La fenêtre principale a un aspect visuel personnalisé

## 3) Personnalisation de la barre de menus

- **Action** : Créez un style moderne pour la barre de menus avec des couleurs contrastées.
- **Indice** : 
  - Stylisez `QMenuBar` pour la barre elle-même
  - Utilisez `QMenuBar::item` pour les éléments du menu
  - Ajoutez des états `:hover` et `:selected` pour l'interactivité
- **Validation** : La barre de menus a un aspect professionnel avec des effets de survol

## 4) Style de la barre d'outils

- **Action** : Harmonisez l'apparence de la barre d'outils avec la barre de menus.
- **Piste** : 
  - Stylisez `QToolBar` pour le conteneur
  - Utilisez `QToolButton` pour les boutons individuels
  - Ajoutez des effets `:hover` et `:pressed` pour le feedback visuel
- **Validation** : La barre d'outils s'intègre visuellement avec le reste de l'interface

## 5) Système de thèmes

- **Action** : Implémentez un commutateur de thèmes dans le menu "Affichage".
- **Indice** : 
  - Créez une méthode `apply_theme(theme_name)` qui charge différents CSS
  - Ajoutez des actions "Thème clair" et "Thème sombre" dans le menu
  - Stockez les styles dans des variables ou des fichiers séparés
- **Validation** : Le changement de thème modifie instantanément l'apparence de toute l'application

## 6) Thème sombre complet

- **Action** : Créez un thème sombre cohérent pour tous les composants de l'interface.
- **Piste** : 
  - Utilisez des couleurs sombres (#2c3e50, #34495e) pour les arrière-plans
  - Contrastez avec du texte clair (#ecf0f1, white)
  - Attention aux bordures et aux états de survol pour maintenir la lisibilité
- **Validation** : Le thème sombre est utilisable et agréable visuellement

## 7) Styles pour la barre de statut

- **Action** : Personnalisez la barre de statut pour qu'elle s'harmonise avec vos thèmes.
- **Indice** : 
  - Stylisez `QStatusBar` pour la couleur de fond
  - Ajoutez une bordure supérieure pour séparer du contenu principal
  - Assurez-vous que le texte reste lisible dans les deux thèmes
- **Validation** : La barre de statut s'intègre parfaitement dans chaque thème

---

## Exercices supplémentaires

- **Animations CSS** : Ajoutez des transitions fluides lors du changement de thème (piste: `transition` en CSS).
- **Thème personnalisé** : Créez un troisième thème avec vos couleurs préférées (bleu, vert, violet...).
- **Styles conditionnels** : Ajoutez des styles différents selon l'état des actions (activé/désactivé).
- **Préférences utilisateur** : Sauvegardez le thème choisi et restaurez-le au démarrage (piste: `QSettings`).
- **CSS avancé** : Expérimentez avec les dégradés (`linear-gradient`) et les ombres (`box-shadow`).
- **Hot-reload** : Implémentez un rechargement automatique du CSS quand le fichier est modifié (piste: `QFileSystemWatcher`).
