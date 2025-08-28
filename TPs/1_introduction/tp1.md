# TP1 - Installation et validation de l'environnement

**Durée** : 15 minutes

**Objectif** : Disposer d'un environnement Python fonctionnel avec `uv`, exécuter un mini script PyQt6 et valider que VSCode détecte l'interpréteur.

**Pré-requis** : Python récent installé.

## 1) Créer l'espace de travail du TP

- **Action** : Dans un terminal, créez un dossier de travail `tp_intro_env` et ouvrez-le dans VSCode.
- **Indice** : 
  - Commandes shell utiles: `mkdir`, `cd`.
  - Pour ouvrir VSCode depuis le terminal, on peut taper `code .` (si `code` est disponible). Sinon ouvrez VSCode puis `File > Open Folder...`.

## 2) Installer `uv` (gestionnaire Python rapide)

- **Action** : Installez `uv` si nécessaire.
- **Piste** : Consultez la documentation `uv` (mot-clés: "astral uv install") pour la commande d'installation.
- **Validation** : `uv --version` doit afficher un numéro de version.

## 3) Initialiser un projet minimal

- **Action** : Initialisez la structure d'un projet Python simple.
- **Indice** : `uv init` permet de créer un projet. Le but est d'obtenir un `pyproject.toml`.
- **Option** : Si vous préférez sans modèle, créez vous-même `pyproject.toml` et un dossier `src/`.

## 4) Ajouter PyQt6 comme dépendance

- **Action** : Ajoutez `PyQt6` avec `uv`.
- **Indice** : Cherchez la commande `uv add ...`.
- **Validation** : Le fichier `pyproject.toml` doit lister `PyQt6` dans les dépendances et `uv sync` ne doit pas afficher d'erreurs.

## 5) Créer un premier script de validation

- **Action** : A la racine du projet, créez `hello_qt.py` qui ouvre une fenêtre minimale.
- **Guides** : 
  - Cherchez comment créer une `QApplication` et une `QLabel` avec PyQt6.
  - Lancez la boucle d'événements (indice: `app.exec()` en PyQt6).
- **Validation** : Lancer `uv run hello_qt.py` (ou une autre commande équivalente selon votre structure) doit afficher une petite fenêtre avec du texte.

---

## Exercices supplémentaires (pour aller plus loin)

- **Essayer d'autres version de Qt en python** : Essayer de modifier le code pour utiliser PyQt5 ou PySide6.
- **Test rapide** : Ajoutez un test trivial (ex: fonction qui renvoie une chaîne) et exécutez-le avec `uv run pytest` (indice: ajouter `pytest`).
- **Style** : Créez une feuille de style `.qss` minimale et appliquez-la à votre widget.
