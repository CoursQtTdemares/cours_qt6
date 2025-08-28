# TP4 - Synchronisation des composants

**Durée** : 25 minutes

**Objectif** : Interconnecter les différents éléments d'interface (menus, barres d'outils, actions) et implémenter un système de communication par signaux personnalisés.

**Pré-requis** : TP1, TP2 et TP3 terminés avec une application complète.

## 1) Actions partagées entre composants

- **Action** : Refactorisez vos actions pour qu'elles soient partagées entre menus et barres d'outils.
- **Indice** : 
  - Créez les `QAction` une seule fois dans une méthode dédiée
  - Ajoutez ces actions à la fois aux menus et aux barres d'outils
  - Stockez les actions importantes comme attributs de classe (`self.save_action`)
- **Validation** : Modifier l'état d'une action (enabled/disabled) affecte simultanément le menu et la barre d'outils

## 2) Gestion d'état cohérente

- **Action** : Implémentez une logique qui maintient la cohérence entre les différents éléments d'interface.
- **Piste** : 
  - L'action "Sauvegarder" doit se désactiver après sauvegarde
  - Le titre de la fenêtre doit indiquer si le document est modifié (astérisque)
  - La barre de statut doit refléter l'état actuel de l'application
- **Validation** : L'interface reste cohérente quelque soit la façon dont l'utilisateur interagit

## 3) Signal personnalisé pour l'état de document

- **Action** : Créez un signal personnalisé `document_state_changed` qui notifie les changements d'état.
- **Indice** : 
  - Utilisez `pyqtSignal(bool)` pour indiquer si le document est modifié
  - Émettez ce signal lors des actions qui modifient le document
  - Connectez ce signal à une méthode qui met à jour l'interface
- **Validation** : Toute modification de document met automatiquement à jour l'interface

## 4) Menu Affichage avec contrôles d'interface

- **Action** : Ajoutez un menu "Affichage" permettant de masquer/afficher les barres d'interface.
- **Piste** : 
  - Créez des actions checkables pour "Barre d'outils" et "Barre de statut"
  - Connectez ces actions aux méthodes `setVisible()` des barres correspondantes
  - Synchronisez l'état des actions avec la visibilité réelle des barres
- **Validation** : Les actions du menu reflètent l'état actuel et permettent de contrôler l'affichage

## 5) Communication bidirectionnelle

- **Action** : Implémentez une communication bidirectionnelle entre la barre de statut et les actions.
- **Indice** : 
  - Ajoutez un widget permanent dans la barre de statut (ex: compteur d'actions)
  - Incrémentez ce compteur à chaque action effectuée
  - Permettez de remettre à zéro via un bouton dans la barre de statut
- **Validation** : Les interactions dans la barre de statut affectent le comportement de l'application

## 6) Signaux en cascade

- **Action** : Créez une chaîne de signaux qui se propagent à travers différents composants.
- **Piste** : 
  - Un clic sur "Nouveau" émet un signal qui déclenche la réinitialisation
  - Cette réinitialisation émet à son tour un signal de changement d'état
  - Ce changement d'état met à jour les menus, barres et titre de fenêtre
- **Validation** : Une seule action déclenche une mise à jour en cascade de toute l'interface

## 7) Système de notifications internes

- **Action** : Implémentez un système de notifications qui affiche des messages colorés dans la barre de statut.
- **Indice** : 
  - Créez un signal `show_notification(message, type)` avec différents types (info, success, warning, error)
  - Utilisez des QLabel colorés dans la barre de statut qui s'auto-suppriment
  - Connectez ce signal aux différentes actions pour donner du feedback
- **Validation** : Les actions importantes affichent des notifications visuelles appropriées

---

## Exercices supplémentaires

- **Historique d'actions** : Implémentez un historique des actions effectuées accessible via un menu ou un panneau.
- **Mode debug** : Ajoutez un mode debug qui affiche tous les signaux émis dans la console ou un panneau dédié.
- **Synchronisation de préférences** : Créez un système où modifier une préférence met automatiquement à jour tous les composants concernés.
- **États de l'application** : Implémentez différents états de l'application (Chargement, Prêt, Occupé) avec mise à jour automatique de l'interface.
- **Connecteurs intelligents** : Créez des décorateurs ou des classes helper pour automatiser la connexion de signaux fréquents.
- **Tests de synchronisation** : Écrivez des tests unitaires qui vérifient que les signaux sont bien émis et connectés correctement.
