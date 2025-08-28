# TP4 - Application multi-timer avancée

**Durée** : 30 minutes

**Objectif** : Créer une application de gestion de timers multiples avec notifications, événements programmés et sauvegarde d'état.

**Pré-requis** : TP1 à TP3 terminés, compréhension des `QTimer` et signaux.

## 1) Structure de l'application

- **Action** : Créez un projet `tp_multi_timer` avec une fenêtre principale gérant plusieurs timers simultanés.
- **Validation** : Application de base avec interface de gestion de timers.

## 2) Classe Timer personnalisée

- **Action** : Créez une classe `CustomTimer` héritant de `QObject` avec nom, durée et état.
- **Piste** : Incluez des signaux pour `finished`, `tick`, `started`, `paused`.
- **Validation** : Classe timer avec toutes les fonctionnalités de base.

## 3) Interface de création de timer

- **Action** : Ajoutez un formulaire pour créer un nouveau timer (nom, heures, minutes, secondes).
- **Indice** : Utilisez `QSpinBox` pour la saisie temporelle et validation des valeurs.
- **Validation** : Formulaire fonctionnel créant des timers paramétrés.

## 4) Liste des timers actifs

- **Action** : Affichez tous les timers dans une liste avec leur progression et contrôles (play/pause/stop).
- **Piste** : Utilisez `QListWidget` avec des widgets personnalisés incluant `QProgressBar`.
- **Validation** : Liste dynamique montrant l'état de tous les timers.

## 5) Gestion simultanée

- **Action** : Permettez le démarrage, pause et arrêt de plusieurs timers en parallèle.
- **Indice** : Chaque timer doit avoir son propre `QTimer` interne et gérer son état indépendamment.
- **Validation** : Plusieurs timers peuvent fonctionner simultanément sans interférence.

## 6) Notifications de fin

- **Action** : Implémentez des notifications quand un timer se termine (son, popup, changement visuel).
- **Piste** : Utilisez `QMessageBox` ou `QSystemTrayIcon` pour les notifications.
- **Validation** : Notification claire quand un timer arrive à expiration.

## 7) Événements programmés

- **Action** : Ajoutez la possibilité de programmer des actions à des moments spécifiques (ex: dans 30min).
- **Indice** : Calculez le délai avec `QDateTime` et utilisez `QTimer.singleShot()`.
- **Validation** : Événements futurs programmés s'exécutent au bon moment.

## 8) Sauvegarde et restauration

- **Action** : Sauvegardez l'état des timers dans un fichier JSON et restaurez-les au redémarrage.
- **Piste** : Sérialisez l'état, la progression et les paramètres de chaque timer.
- **Validation** : L'application conserve l'état des timers entre les sessions.

---

## Exercices supplémentaires

- **Templates de timers** : Créez des modèles prédéfinis (Pomodoro 25min, pause 5min, etc.).
- **Minuteur décompte** : Ajoutez des timers en mode décompte avec affichage temps restant.
- **Historique** : Gardez un historique des timers terminés avec statistiques.
- **Sons personnalisés** : Permettez de choisir différents sons de notification par timer.
