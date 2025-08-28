# TP4 - Interface responsive

**Durée** : 30 minutes

**Objectif** : Développer une interface qui s'adapte automatiquement au redimensionnement et gérer différents modes d'affichage selon la taille.

**Pré-requis** : TP1 à TP3 terminés, compréhension des layouts avancés.

## 1) Application de blog responsive

- **Action** : Créez un projet `tp_blog_responsive` simulant une interface de blog.
- **Validation** : Projet initialisé avec PyQt6 et fenêtre de base.

## 2) Header adaptatif

- **Action** : Créez un header avec logo à gauche, menu navigation au centre, bouton profile à droite.
- **Piste** : Layout horizontal avec `addStretch()` pour espacer les éléments.
- **Validation** : Header avec trois sections bien réparties horizontalement.

## 3) Zone de contenu principale

- **Action** : Créez la zone principale avec sidebar (catégories) à gauche et contenu d'articles à droite.
- **Indice** : Proportions 1:3, sidebar avec `QListWidget`, contenu avec `QTextEdit`.
- **Validation** : Mise en page type blog avec sidebar et zone d'articles.

## 4) Détection du redimensionnement

- **Action** : Surchargez `resizeEvent()` pour détecter les changements de taille de fenêtre.
- **Piste** : Récupérez `event.size().width()` et définissez des seuils (ex: 800px, 500px).
- **Validation** : Messages de debug affichent la largeur lors du redimensionnement.

## 5) Mode tablette (largeur < 800px)

- **Action** : Quand la largeur < 800px, transformez le menu horizontal en menu hamburger.
- **Indice** : Remplacez les boutons du menu par un seul bouton "☰" et masquez les éléments.
- **Validation** : Le menu se transforme en hamburger sur les tailles moyennes.

## 6) Mode mobile (largeur < 500px)

- **Action** : En mode mobile, masquez la sidebar et empilez tout verticalement.
- **Piste** : Utilisez `setVisible(False)` sur la sidebar et réorganisez le layout principal.
- **Validation** : Interface simplifiée en une colonne pour les petites tailles.

## 7) Menu hamburger fonctionnel

- **Action** : Implémentez l'ouverture/fermeture du menu hamburger au clic.
- **Indice** : Créez un `QFrame` overlay qui apparaît/disparaît avec les options du menu.
- **Validation** : Le menu hamburger affiche les options de navigation quand cliqué.

## 8) Adaptations avancées

- **Action** : Ajustez les tailles de police et espacement selon la résolution d'écran.
- **Piste** : Utilisez `QApplication.primaryScreen().logicalDotsPerInch()` pour adapter le DPI.
- **Validation** : L'interface s'adapte visuellement aux différentes résolutions.

---

## Exercices supplémentaires

- **Transitions fluides** : Ajoutez des animations lors des changements de layout (piste: `QPropertyAnimation`).
- **Breakpoints personnalisés** : Permettez à l'utilisateur de définir ses propres seuils de responsive.
- **Orientation** : Gérez les changements d'orientation mobile (portrait/paysage).
- **Grid responsive** : Créez une grille d'articles qui s'adapte au nombre de colonnes selon la largeur.
