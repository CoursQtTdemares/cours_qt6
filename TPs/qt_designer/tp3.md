# TP3 - Widgets personnalisés et promotion

**Durée** : 30 minutes

**Objectif** : Développer des widgets personnalisés réutilisables et les intégrer via promotion dans Designer.

**Pré-requis** : TP1 et TP2 terminés, notions de création de widgets.

## 1) Widget de sélection de date avancé

- **Action** : Créez une classe `DateRangeWidget` combinant deux `QDateEdit` pour une plage de dates.
- **Piste** : Layout horizontal avec label "De" - DateEdit - "À" - DateEdit + validation.
- **Validation** : Widget fonctionnel avec validation de la plage de dates.

## 2) Widget d'évaluation par étoiles

- **Action** : Développez un `StarRatingWidget` pour noter de 1 à 5 étoiles.
- **Indice** : Héritez de `QWidget`, gérez `mousePressEvent` et `paintEvent` pour les étoiles.
- **Validation** : Widget cliquable affichant des étoiles pleines/vides.

## 3) Champ de saisie avec validation intégrée

- **Action** : Créez `ValidatedLineEdit` avec indicateur de validité intégré.
- **Piste** : Héritez de `QLineEdit`, ajoutez une icône et changez les couleurs selon validation.
- **Validation** : Champ avec feedback visuel automatique selon le contenu.

## 4) Module de widgets personnalisés

- **Action** : Organisez vos widgets dans un module `custom_widgets.py` bien documenté.
- **Indice** : Documentez chaque widget avec docstrings et exemples d'utilisation.
- **Validation** : Module importable avec widgets bien structurés.

## 5) Promotion dans Designer

- **Action** : Dans Designer, promouvez des `QWidget` vers vos widgets personnalisés.
- **Piste** : Clic droit > "Promote to..." puis configuration classe et module.
- **Validation** : Widgets personnalisés visibles dans l'Object Inspector de Designer.

## 6) Interface utilisant les widgets promus

- **Action** : Créez un nouveau formulaire utilisant tous vos widgets personnalisés.
- **Indice** : Formulaire d'évaluation de produit avec dates, notes et champs validés.
- **Validation** : Interface Designer utilisant exclusivement des widgets personnalisés.

## 7) Compilation et test

- **Action** : Compilez le `.ui` en Python et testez l'intégration complète.
- **Piste** : `pyuic6 evaluation_form.ui -o ui_evaluation.py` puis test d'intégration.
- **Validation** : Interface générée fonctionnelle avec widgets personnalisés opérationnels.

## 8) Signaux personnalisés

- **Action** : Ajoutez des signaux personnalisés à vos widgets et connectez-les.
- **Indice** : `dateRangeChanged`, `ratingChanged`, `validationChanged` émis selon les interactions.
- **Validation** : Communication inter-widgets via signaux personnalisés.

---

## Exercices supplémentaires

- **Widget composé complexe** : Créez un widget d'adresse complète avec géocodage.
- **Thèmes personnalisés** : Ajoutez la gestion de thèmes à vos widgets personnalisés.
- **Propriétés Designer** : Exposez des propriétés configurables dans Designer via `Q_PROPERTY`.
- **Palette de widgets** : Créez une palette personnalisée pour Designer avec vos widgets.
