# TP2 - Configuration VSCode et premier debug

**Durée** : 20 minutes

**Objectif** : Configurer VSCode pour Python/uv, poser un point d'arrêt, déboguer un script PyQt6 et inspecter une variable.

**Pré-requis** : TP1 réussi (projet `uv` avec script `hello_qt`).

## 1) Extensions VSCode indispensables

- **Action** : Installez l'extension officielle Python et, si besoin, Pylance.
- **Indice** : Marketplace VSCode (icône carré), recherchez "Python" par Microsoft.

## 2) Sélection de l'interpréteur

- **Action** : Sélectionnez l'interpréteur Python utilisé par `uv` pour le dossier du projet.
- **Indice** : Palette > "Python: Select Interpreter". Vérifiez que la résolution des imports PyQt6 fonctionne (aucune erreur de type non résolu sur `from PyQt6 import QtWidgets`).

## 3) Créer une configuration de débogage

- **Action** : Générez un `launch.json` minimal pour lancer le script PyQt6.
- **Piste** : Onglet Run and Debug > create a launch.json > Python > Module ou Script.
- **Validation** : Un bouton "Run" exécute votre app.

## 4) Poser un breakpoint et démarrer le débogueur

- **Action** : Ajoutez une variable locale avant la création du widget (ex: `message = "Bonjour Qt"`) puis référencez-la dans le label.
- **Action** : Placez un point d'arrêt sur la ligne où le label est créé.
- **Validation** : En débogage, VSCode doit s'arrêter sur le breakpoint; inspectez `message`.

## 5) Pas à pas et Watches

- **Action** : Utilisez Step Over/Into/Out pour avancer pas à pas.
- **Indice** : Ajoutez `app` ou votre widget dans la fenêtre "Variables" ou "Watch".

## 6) Télémétrie rapide

- **Action** : Affichez la taille de la fenêtre en runtime.
- **Piste** : Recherchez `QWidget.size()` ou `geometry()` dans la doc PyQt6/Qt.
- **Validation** : En pause débogueur, inspectez la valeur retournée.

---

## Exercices supplémentaires

- **Points d'arrêts conditionnels** : Créez un compteur de clics sur un bouton, ajoutez un breakpoint conditionnel (par ex, `compteur == 5`).
- **Logs** : Ajoutez un log à la levée d'un signal (piste: connexion signal/slot), observez-le en console.