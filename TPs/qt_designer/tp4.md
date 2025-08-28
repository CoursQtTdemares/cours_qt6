# TP4 - Intégration VSCode complète

**Durée** : 30 minutes

**Objectif** : Configurer l'environnement VSCode pour Qt Designer et créer un workflow de développement automatisé.

**Pré-requis** : TP1 à TP3 terminés, VSCode installé et configuré.

## 1) Extensions VSCode pour Qt

- **Action** : Installez et configurez les extensions VSCode nécessaires pour Qt Designer.
- **Piste** : "Qt for Python", "XML Tools", et éventuellement "Python Preview".
- **Validation** : Extensions installées et fichiers .ui reconnus avec coloration syntaxique.

## 2) Configuration des tâches VSCode

- **Action** : Créez un fichier `.vscode/tasks.json` pour automatiser les tâches Qt.
- **Indice** : Tâches pour ouvrir Designer, compiler .ui vers .py, et watcher automatique.
- **Validation** : Menu "Terminal > Run Task" affiche vos tâches Qt personnalisées.

## 3) Commande de compilation automatique

- **Action** : Configurez une tâche qui compile automatiquement tous les fichiers .ui modifiés.
- **Piste** : Script utilisant `find` et `pyuic6` avec détection des modifications.
- **Validation** : Compilation automatique des fichiers .ui lors des modifications.

## 4) Configuration de débogage

- **Action** : Configurez `.vscode/launch.json` pour déboguer les applications utilisant Designer.
- **Indice** : Configuration spéciale pour PyQt6 avec variables d'environnement appropriées.
- **Validation** : Débogage fonctionnel avec breakpoints dans le code Python chargeant les .ui.

## 5) Snippets pour Qt Designer

- **Action** : Créez des snippets VSCode pour les patterns courants d'intégration Designer.
- **Piste** : Snippets pour `uic.loadUi()`, classe avec interface Designer, connexions signaux.
- **Validation** : Snippets accessibles via autocomplétion pour accélérer le développement.

## 6) Script d'intégration automatique

- **Action** : Développez un script Python qui surveille et compile automatiquement les fichiers .ui.
- **Indice** : Surveillance des modifications avec `watchdog` et compilation conditionnelle.
- **Validation** : Script surveillant le dossier ui/ et compilant automatiquement.

## 7) Workflow de développement optimisé

- **Action** : Créez un workflow complet : Designer → Compilation → Test → Debug.
- **Piste** : Raccourcis clavier, tâches automatiques, et intégration fluide entre outils.
- **Validation** : Workflow permettant des itérations rapides design → code → test.

## 8) Documentation du workflow

- **Action** : Documentez votre configuration dans un README.md pour l'équipe.
- **Indice** : Instructions d'installation, utilisation des tâches, et bonnes pratiques.
- **Validation** : Documentation claire permettant à un nouveau développeur de reproduire l'environnement.

---

## Exercices supplémentaires

- **Git hooks** : Configurez des hooks Git pour compiler automatiquement les .ui avant commit.
- **Live reload** : Implémentez un système de rechargement automatique de l'interface pendant le développement.
- **Template de projet** : Créez un template VSCode avec toute la configuration Qt prête.
- **Extension personnalisée** : Développez une extension VSCode simple pour des commandes Qt personnalisées.
