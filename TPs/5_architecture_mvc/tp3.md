# TP3 - Délégués d'édition avancés

**Durée** : 30 minutes

**Objectif** : Créer des délégués personnalisés pour différents types de données avec validation et contraintes d'édition.

**Pré-requis** : TP1 et TP2 terminés, notions de délégués de base.

## 1) Projet de gestion d'inventaire

- **Action** : Créez un projet `tp_inventory_delegates` avec un modèle d'articles (nom, prix, quantité, catégorie, date).
- **Validation** : Modèle de données varié prêt pour des délégués spécialisés.

## 2) Délégué de prix avec validation

- **Action** : Créez un `PriceDelegate` pour la colonne prix avec `QDoubleSpinBox` et contraintes.
- **Piste** : Prix minimum 0.01€, maximum 9999.99€, 2 décimales, suffixe "€".
- **Validation** : Édition du prix avec spinbox contraints et formatage.

## 3) Délégué de catégorie avec combo

- **Action** : Implémentez un `CategoryDelegate` avec `QComboBox` contenant des catégories prédéfinies.
- **Indice** : Liste : Électronique, Vêtements, Alimentaire, Maison, Sport.
- **Validation** : Sélection de catégorie via liste déroulante uniquement.

## 4) Délégué de quantité avec slider

- **Action** : Créez un `QuantityDelegate` utilisant `QSlider` pour des quantités de 0 à 100.
- **Piste** : Affichez la valeur numérique à côté du slider en temps réel.
- **Validation** : Édition intuitive des quantités avec slider visuel.

## 5) Délégué de date avec calendrier

- **Action** : Implémentez un `DateDelegate` avec `QDateEdit` et popup calendrier.
- **Indice** : Contrainte : pas de date future, format français DD/MM/YYYY.
- **Validation** : Sélection de date via calendrier avec validation.

## 6) Délégué conditionnel

- **Action** : Créez un délégué qui change selon la catégorie (ex: électronique → garantie, alimentaire → DLC).
- **Piste** : Vérifiez la valeur de la colonne catégorie pour choisir l'éditeur approprié.
- **Validation** : Interface d'édition adaptée au contexte de la ligne.

## 7) Validation croisée

- **Action** : Implémentez une validation qui vérifie la cohérence entre colonnes (ex: prix/quantité).
- **Indice** : Dans `setModelData()`, vérifiez les autres colonnes avant de valider.
- **Validation** : Empêche la saisie de données incohérentes.

## 8) Feedback visuel de validation

- **Action** : Colorez les cellules en rouge/vert selon la validité des données saisies.
- **Piste** : Utilisez `setStyleSheet()` sur l'éditeur et le rôle `BackgroundRole` du modèle.
- **Validation** : Retour visuel immédiat sur la validité des données.

---

## Exercices supplémentaires

- **Délégué avec auto-complétion** : Ajoutez un `QLineEdit` avec auto-complétion pour les noms d'articles.
- **Délégué image** : Créez un délégué permettant de sélectionner une image d'icône pour l'article.
- **Validation en temps réel** : Affichez des messages d'erreur pendant la saisie, pas seulement à la fin.
- **Délégué composite** : Créez un éditeur complexe combinant plusieurs widgets dans un même délégué.
