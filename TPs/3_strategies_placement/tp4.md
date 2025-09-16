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

---

## Exercices supplémentaires

- **Mode mobile** : Masquez la sidebar et empilez tout verticalement quand largeur < 500px (piste: `setVisible(False)`).
- **Menu hamburger fonctionnel** : Implémentez l'ouverture/fermeture du menu hamburger au clic (piste: `QFrame` overlay).
- **Adaptations DPI** : Ajustez les tailles de police selon la résolution d'écran (piste: `logicalDotsPerInch()`).
- **Transitions fluides** : Ajoutez des animations lors des changements de layout (piste: `QPropertyAnimation`).
- **Breakpoints personnalisés** : Permettez à l'utilisateur de définir ses propres seuils de responsive.
- **Orientation** : Gérez les changements d'orientation mobile (portrait/paysage).
- **Grid responsive** : Créez une grille d'articles qui s'adapte au nombre de colonnes selon la largeur.
