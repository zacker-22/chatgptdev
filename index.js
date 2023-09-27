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
    res.render( 'index', {
        query: "query",

    });
    
})



server.listen(port, () => {
    console.log('HTTPS is running on port ' + port + '')
});