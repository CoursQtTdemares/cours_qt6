# TP1 - Gestionnaire d'événements interactif

**Durée** : 30 minutes

**Objectif** : Créer une application qui capture et affiche tous types d'événements, en implémentant des filtres d'événements personnalisés.

**Pré-requis** : Chapitres 1-3 maîtrisés, notions de base sur les événements Qt.

## 1) Application moniteur d'événements

- **Action** : Créez un projet `tp_event_monitor` avec une fenêtre principale pour capturer les événements.
- **Validation** : Fenêtre de base fonctionnelle avec PyQt6.

## 2) Zone d'affichage des événements

- **Action** : Ajoutez un `QTextEdit` en lecture seule pour afficher la liste des événements capturés.
- **Piste** : Utilisez `setReadOnly(True)` et `append()` pour ajouter du texte.
- **Validation** : Zone de texte prête à recevoir les logs d'événements.

## 3) Capture des événements souris

- **Action** : Surchargez `mousePressEvent()`, `mouseReleaseEvent()` et `mouseMoveEvent()`.
- **Indice** : Récupérez la position avec `event.position()` et le bouton avec `event.button()`.
- **Validation** : Les clics de souris s'affichent avec position et bouton dans la zone de log.

## 4) Capture des événements clavier

- **Action** : Implémentez `keyPressEvent()` et `keyReleaseEvent()`.
- **Piste** : Utilisez `event.text()` pour les caractères et `event.key()` pour les touches spéciales.
- **Validation** : La frappe clavier génère des logs détaillés.

## 5) Filtrage sélectif

- **Action** : Ajoutez des cases à cocher pour activer/désactiver certains types d'événements.
- **Indice** : Créez des flags booléens et vérifiez-les avant de logger les événements.
- **Validation** : Possibilité de filtrer les types d'événements affichés.

## 6) Filtre d'événements global

- **Action** : Implémentez un `eventFilter()` pour capturer les événements sur tous les widgets.
- **Piste** : Installez le filtre avec `installEventFilter(self)` et recherchez les types d'événements Qt.
- **Validation** : Capture des événements même sur les widgets enfants.

## 7) Statistiques d'événements

- **Action** : Comptez et affichez le nombre d'événements par type en temps réel.
- **Indice** : Utilisez un dictionnaire pour compter et un `QLabel` pour afficher.
- **Validation** : Affichage en temps réel des statistiques d'événements.

## 8) Fonction de nettoyage

- **Action** : Ajoutez un bouton pour vider le log et remettre les compteurs à zéro.
- **Validation** : Le bouton efface complètement l'historique et les statistiques.

---

## Exercices supplémentaires

- **Sauvegarde des logs** : Exportez l'historique des événements dans un fichier texte.
- **Filtrage avancé** : Ajoutez un système de filtrage par mots-clés ou expressions régulières.
- **Événements chronométrés** : Affichez le temps écoulé entre deux événements identiques.
- **Mode replay** : Enregistrez une séquence d'événements et permettez sa reproduction.
