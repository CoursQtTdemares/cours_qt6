# TP3 - Téléchargement asynchrone de données

**Durée** : 30 minutes

**Objectif** : Découvrir les threads avec QRunnable pour simuler des téléchargements météo.

**Pré-requis** : TP1 et TP2 terminés et fonctionnels.

## 1) Classe WorkerSignals et WeatherWorker

- **Action** : Créez `WorkerSignals` avec signal `data_received` et `WeatherWorker` héritant de `QRunnable`.
- **Piste** : `data_received = pyqtSignal(str, int)` pour (ville, température). Worker avec `city` en paramètre.
- **Validation** : Classes de base créées avec signaux définis.

## 2) Méthode run() de simulation

- **Action** : Implémentez `run()` qui simule un téléchargement avec `time.sleep(2)` et données aléatoires.
- **Piste** : `time.sleep(2)`, `temp = random.randint(15, 25)`, `self.signals.data_received.emit(self.city, temp)`.
- **Validation** : Worker qui simule un délai et émet des données.

## 3) QThreadPool dans MainWindow

- **Action** : Ajoutez `QThreadPool` dans la fenêtre principale et méthode pour lancer les workers.
- **Piste** : `self.thread_pool = QThreadPool()`, méthode `download_weather()` qui crée et lance des workers.
- **Validation** : Pool de threads initialisé et prêt à recevoir des tâches.

## 4) Nouvelle sous-fenêtre "Données temps réel"

- **Action** : Créez `create_realtime_view()` avec QTextEdit pour afficher les données reçues.
- **Piste** : QTextEdit en lecture seule, méthode `on_data_received()` qui fait `append()`.
- **Validation** : Sous-fenêtre prête à recevoir les données des workers.

## 5) Connexion des signaux

- **Action** : Connectez le signal `data_received` à `on_data_received()` pour mettre à jour l'interface.
- **Piste** : `worker.signals.data_received.connect(self.on_data_received)` avant `thread_pool.start()`.
- **Validation** : Données des workers s'affichent dans l'interface.

## 6) Bouton de téléchargement

- **Action** : Ajoutez un bouton "🌍 Actualiser" qui lance 3 workers pour Paris, Lyon, Marseille.
- **Piste** : Bouton dans la barre d'outils, méthode qui crée 3 workers en parallèle.
- **Validation** : Données apparaissent progressivement, interface reste réactive.

---

## Exercices supplémentaires

- **Indicateur** : Affichez "Téléchargement..." pendant les opérations.
- **Plus de villes** : Ajoutez Nice, Toulouse, Bordeaux.
- **Gestion d'erreur** : Simulez parfois une erreur dans le worker.