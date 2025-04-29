# MongoDB Scripts

Ce projet contient une collection de scripts MongoDB pour effectuer des opérations de base sur une base de données.

## Scripts

### 0-list_databases
Liste toutes les bases de données disponibles sur le serveur MongoDB.
```bash
// List all databases
show dbs
```

### 1-use_or_create_database
Utilise ou crée une base de données nommée "my_db".
```bash
// Use or create a database
use my_db
```

### 2-insert
Insère un nouveau document dans la collection "school".
```bash
// Insert a document in the collection school
db.school.insertOne({ name: "Holberton school" })
```

### 3-find
Trouve tous les documents dans la collection "school".
```bash
// List all documents in the collection school
db.school.find()
```

### 4-update
Met à jour un document spécifique dans la collection "school".
```bash
// Update a document in the collection school
db.school.updateOne(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } }
)
```

### 5-delete
Supprime un document spécifique de la collection "school".
```bash
// Delete a document from the collection school
db.school.deleteOne({ name: "Holberton school" })
```

### 6-count
Compte le nombre total de documents dans la collection "school".
```bash
// Count documents in the collection school
db.school.countDocuments()
```

### 7-list_collections
Liste toutes les collections dans la base de données actuelle.
```bash
// List all collections in the database
db.getCollectionNames()
```

### 8-update_many
Met à jour tous les documents qui ne correspondent pas aux critères spécifiés.
```bash
// Update all documents that don't match the criteria
db.users.updateMany(
  { likes: { $ne: "bananas" } },
  { $set: { likes: "bananas" } }
)
```

### 9-delete_many
Supprime tous les documents qui correspondent aux critères spécifiés.
```bash
// Delete all documents that match the criteria
db.users.deleteMany({ likes: "bananas" })
```

## Utilisation

Pour exécuter un script, utilisez la commande suivante :
```bash
cat <nom_du_script> | mongo
```

Par exemple :
```bash
cat 0-list_databases | mongo
```

## Notes

- Assurez-vous que MongoDB est installé et en cours d'exécution sur votre système
- Les scripts peuvent être modifiés selon vos besoins spécifiques
- Les commandes sont exécutées dans le shell MongoDB
- Tous les fichiers se terminent par une nouvelle ligne
- La première ligne de chaque fichier est un commentaire 