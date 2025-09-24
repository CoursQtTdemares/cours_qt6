# TP1 - Téléchargement asynchrone de données

**Durée** : 30 minutes

**Objectif** : Découvrir les threads avec QRunnable pour récupérer des données météo en parallèle.

**Pré-requis** : Chapitres 1-5 maîtrisés.

## 1) Créer le projet et fenêtre principale

- **Action** : Créez un projet `weather_threads_app` avec `WeatherMainWindow` héritant de `QMainWindow`.
- **Piste** : `uv init` puis `uv add PyQt6`. Ajoutez un `QPushButton` "Télécharger" et un `QTextEdit` pour afficher les résultats.
- **Validation** : Fenêtre avec bouton et zone de texte.

## 2) Classes WorkerSignals et WeatherWorker

- **Action** : Créez `WorkerSignals` avec signal `data_received` et `WeatherWorker` héritant de `QRunnable`.
- **Piste** : `data_received = pyqtSignal(str, int)` pour (ville, température). Worker avec `city` en paramètre.
- **Validation** : Classes de base créées avec signaux définis.

## 3) Méthode run() de simulation

- **Action** : Implémentez `run()` qui simule un téléchargement avec `time.sleep(2)` et température aléatoire.
- **Piste** : `time.sleep(2)`, `temp = random.randint(15, 25)`, émet les données avec le signal.
- **Validation** : Worker qui simule un délai et génère des données.

## 4) QThreadPool et lancement des workers

- **Action** : Ajoutez `QThreadPool` dans MainWindow et méthode qui lance 3 workers pour Paris, Lyon, Marseille.
- **Piste** : `self.thread_pool = QThreadPool()`, créer 3 workers dans une boucle, connecter les signaux.
- **Validation** : Pool de threads qui lance 3 téléchargements en parallèle.

## 5) Affichage des résultats

- **Action** : Connectez le signal `data_received` pour afficher les données dans le QTextEdit.
- **Piste** : Méthode `on_data_received()` qui fait `self.text_edit.append(f"{city}: {temp}°C")`.
- **Validation** : Données des workers s'affichent progressivement dans l'interface.

## 6) Connexion du bouton et test

- **Action** : Connectez le bouton au lancement des téléchargements et testez l'application complète.
- **Piste** : `self.download_button.clicked.connect(self.start_downloads)`. Interface reste réactive pendant les téléchargements.
- **Validation** : Application fonctionnelle, bouton lance 3 téléchargements, résultats apparaissent progressivement.

---

## Exercices supplémentaires

- **Indicateur** : Affichez "Téléchargement..." pendant les opérations.
- **Plus de villes** : Ajoutez Nice, Toulouse.
- **Gestion d'erreur** : Simulez parfois une erreur avec try/except.
