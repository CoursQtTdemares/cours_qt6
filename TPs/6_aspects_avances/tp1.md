# TP1 - Interface MDI météo de base

**Durée** : 30 minutes

**Objectif** : Découvrir l'architecture MDI avec QMdiArea et créer une application météo simple.

**Pré-requis** : Chapitres 1-5 maîtrisés.

## 1) Créer le projet et fenêtre principale

- **Action** : Créez un projet `weather_mdi_app` avec `WeatherMainWindow` héritant de `QMainWindow`.
- **Piste** : `uv init` puis `uv add PyQt6`. Ajoutez `QMdiArea` comme widget central.
- **Validation** : Fenêtre principale avec zone MDI vide.

## 2) Première sous-fenêtre "Météo actuelle"

- **Action** : Créez une méthode `create_current_view()` qui ajoute une sous-fenêtre avec QLabel.
- **Piste** : `sub_window = QMdiSubWindow()`, `sub_window.setWidget(QLabel("Météo : 22°C"))`, `self.mdi_area.addSubWindow(sub_window)`.
- **Validation** : Sous-fenêtre visible avec texte météo.

## 3) Deuxième sous-fenêtre "Prévisions"

- **Action** : Créez `create_forecast_view()` avec QTextEdit contenant les prévisions de 3 jours.
- **Piste** : QTextEdit en lecture seule avec texte "Demain: 24°C\nAprès-demain: 20°C\n...".
- **Validation** : Deuxième sous-fenêtre avec prévisions affichées.

## 4) Menu Fenêtre avec dispositions

- **Action** : Ajoutez un menu "Fenêtre" avec actions "Cascade" et "Mosaïque".
- **Piste** : `window_menu = menubar.addMenu("Fenêtre")` puis `self.mdi_area.cascadeSubWindows()`.
- **Validation** : Menu fonctionnel qui réorganise les fenêtres.

## 5) Configuration automatique

- **Action** : Créez les 2 sous-fenêtres automatiquement au démarrage en cascade.
- **Piste** : Appelez les méthodes dans `__init__()` puis `self.mdi_area.cascadeSubWindows()`.
- **Validation** : Application démarre avec 2 fenêtres organisées.

## 6) Application complète

- **Action** : Finalisez avec fonction `main()` et testez toutes les fonctionnalités MDI.
- **Piste** : Boucle d'événements classique. Testez la fermeture, redimensionnement des sous-fenêtres.
- **Validation** : Application MDI complète et interactive.

---

## Exercices supplémentaires

- **Troisième fenêtre** : Ajoutez "Graphiques" pour le TP2.
- **Icônes** : Ajoutez des icônes ☀️ 📊 aux sous-fenêtres.
- **Menu Fichier** : Ajoutez "Quitter" dans un menu Fichier.