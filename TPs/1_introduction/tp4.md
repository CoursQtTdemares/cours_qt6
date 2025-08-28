# TP4 - Première application personnalisée

**Durée** : 30 minutes

**Objectif** : Assembler une petite fenêtre PyQt6 avec un layout, un champ de saisie, un bouton et une zone d'affichage, en respectant une structure de projet simple pilotée par `uv`.

**Pré-requis** : TP1 à TP3.

## 1) Structure minimale

- **Action** : Créez un fichier `src/app.py` qui contiendra une classe fenêtre principale.
- **Piste** : Héritez de `QWidget` (ou `QMainWindow` si vous préférez) et créez les widgets suivants: `QLineEdit`, `QPushButton`, `QTextEdit`.

## 2) Disposition

- **Action** : Placez les éléments dans un layout cohérent.
- **Indice** : `QVBoxLayout` pour empiler les éléments, `QHBoxLayout` pour aligner la zone de saisie et le bouton.
- **Validation** : La fenêtre s'adapte lorsque vous la redimensionnez.

## 3) Comportement

- **Action** : Au clic sur le bouton, récupérez le texte du `QLineEdit` et affichez-le dans le `QTextEdit` avec un horodatage.
- **Piste** : Connexion signal/slot sur `QPushButton.clicked`. Formatage horaire: regardez `datetime` de Python.

## 4) Petites finitions

- **Action** : Définissez un titre de fenêtre, une taille initiale, et (facultatif) une icône.
- **Action** : Appliquez un style simple (couleur de fond ou marges) via une feuille `.qss` ou `setStyleSheet`.

## 5) Point d'entrée et exécution

- **Action** : Ajoutez un `if __name__ == "__main__":` qui instancie `QApplication` et votre fenêtre.
- **Piste** : Centralisez le lancement dans `main.py`.

## 6) Test manuel

- **Action** : Tapez du texte, cliquez plusieurs fois, vérifiez que chaque clic ajoute une ligne avec heure + contenu.
- **Action** : Redimensionnez la fenêtre, vérifiez l'adaptabilité du layout.

---

## Exercices supplémentaires

- **Persistance** : Ajoutez une sauvegarde automatique du contenu du `QTextEdit` dans un fichier à la fermeture (piste: événement `closeEvent`).
- **Validation d'entrée** : Empêchez l'ajout de lignes vides, affichez un message d'aide (piste: `QMessageBox` ou couleur du champ).
- **Shortcut** : Ajoutez `Ctrl+Enter` pour déclencher l'action du bouton (piste: `QShortcut`).
- **Refactoring** : Séparez construction UI et logique dans des méthodes distinctes.