# TP2 - Signaux/slots et validation

**Durée** : 30 minutes  

**Objectif** : Implémenter la validation de formulaire avec signaux/slots en mixant connexions Designer et programmation Python.

**Pré-requis** : TP1 terminé, compréhension des signaux/slots de base.

## 1) Connexions simples dans Designer

- **Action** : Ouvrez `contact_form.ui` et utilisez l'éditeur de signaux/slots de Designer.
- **Piste** : Mode "Edit Signals/Slots" pour connecter visuellement les éléments.
- **Validation** : Au moins 2 connexions réalisées directement dans Designer.

## 2) Bouton Clear automatique

- **Action** : Connectez un bouton "Effacer" pour vider automatiquement tous les champs.
- **Indice** : Signal `clicked()` du bouton vers slot `clear()` des `QLineEdit`.
- **Validation** : Bouton qui efface tous les champs sans code Python.

## 3) Synchronisation des champs

- **Action** : Connectez le `QCheckBox` "Contact professionnel" pour activer/désactiver certains champs.
- **Piste** : Signal `toggled(bool)` vers slot `setEnabled(bool)` des champs concernés.
- **Validation** : Case à cocher qui contrôle l'état d'autres widgets.

## 4) Intégration Python

- **Action** : Créez `contact_dialog.py` qui charge le fichier `.ui` et ajoute la logique métier.
- **Indice** : Utilisez `uic.loadUi()` pour charger l'interface, puis connectez les signaux complexes.
- **Validation** : Classe Python fonctionnelle chargeant l'interface Designer.

## 5) Validation en temps réel

- **Action** : Implémentez la validation d'email et de téléphone en Python.
- **Piste** : Connectez `textChanged` à des fonctions de validation avec feedback visuel.
- **Validation** : Champs colorés en rouge/vert selon la validité en temps réel.

## 6) Validation croisée

- **Action** : Ajoutez une validation qui vérifie la cohérence entre plusieurs champs.
- **Indice** : Prénom + Nom ne peuvent être vides si "Contact professionnel" est coché.
- **Validation** : Logique de validation complexe avec messages d'erreur appropriés.

## 7) Gestion du bouton OK

- **Action** : Le bouton OK ne doit être activé que si le formulaire est valide.
- **Piste** : Fonction qui vérifie tous les champs et met à jour `setEnabled()` du bouton.
- **Validation** : Bouton OK activé/désactivé selon l'état de validation global.

## 8) Messages de statut

- **Action** : Ajoutez un `QLabel` de statut qui affiche l'état de validation en temps réel.
- **Indice** : Messages comme "Formulaire valide", "Email invalide", etc.
- **Validation** : Feedback utilisateur permanent sur l'état du formulaire.

---

## Exercices supplémentaires

- **Validation personnalisée** : Créez des validateurs Qt personnalisés pour les champs.
- **Autocomplétion** : Ajoutez l'autocomplétion sur les champs Ville et Pays.
- **Sauvegarde automatique** : Sauvegardez les données pendant la saisie (timer).
- **Raccourcis avancés** : Implémentez des raccourcis clavier pour les actions courantes.
