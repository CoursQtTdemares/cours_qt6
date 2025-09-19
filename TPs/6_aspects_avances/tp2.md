# TP2 - Éditeur graphique avec QPainter

**Durée** : 30 minutes  

**Objectif** : Développer un mini-éditeur de formes géométriques avec transformations et animations.

**Pré-requis** : TP1 terminé, notions de base sur QPainter.

## 1) Canvas de dessin de base

- **Action** : Créez un projet `tp_paint_editor` avec un widget de dessin personnalisé.
- **Piste** : Héritez de `QWidget` et surchargez `paintEvent()` avec `QPainter`.
- **Validation** : Zone de dessin fonctionnelle avec arrière-plan blanc.

## 2) Outils de formes géométriques

- **Action** : Implémentez des outils pour dessiner rectangle, ellipse, ligne, polygone.
- **Indice** : Barre d'outils avec boutons, mode de dessin selon l'outil sélectionné.
- **Validation** : Possibilité de dessiner différentes formes avec la souris.

## 3) Propriétés de dessin

- **Action** : Ajoutez des contrôles pour couleur de trait, épaisseur, couleur de remplissage.
- **Piste** : `QColorDialog` pour les couleurs, `QSpinBox` pour l'épaisseur.
- **Validation** : Formes dessinées avec les propriétés sélectionnées.

## 4) Sélection et manipulation

- **Action** : Permettez de sélectionner et déplacer les formes existantes.
- **Indice** : Détection de clic sur les formes, handles de sélection, glisser-déposer.
- **Validation** : Formes sélectionnables et déplaçables après création.

## 5) Transformations géométriques

- **Action** : Ajoutez rotation et mise à l'échelle des formes sélectionnées.
- **Piste** : Utilisez `QPainter.save()`, `rotate()`, `scale()`, `restore()`.
- **Validation** : Formes transformables avec contrôles visuels.

## 6) Système d'animations

- **Action** : Implémentez l'animation de formes (rotation, translation, pulsation).
- **Indice** : `QTimer` pour l'animation, propriétés animées modifiées périodiquement.
- **Validation** : Formes qui peuvent être animées en boucle.

## 7) Sauvegarde et chargement

- **Action** : Sauvegardez les dessins dans un format personnalisé et rechargez-les.
- **Piste** : Format JSON avec propriétés des formes, ou format image PNG/SVG.
- **Validation** : Dessins persistants entre les sessions.

## 8) Export et rendu haute qualité

- **Action** : Exportez vers différents formats (PNG, SVG, PDF) avec paramètres de qualité.
- **Indice** : `QPainter` sur `QPixmap` pour PNG, `QSvgGenerator` pour SVG.
- **Validation** : Export fonctionnel vers plusieurs formats avec bonne qualité.

---

## Exercices supplémentaires

- **Calques** : Système de calques pour organiser les formes par groupes.
- **Historique** : Annuler/Refaire (Undo/Redo) pour toutes les opérations.
- **Grille magnétique** : Grille d'alignement avec accrochage automatique.
- **Effets visuels** : Ombres portées, dégradés, textures pour les formes.
