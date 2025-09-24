# TP2 - Graphiques météo personnalisés

**Durée** : 30 minutes

**Objectif** : Découvrir QPainter pour créer un graphique de températures simple.

**Pré-requis** : TP1 terminé et fonctionnel.

## 1) Classe WeatherChartWidget

- **Action** : Créez `WeatherChartWidget` héritant de `QWidget` avec données de températures.
- **Piste** : `self.temperatures = [15, 18, 22, 20, 17]` et `self.hours = ["8h", "10h", "12h", "14h", "16h"]`.
- **Validation** : Widget personnalisé avec données d'exemple.

## 2) Méthode paintEvent basique

- **Action** : Implémentez `paintEvent()` qui dessine un fond coloré avec QPainter.
- **Piste** : `painter = QPainter(self)`, `painter.fillRect(self.rect(), QColor(240, 248, 255))`.
- **Validation** : Widget avec fond bleu clair.

## 3) Calcul des points de la courbe

- **Action** : Convertissez les températures en coordonnées écran dans une liste de points.
- **Piste** : Boucle sur temperatures, calculez x et y avec des formules simples.
- **Validation** : Liste de QPointF calculée correctement.

## 4) Dessin de la courbe

- **Action** : Tracez des lignes entre les points et dessinez des cercles sur chaque point.
- **Piste** : `painter.drawLine(points[i], points[i+1])` et `painter.drawEllipse(point, 6, 6)`.
- **Validation** : Courbe de température visible avec points marqués.

## 5) Ajout des étiquettes

- **Action** : Affichez les heures sous le graphique avec `drawText()`.
- **Piste** : Boucle sur hours, `painter.drawText(x, y+20, hour)`.
- **Validation** : Heures affichées sous chaque point.

## 6) Intégration dans MDI

- **Action** : Remplacez le contenu de la sous-fenêtre "Graphiques" par votre widget.
- **Piste** : Dans `create_chart_view()`, utilisez `WeatherChartWidget()` au lieu de QLabel.
- **Validation** : Graphique météo affiché dans l'application MDI.

---

## Exercices supplémentaires

- **Couleurs** : Utilisez des couleurs différentes selon la température.
- **Grille** : Ajoutez une grille de fond au graphique.
- **Titre** : Ajoutez un titre "Températures du jour" en haut.