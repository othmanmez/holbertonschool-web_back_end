const express = require('express');
const { readFile } = require('fs').promises;

const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    try {
        const database = process.argv[2];
        const data = await readFile(database, 'utf8');
        const lines = data.trim().split('\n');
        const students = lines.slice(1).filter(line => line.length > 0);
        
        let response = 'This is the list of our students\n';
        response += `Number of students: ${students.length}\n`;
        
        const fields = {};
        students.forEach(student => {
            const [firstname, , , field] = student.split(',');
            if (!fields[field]) {
                fields[field] = { count: 0, students: [] };
            }
            fields[field].count += 1;
            fields[field].students.push(firstname);
        });
        
        for (const [field, data] of Object.entries(fields)) {
            response += `Number of students in ${field}: ${data.count}. List: ${data.students.join(', ')}\n`;
        }
        
        res.send(response.trim());
    } catch (error) {
        res.send('Cannot load the database');
    }
});

app.listen(1245);

module.exports = app; 