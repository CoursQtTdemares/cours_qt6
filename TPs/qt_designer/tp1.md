# TP1 - Interface de base avec Designer

**Durée** : 30 minutes

**Objectif** : Créer une interface de gestion de contacts avec Designer en configurant les propriétés et layouts appropriés.

**Pré-requis** : Chapitres 1-5 maîtrisés, Qt Designer installé.

## 1) Installation et vérification de Designer

- **Action** : Vérifiez que Qt Designer est accessible depuis votre environnement.
- **Piste** : Commande `designer` dans le terminal ou cherchez "Qt Designer" dans le menu applications.
- **Validation** : Qt Designer s'ouvre avec une interface de création de formulaires.

## 2) Création du formulaire de contact

- **Action** : Créez un nouveau "Dialog" et configurez les propriétés de base.
- **Indice** : Taille 400x300, titre "Gestion de Contacts", nom d'objet `ContactDialog`.
- **Validation** : Formulaire de base avec propriétés correctement définies.

## 3) Section informations personnelles

- **Action** : Ajoutez les champs : Prénom, Nom, Email, Téléphone avec leurs labels.
- **Piste** : Utilisez `QLabel` et `QLineEdit`, organisez avec `QFormLayout`.
- **Validation** : Quatre lignes de saisie bien alignées avec labels explicites.

## 4) Section adresse

- **Action** : Créez un `QGroupBox` "Adresse" avec Rue, Ville, Code postal, Pays.
- **Indice** : Le pays doit être une `QComboBox` avec quelques pays prédéfinis.
- **Validation** : Groupe visuellement distinct avec champs d'adresse organisés.

## 5) Contrôles et boutons d'action

- **Action** : Ajoutez une `QCheckBox` "Contact professionnel" et boutons OK/Annuler.
- **Piste** : Boutons alignés à droite, avec tailles cohérentes.
- **Validation** : Interface complète avec tous les contrôles nécessaires.

## 6) Configuration des propriétés avancées

- **Action** : Configurez les placeholders, tailles min/max, et tooltips pour tous les champs.
- **Indice** : Email avec placeholder "nom@exemple.com", téléphone avec masque de saisie.
- **Validation** : Champs avec aide contextuelle et contraintes appropriées.

## 7) Layouts et redimensionnement

- **Action** : Appliquez les layouts appropriés pour un redimensionnement correct.
- **Piste** : Layout principal vertical, sous-layouts selon les besoins.
- **Validation** : Interface qui s'adapte proprement au redimensionnement.

## 8) Sauvegarde et test initial

- **Action** : Sauvegardez en `contact_form.ui` et testez l'aperçu dans Designer.
- **Validation** : Fichier .ui créé et aperçu fonctionnel dans Designer.

---

## Exercices supplémentaires

- **Validation visuelle** : Ajoutez des styles CSS pour les champs obligatoires.
- **Accessibilité** : Configurez les raccourcis clavier et l'ordre de tabulation.
- **Icônes** : Ajoutez des icônes aux boutons en utilisant les ressources Qt.
- **Template** : Créez un template réutilisable pour d'autres formulaires similaires.