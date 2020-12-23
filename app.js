const express = require('express');
const app = express();
const path = require('path');
//const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv/config');

//Middlewares (functions that execute when routes are hit)
app.use(cors());
app.use(bodyParser.json());

/*app.use('/posts', () => {
    console.log('This middleware is running');
});*/

//Import Routes
const postsRoute = require('./routes/posts');

app.use('/posts', postsRoute);

//Routes
app.get('/', function(req, res){
    res.sendFile(path.join(__dirname + '/views/analyze.html'));
});

const analyzeRoute = require('./routes/analyze');

app.use('/analyze', analyzeRoute);

const locateRoute = require('./routes/locate');

app.use('/locate', locateRoute);

//listen to server
app.listen(8080);