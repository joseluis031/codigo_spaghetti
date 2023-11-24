const express = require('express');
const bodyParser = require('body-parser');
const Airtable = require('airtable');

const app = express();
app.use(bodyParser.json());

const base = new Airtable({apiKey: 'YOUR_API_KEY'}).base('YOUR_BASE_ID');

app.post('/saveResult', (req, res) => {
    const { operation, result } = req.body;

    base('Table Name').create([
        {
            "fields": {
                "Operation": operation,
                "Result": result
            }
        }
    ], function(err, records) {
        if (err) {
            console.error(err);
            res.status(500).send(err);
            return;
        }
        res.status(200).send(records);
    });
});

app.listen(3000, () => console.log('Server running on port 3000'));