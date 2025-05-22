# 📘 Node.js Basics

## 🎯 Objectifs pédagogiques

À l'issue de ce projet, vous serez capable d'expliquer et de mettre en œuvre sans l'aide de Google :

- L'exécution de JavaScript à l’aide de Node.js
- L’utilisation des modules Node.js
- La lecture de fichiers (de manière synchrone et asynchrone) via des modules spécifiques de Node.js
- L’utilisation de `process` pour lire les arguments de ligne de commande et accéder à l’environnement
- La création de serveurs HTTP avec Node.js et Express.js
- La définition de routes simples et avancées avec Express.js
- L’utilisation d’ES6 avec Babel
- L’utilisation de Nodemon pour un développement plus rapide

---

## 🛠️ Configuration requise

- Éditeurs autorisés : `vi`, `vim`, `emacs`, `Visual Studio Code`
- Le projet est conçu pour Ubuntu 20.04 LTS
- Node.js version `20.x.x`
- Les fichiers doivent se terminer par une nouvelle ligne
- Les fichiers doivent porter l’extension `.js`
- Tous les tests doivent être passés avec `npm run test` ou `npm run full-test`
- Le linting est effectué avec ESLint (standard Airbnb + plugin Jest)
- Export des fonctions/classes via `module.exports = myFunction;`
- Fichiers obligatoires à soumettre :
  - `package.json`
  - `babel.config.js`
  - `.eslintrc.js`
  - `database.csv`

---

## 🧾 Contenu du projet

| Fichier                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `0-console.js`                | Affiche un message dans la console                                          |
| `1-stdin.js`                  | Lit une entrée utilisateur depuis la console                               |
| `2-read_file.js`             | Lit un fichier de manière synchrone et affiche des statistiques            |
| `3-read_file_async.js`       | Lit un fichier de manière asynchrone avec Promesse                         |
| `4-http.js`                  | Crée un serveur HTTP simple avec le module `http`                          |
| `5-http.js`                  | Serveur HTTP affichant le contenu du fichier CSV selon l'URL               |
| `6-http_express.js`          | Serveur HTTP de base avec Express                                          |
| `7-http_express.js`          | Serveur Express avancé avec routes conditionnelles                         |
| `full_server/`               | Serveur modulaire complet (avec MVC)                                       |

---

## 📂 Arborescence


