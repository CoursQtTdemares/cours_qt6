# TP3 - Navigation dans la documentation

**Durée** : 15 minutes

**Objectif** : Savoir trouver rapidement une information dans la documentation Qt/PyQt et l'appliquer à un cas simple.

**Pré-requis** : Avoir un projet PyQt6 fonctionnel (TP1) et VSCode configuré (TP2).

## 1) Identifier les bonnes ressources

- **Action** : Ouvrez la doc Qt (C++) et la doc PyQt6.
- **Indice** : Cherchez "Qt Widgets" et "PyQt6 reference". Note: les API PyQt6 référencent souvent les pages Qt (C++), la correspondance nom d'API est prévisible.

## 2) Trouver une propriété utile de `QLabel`

- **Action** : Recherchez comment afficher du texte riche (HTML simple) dans un `QLabel`.
- **Piste** : Comparez `setText` vs `setTextFormat` et repérez le type `Qt.RichText`.
- **Validation** : Modifiez votre `hello_qt` pour afficher un texte en gras ou coloré.

## 3) Trouver un signal d'intérêt sur un bouton

- **Action** : Dans la doc de `QPushButton`, identifiez au moins un signal clé (ex: `clicked`).
- **Piste** : Regardez aussi `toggled` si le bouton est checkable.
- **Validation** : Ajoutez un bouton qui modifie le texte du label à chaque clic.

## 4) Comprendre la hiérarchie des classes

- **Action** : Visualisez les classes parentes de `QLabel` et `QPushButton`.
- **Piste** : Remontez vers `QWidget` et `QObject` pour repérer l'héritage commun (signaux/slots, événements).

## 5) Mini challenge doc

- **Action** : Cherchez comment définir une icône de fenêtre.
- **Indice** : Mot-clés: `QWidget windowIcon`, `QIcon`, `setWindowIcon`.
- **Validation** : Appliquez une icône simple (fichier `.png`) si disponible.

---

## Exercices supplémentaires

- **Layout** : Recherchez la meilleure façon de disposer le label et le bouton (indice: `QVBoxLayout`, `QHBoxLayout`). Implémentez-le.
- **Accessibilité** : Trouvez comment définir un raccourci clavier pour le bouton (piste: `setShortcut` ou `&` dans le texte).
- **Doc offline** : Téléchargez la doc Qt offline et configurez une recherche rapide dans votre navigateur.