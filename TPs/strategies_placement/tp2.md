# TP2 - Interface en grille avancée

**Durée** : 30 minutes  

**Objectif** : Concevoir une calculatrice fonctionnelle avec `QGridLayout`, en gérant les widgets multi-cellules et l'espacement.

**Pré-requis** : TP1 terminé et concepts des layouts de base acquis.

## 1) Projet calculatrice

- **Action** : Créez un nouveau projet `tp_calculatrice` et initialisez la structure.
- **Validation** : Projet `uv` fonctionnel avec PyQt6 installé.

## 2) Fenêtre et affichage

- **Action** : Créez une classe `Calculator` avec un `QLineEdit` en haut pour l'affichage.
- **Piste** : L'affichage doit être en lecture seule et aligné à droite.
- **Validation** : Une zone d'affichage style calculatrice apparaît en haut.

## 3) Grille des boutons principaux

- **Action** : Ajoutez les boutons numériques (0-9) dans une grille 4x3.
- **Indice** : Utilisez `QGridLayout` avec `addWidget(bouton, ligne, colonne)`.
- **Validation** : Les chiffres 1-9 forment un pavé numérique classique.

## 4) Bouton zéro étendu

- **Action** : Faites en sorte que le bouton "0" occupe deux colonnes en bas.
- **Piste** : Cherchez la surcharge de `addWidget()` avec `row_span` et `col_span`.
- **Validation** : Le bouton "0" est plus large que les autres.

## 5) Colonne des opérateurs

- **Action** : Ajoutez une colonne de droite avec +, -, ×, ÷, =.
- **Indice** : Utilisez une couleur de fond différente pour distinguer les opérateurs.
- **Validation** : Les opérateurs sont visuellement distincts des chiffres.

## 6) Ligne de fonctions

- **Action** : Ajoutez en haut les boutons C (clear), ±, %, avec des couleurs spéciales.
- **Piste** : Recherchez `setStyleSheet()` pour modifier l'apparence des boutons.
- **Validation** : Une ligne de fonctions spéciales apparaît au-dessus des chiffres.

## 7) Logique de base

- **Action** : Implémentez la saisie des chiffres et l'affichage dans la zone de résultat.
- **Indice** : Connectez tous les boutons chiffres au même slot avec `lambda` ou `sender()`.
- **Validation** : Cliquer sur les chiffres les affiche dans l'écran.

## 8) Fonction Clear

- **Action** : Implémentez le bouton "C" pour remettre à zéro l'affichage.
- **Validation** : Le bouton "C" efface complètement l'affichage.

---

## Exercices supplémentaires

- **Calculs complets** : Implémentez la logique complète des opérations arithmétiques.
- **Gestion d'erreurs** : Affichez "Erreur" en cas de division par zéro.
- **Historique** : Ajoutez une zone d'historique des calculs précédents.
- **Raccourcis clavier** : Permettez la saisie au clavier (piste: `keyPressEvent()`).
