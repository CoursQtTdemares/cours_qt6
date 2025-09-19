# TP1 - Première interface avec Designer

**Durée** : 20 minutes

**Objectif** : Maîtriser le workflow de base Qt Designer → Python avec chargement dynamique.

**Pré-requis** : Chapitre 4 maîtrisé, Qt Designer installé via `uv run pyqt6-tools designer`.

## 1) Lancement de Qt Designer

- **Action** : Lancez Qt Designer et créez une nouvelle **MainWindow**.
- **Piste** : `uv run pyqt6-tools designer` puis "Main Window" dans le dialogue New Form.
- **Validation** : Qt Designer ouvert avec une MainWindow vide et les zones (Widget Box, Property Editor) visibles.

## 2) Création de l'interface simple

- **Action** : Ajoutez un **QPushButton** et un **QLabel** au widget central.
- **Indice** : Glissez-déposez depuis Widget Box, positionnez le bouton au-dessus du label.
- **Validation** : Interface avec un bouton "PushButton" et un label "TextLabel" visible.

## 3) Configuration des propriétés importantes

- **Action** : Configurez les **objectName** et textes des widgets.
- **Piste** : Bouton → objectName: `clickButton`, text: "Cliquer ici" | Label → objectName: `resultLabel`, text: "Résultat affiché ici".
- **Validation** : Widgets avec noms et textes personnalisés dans Property Editor.

## 4) Application d'un layout

- **Action** : Sélectionnez les widgets et appliquez un **Vertical Layout**.
- **Indice** : Sélection multiple (Ctrl+clic), puis clic-droit → "Lay Out Vertically".
- **Validation** : Widgets organisés verticalement avec redimensionnement automatique.

## 5) Sauvegarde du fichier .ui

- **Action** : Sauvegardez l'interface en `simple_interface.ui`.
- **Piste** : File → Save, choisir le nom et l'emplacement approprié.
- **Validation** : Fichier `simple_interface.ui` créé et test Preview dans Designer fonctionnel.

## 6) Chargement dynamique en Python

- **Action** : Créez `main.py` qui charge l'interface avec `uic.loadUi()`.
- **Indice** : Utilisez le code de base du cours avec chemin relatif sécurisé.
- **Validation** : Script Python qui affiche l'interface Designer au lancement.

## 7) Connexion du signal au slot

- **Action** : Connectez le bouton à une fonction qui modifie le texte du label.
- **Piste** : `self.clickButton.clicked.connect(self.handle_click)` et fonction qui change `self.resultLabel.setText()`.
- **Validation** : Clic sur le bouton change le texte du label (ex: "Bouton cliqué !").

## 8) Test et finalisation

- **Action** : Testez l'application complète et vérifiez toutes les interactions.
- **Validation** : Application fonctionnelle avec interface Designer chargée et interaction bouton-label opérationnelle.

---

## Exercices supplémentaires

- **QLineEdit** : Ajoutez un champ de saisie qui modifie le label en temps réel.
- **QComboBox** : Ajoutez une liste déroulante qui change la couleur du label.
- **QCheckBox** : Ajoutez une case qui active/désactive le bouton principal.
- **Layouts** : Expérimentez avec GridLayout pour une organisation en grille.
