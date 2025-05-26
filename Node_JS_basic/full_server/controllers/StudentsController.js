import readDatabase from '../utils';

class StudentsController {
    static async getAllStudents(request, response) {
        try {
            const fields = await readDatabase(process.argv[2]);
            let output = 'This is the list of our students\n';
            
            const sortedFields = Object.keys(fields).sort((a, b) => 
                a.localeCompare(b, undefined, {sensitivity: 'base'}));
            
            for (const field of sortedFields) {
                output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
            }
            
            response.status(200).send(output.trim());
        } catch (error) {
            response.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(request, response) {
        const { major } = request.params;
        
        if (major !== 'CS' && major !== 'SWE') {
            response.status(500).send('Major parameter must be CS or SWE');
            return;
        }
        
        try {
            const fields = await readDatabase(process.argv[2]);
            const students = fields[major] || [];
            response.status(200).send(`List: ${students.join(', ')}`);
        } catch (error) {
            response.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController; 