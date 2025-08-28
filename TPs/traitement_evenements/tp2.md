# TP2 - Système de signaux personnalisés

**Durée** : 30 minutes  

**Objectif** : Développer un système de communication entre composants avec des signaux personnalisés, paramètres multiples et gestion d'erreurs.

**Pré-requis** : TP1 terminé, compréhension des signaux/slots de base.

## 1) Architecture de communication

- **Action** : Créez un projet `tp_signaux_custom` avec une classe `EventManager` héritant de `QObject`.
- **Piste** : Cette classe centralisera tous les signaux personnalisés de l'application.
- **Validation** : Classe de base fonctionnelle avec héritage `QObject` correct.

## 2) Signaux de données multiples

- **Action** : Définissez des signaux avec surcharge pour différents types : `dataChanged[int]`, `dataChanged[str]`, `dataChanged[dict]`.
- **Indice** : Utilisez `pyqtSignal([int], [str], [dict])` pour créer des surcharges.
- **Validation** : Trois versions du signal `dataChanged` disponibles.

## 3) Signal de progression avec validation

- **Action** : Créez un signal `progressUpdate` avec paramètres (pourcentage, message, temps_restant).
- **Piste** : Définissez comme `pyqtSignal(int, str, int)` pour pourcentage, message et temps.
- **Validation** : Signal composé fonctionnel avec paramètres multiples.

## 4) Gestionnaire de tâches émetteur

- **Action** : Créez une classe `TaskProcessor` qui émet les signaux pendant un traitement simulé.
- **Indice** : Utilisez `QTimer` ou `QThread.msleep()` pour simuler du travail et émettre des signaux.
- **Validation** : Les signaux de progression sont émis périodiquement.

## 5) Interface de réception

- **Action** : Créez une fenêtre avec `QProgressBar`, `QLabel` pour messages, et zone de log.
- **Piste** : Connectez ces widgets aux signaux de l'`EventManager`.
- **Validation** : Interface mise à jour en temps réel par les signaux.

## 6) Gestion d'erreurs par signaux

- **Action** : Ajoutez un signal `errorOccurred` avec niveau de gravité et message.
- **Indice** : Créez une énumération pour les niveaux (INFO, WARNING, ERROR, CRITICAL).
- **Validation** : Les erreurs sont signalées et affichées différemment selon leur gravité.

## 7) Signal de communication inter-composants

- **Action** : Créez un signal `componentMessage` pour faire communiquer différents widgets.
- **Piste** : Incluez l'ID du composant émetteur, l'ID du destinataire et le message.
- **Validation** : Un widget peut envoyer des messages ciblés à un autre widget.

## 8) Déconnexion dynamique

- **Action** : Implémentez un système pour connecter/déconnecter les signaux à la volée.
- **Indice** : Boutons pour activer/désactiver certaines connexions signal-slot.
- **Validation** : Possibilité de gérer les connexions dynamiquement.

---

## Exercices supplémentaires

- **Signal avec priorité** : Ajoutez un système de priorité pour traiter certains signaux avant d'autres.
- **Broadcasting** : Créez un signal qui peut être envoyé à tous les composants connectés.
- **Signal avec callback** : Implémentez un mécanisme où l'émetteur peut recevoir une confirmation de réception.
- **Logging avancé** : Enregistrez tous les signaux émis avec timestamp et traçabilité.
