# ES6 Classes

Ce projet explore les concepts des classes ES6 en JavaScript. Il contient plusieurs implémentations de classes démontrant différentes fonctionnalités d'ES6.

## Description des fichiers

* `0-classroom.js` : Implémente une classe `ClassRoom` avec un attribut `_maxStudentsSize`.

* `1-make_classrooms.js` : Utilise la classe `ClassRoom` pour créer un tableau de 3 `ClassRoom`.

* `2-hbtn_course.js` : Implémente une classe `HolbertonCourse` avec validation des attributs.

* `3-currency.js` : Implémente une classe `Currency` avec des getters et setters.

* `4-pricing.js` : Implémente une classe `Pricing` qui utilise la classe `Currency`.

* `5-building.js` : Implémente une classe abstraite `Building`.

* `6-sky_high.js` : Implémente une classe `SkyHighBuilding` qui hérite de `Building`.

* `7-airport.js` : Implémente une classe `Airport` avec une méthode toString() personnalisée.

* `8-hbtn_class.js` : Implémente une classe `HolbertonClass` avec des méthodes de conversion.

* `9-hoisting.js` : Démontre le concept de hoisting avec des classes ES6.

* `10-car.js` : Implémente une classe `Car` avec une méthode de clonage.

## Configuration

Le projet utilise les outils suivants :
- Babel pour la transpilation ES6
- ESLint pour le linting avec la configuration Airbnb-base
- Jest pour les tests

## Installation

```bash
npm install
```

## Scripts disponibles

```bash
# Lancer ESLint
npm run lint

# Vérifier le linting
npm run check-lint

# Mode développement avec Babel
npm run dev

# Lancer les tests
npm run test

# Lancer le linting et les tests
npm run full-test
```

## Règles ESLint

Le projet utilise une configuration ESLint personnalisée avec les règles suivantes :
- Support des underscores dans les noms de variables
- Extensions de fichiers obligatoires dans les imports
- Plusieurs classes autorisées par fichier
- Arguments non utilisés autorisés dans les fonctions 