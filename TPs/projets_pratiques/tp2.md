# TP2 - Tests et debugging complets

**Durée** : 45 minutes  

**Objectif** : Écrire une suite de tests complète pour l'application et implémenter les outils de debugging et monitoring.

**Pré-requis** : TP1 terminé avec application fonctionnelle.

## 1) Configuration de l'environnement de test

- **Action** : Configurez `pytest` avec les plugins nécessaires pour PyQt6.
- **Piste** : `pytest-qt`, `pytest-mock`, `pytest-cov` pour la couverture de code.
- **Validation** : Environnement de test fonctionnel avec exécution des premiers tests.

## 2) Tests unitaires des modèles

- **Action** : Écrivez des tests complets pour la classe `Contact` et les validations.
- **Indice** : Testez création, validation, sérialisation, cas d'erreur avec `@pytest.mark.parametrize`.
- **Validation** : Couverture de test >90% pour les modèles avec cas limites.

## 3) Tests d'intégration de la base de données

- **Action** : Testez toutes les opérations CRUD avec base de données temporaire.
- **Piste** : Fixtures pytest pour DB en mémoire, rollback automatique des transactions.
- **Validation** : Tests robustes des opérations de persistance avec isolation.

## 4) Tests de l'interface utilisateur

- **Action** : Utilisez `pytest-qt` pour tester les interactions de l'interface.
- **Indice** : `QTest.mouseClick()`, `QTest.keyClicks()`, vérification des signaux émis.
- **Validation** : Tests automatisés des parcours utilisateur principaux.

## 5) Mocking et tests d'isolation

- **Action** : Utilisez `pytest-mock` pour isoler les composants pendant les tests.
- **Piste** : Mock des appels de base de données, fichiers, services externes.
- **Validation** : Tests rapides et fiables isolant chaque composant.

## 6) Outils de debugging intégrés

- **Action** : Implémentez un système de debugging avec logs détaillés et monitoring.
- **Indice** : Niveaux de log configurables, profiling des requêtes, métriques de performance.
- **Validation** : Système de debugging aidant au développement et dépannage.

## 7) Tests de performance et stress

- **Action** : Créez des tests de charge avec beaucoup de contacts et opérations simultanées.
- **Piste** : Génération de données de test, mesure des temps de réponse, tests de mémoire.
- **Validation** : Application validée pour gérer de gros volumes de données.

## 8) Pipeline de CI/CD local

- **Action** : Configurez un script de validation automatique (tests + linting + couverture).
- **Indice** : Script bash/Python exécutant tous les contrôles avant commit.
- **Validation** : Process de validation automatique garantissant la qualité.

---

## Métriques attendues

- **Couverture de code** : >85% sur l'ensemble du projet
- **Tests passants** : 100% de réussite de la suite de tests
- **Performance** : <500ms pour 10000 contacts en recherche
- **Qualité** : Score de linting >8/10 avec outils standards
