# TP2 - Graphiques personnalisés avec les données

**Durée** : 30 minutes

**Objectif** : Utiliser QPainter pour tracer un graphique simple avec 3 points de température et 2 segments.

**Pré-requis** : TP1 terminé et fonctionnel.

## 1) Créer la classe ChartWidget

- **Action** : Créez `ChartWidget` héritant de `QWidget` avec 3 températures fixes en données d'exemple.
- **Piste** : `self.temperatures = [20, 25, 22]` et `self.cities = ["Paris", "Lyon", "Marseille"]`.
- **Validation** : Widget personnalisé avec données d'exemple.

## 2) Méthode paintEvent de base

- **Action** : Implémentez `paintEvent()` qui dessine un fond bleu clair avec QPainter.
- **Piste** : `painter = QPainter(self)`, `painter.fillRect(self.rect(), QColor(240, 248, 255))`.
- **Validation** : Widget avec fond coloré.

## 3) Calcul des 3 points

- **Action** : Convertissez les 3 températures en coordonnées écran avec des positions fixes simples.
- **Piste** : Point 1 à (100, y1), Point 2 à (200, y2), Point 3 à (300, y3) où y dépend de la température.
- **Validation** : 3 QPointF calculés correctement.

## 4) Dessin des 2 segments

- **Action** : Tracez 2 lignes reliant Point1→Point2 et Point2→Point3.
- **Piste** : `painter.setPen(QPen(QColor(255, 0, 0), 3))`, `painter.drawLine(point1, point2)`.
- **Validation** : 2 segments rouges visibles entre les 3 points.

## 5) Dessin des 3 points

- **Action** : Dessinez 3 cercles bleus sur les positions des températures.
- **Piste** : `painter.setPen(QPen(QColor(0, 0, 255), 2))`, `painter.drawEllipse(point, 8, 8)`.
- **Validation** : 3 points bleus visibles aux intersections.

## 6) Intégration dans l'application du TP1

- **Action** : Ajoutez le ChartWidget à l'application du TP1 et mettez à jour les données reçues.
- **Piste** : Layout vertical avec bouton, texte et graphique. Méthode `update_chart(temperatures)`.
- **Validation** : Application complète avec téléchargements et graphique qui se met à jour.

---

## Exercices supplémentaires

- **Étiquettes** : Affichez les noms des villes sous chaque point.
- **Couleurs** : Utilisez des couleurs différentes selon la température.
- **Animation** : Animez l'apparition des points lors de la réception des données.