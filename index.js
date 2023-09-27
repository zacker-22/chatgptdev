const http = require('http');
const express = require('express');
const path = require('path');

const port = 8080
app = express();

app.set("view engine", "ejs");

const server = http.createServer(app);

app.use(express.json());
app.use(express.static(path.join(__dirname, 'static')));


app.get('/', (req, res) => {

    const query = req.query.query;
    let url = "http://127.0.0.1:5000/api?query=" + query;
    http.get(url, function (response) {
        response.setEncoding('utf8');
        response.on('data', function (data) {
            console.log(data);
            res.render('index', {result : JSON.parse(data)['result'], query : query });
        });
    });
   

    
})


server.listen(port, () => {
    console.log('HTTPS is running on port ' + port + '')
});