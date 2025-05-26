# Node.js Basics

Ce projet est une introduction aux concepts de base de Node.js, comprenant :
- L'utilisation de Node.js avec JavaScript
- Les opérations d'entrée/sortie (stdin, stdout)
- La lecture de fichiers (synchrone et asynchrone)
- La création de serveurs HTTP avec Node.js natif et Express
- L'utilisation d'ES6 avec Babel-node

## Installation

```bash
# Installer les dépendances
npm install

# Pour le serveur complet (full_server), installer également
npm install --save-dev babel-preset-env
```

## Structure du Projet

- `0-console.js` : Affichage simple dans la console
- `1-stdin.js` : Interaction avec l'utilisateur via stdin/stdout
- `2-read_file.js` : Lecture synchrone d'un fichier CSV
- `3-read_file_async.js` : Lecture asynchrone d'un fichier CSV
- `4-http.js` : Serveur HTTP simple
- `5-http.js` : Serveur HTTP avec routes
- `6-http_express.js` : Serveur Express simple
- `7-http_express.js` : Serveur Express avec routes
- `full_server/` : Application Express complète avec architecture MVC
  - `utils.js` : Utilitaires pour la lecture de la base de données
  - `controllers/` : Contrôleurs de l'application
  - `routes/` : Routes de l'application
  - `server.js` : Point d'entrée du serveur

## Utilisation

### Scripts Simples
```bash
# Exécuter le script console
node 0-console.js

# Exécuter le script stdin
node 1-stdin.js

# Exécuter les scripts de lecture de fichiers
node 2-read_file.js database.csv
node 3-read_file_async.js database.csv

# Démarrer les serveurs HTTP
node 4-http.js
node 5-http.js database.csv
node 6-http_express.js
node 7-http_express.js database.csv
```

### Serveur Complet (full_server)
```bash
# Démarrer le serveur avec babel-node
npm run dev
```

## Format du Fichier Database

Le fichier CSV doit avoir le format suivant :
```csv
firstname,lastname,age,field
Johann,Kerbrou,30,CS
```

## Routes Disponibles

- `GET /` : Page d'accueil
- `GET /students` : Liste de tous les étudiants
- `GET /students/:major` : Liste des étudiants par spécialité (CS ou SWE)

## Tests

Pour exécuter les tests :
```bash
npm test
``` 