# TP1 - Formulaire avec layouts de base

**Durée** : 30 minutes

**Objectif** : Créer un formulaire d'inscription complet en utilisant les layouts verticaux et horizontaux, avec validation des entrées utilisateur.

**Pré-requis** : Maîtrise des bases PyQt6 (chapitres 1-2).

## 1) Créer la structure du projet

- **Action** : Créez un nouveau projet `tp_formulaire` avec `uv` et ajoutez PyQt6.
- **Validation** : Le projet s'initialise correctement et PyQt6 est installé.

## 2) Créer la fenêtre principale

- **Action** : Dans `main_window.py`, créez une classe `FormWindow` héritant de `QMainWindow`.
- **Piste** : Utilisez un widget central avec un layout vertical principal.
- **Validation** : Une fenêtre vide s'affiche avec un titre approprié.

## 3) Section informations personnelles

- **Action** : Créez une première section avec les champs : Prénom, Nom, Email.
- **Indice** : Utilisez `QHBoxLayout` pour chaque ligne "Label + QLineEdit".
- **Validation** : Trois lignes bien alignées avec labels à gauche, champs à droite.

## 4) Section adresse 

- **Action** : Ajoutez une section adresse avec : Rue, Code postal, Ville, Pays (liste déroulante).
- **Piste** : `QComboBox` pour le pays, recherchez comment ajouter des éléments.
- **Validation** : Tous les champs sont présents et la liste pays fonctionne.

## 5) Section préférences

- **Action** : Créez une section avec : Âge (`QSpinBox`), Newsletter (`QCheckBox`), Commentaires (`QTextEdit`).
- **Indice** : Limitez l'âge entre 16 et 99 ans, et la hauteur du `QTextEdit` à 3 lignes.
- **Validation** : Les contrôles respectent les contraintes définies.

## 6) Boutons d'action

- **Action** : Ajoutez en bas les boutons "Valider" et "Annuler" dans un layout horizontal.
- **Piste** : Utilisez `addStretch()` pour pousser les boutons vers la droite.
- **Validation** : Les boutons sont alignés à droite en bas du formulaire.

## 7) Validation simple

- **Action** : Connectez le bouton "Valider" pour afficher les données saisies.
- **Indice** : Récupérez les valeurs avec `.text()`, `.value()`, `.isChecked()`, etc.
- **Validation** : Un `QMessageBox` affiche un résumé des informations saisies.

---

## Exercices supplémentaires

- **Validation avancée** : Vérifiez que l'email contient "@" et que les champs obligatoires sont remplis.
- **Amélioration visuelle** : Ajoutez des séparateurs visuels entre les sections (piste: `QFrame` avec `setFrameStyle()`).
- **Sauvegarde** : Exportez les données du formulaire dans un fichier JSON.
