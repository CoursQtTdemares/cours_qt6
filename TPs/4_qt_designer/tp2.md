# TP2 - Compilation avec pyuic6

**Durée** : 15 minutes

**Objectif** : Comprendre la compilation .ui → Python et comparer les deux approches d'intégration.

**Pré-requis** : TP1 terminé avec `simple_interface.ui` fonctionnel.

## 1) Compilation du fichier .ui

- **Action** : Compilez `simple_interface.ui` vers un fichier Python avec **pyuic6**.
- **Piste** : `pyuic6 simple_interface.ui -o ui_simple_interface.py` dans le terminal.
- **Validation** : Fichier `ui_simple_interface.py` généré avec classe `Ui_MainWindow`.

## 2) Examen du code généré

- **Action** : Ouvrez et analysez le fichier Python généré par pyuic6.
- **Indice** : Observez la méthode `setupUi()`, `retranslateUi()` et les widgets créés.
- **Validation** : Compréhension de la structure du code généré et des noms de widgets.

## 3) Création de la classe d'application

- **Action** : Créez `main_compiled.py` qui hérite de la classe générée.
- **Piste** : `class MainWindow(QMainWindow, Ui_MainWindow):` puis `self.setupUi(self)` dans `__init__`.
- **Validation** : Classe Python qui utilise l'héritage multiple pour intégrer l'interface.

## 4) Adaptation des connexions

- **Action** : Adaptez les connexions de signaux pour la version compilée.
- **Indice** : Les widgets sont directement accessibles (pas de vérification `hasattr` nécessaire).
- **Validation** : Connexions fonctionnelles avec accès direct aux widgets `self.clickButton`, `self.resultLabel`.

## 5) Personnalisation post-setupUi

- **Action** : Ajoutez des personnalisations après `setupUi()` comme dans l'exemple du cours.
- **Piste** : Modification de la police, alignement, ou autres propriétés non définies dans Designer.
- **Validation** : Interface personnalisée avec modifications visibles (police plus grande, alignement, etc.).

## 6) Test des deux versions

- **Action** : Lancez et comparez `main.py` (loadUi) et `main_compiled.py` (compilée).
- **Indice** : Vérifiez que les deux versions ont le même comportement fonctionnel.
- **Validation** : Deux applications identiques fonctionnellement, une avec chargement dynamique, une compilée.

## 7) Analyse des performances

- **Action** : Observez le temps de démarrage et l'autocomplétion IDE des deux approches.
- **Piste** : Version compilée légèrement plus rapide, meilleure autocomplétion des widgets.
- **Validation** : Compréhension pratique des différences entre les deux méthodes.

## 8) Choix de l'approche

- **Action** : Documentez dans un commentaire quand utiliser chaque approche.
- **Indice** : `uic.loadUi()` pour prototypage/apprentissage, compilation pour production.
- **Validation** : Compréhension claire du workflow optimal selon le contexte de développement.

---

## Exercices supplémentaires

- **Script de compilation** : Créez un script qui compile automatiquement tous les .ui d'un dossier.
- **Workflow hybride** : Testez le développement avec .ui pour le design et compilation avant déploiement.
- **Comparaison de taille** : Comparez la taille des applications avec/sans dépendance au fichier .ui.
- **Integration continue** : Intégrez la compilation dans un workflow de développement automatisé.
