const express = require('express');
const router = express.Router();
const path = require('path');

var AWS = require("aws-sdk");
let awsConfig = {
    "region": "YOUR REGION HERE",
    "endpoint": "http://dynamodb.YOUR REGION HERE.amazonaws.com",
    "accessKeyId": "YOUR ACCESSKEYID HERE", "secretAccessKey": "YOUR SECRECT ACCESS KEY HERE"
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();

//const Analysis = require('../models/Analysis');

//ROUTES
//you can use get (shoots message), post (give to list), delete (removes post), patch (updates post)

//GET BACK ALL THE POSTS                

router.get('/', async (req,res) => {

    try{
        const analyze = await Analysis.find();
        res.json(analyze);
    }catch(err) {
        res.json({ message: err});
    }
    //res.sendFile(path.join(__dirname + '../../views/analyze.html'));
});



//SUBMITS A POST
router.post('/', async (req,res) => {

    var saveFlag = true;
    var computeFlag = true;

    //Flags to force save and compute
    if (req.query.save == 'true'){
        var saveFlag = true;
    }
    else if (req.query.save == 'false'){
        var saveFlag = false;
    }
    if (req.query.compute == 'true'){
        var computeFlag = true;
    }
    else if (req.query.compute == 'false'){
        var computeFlag = false;
    }

    //console.log("inital flags are: compute = " + computeFlag + " save = "+ saveFlag);

    if (saveFlag == true){
        computeFlag = true;
    }

    //console.log("fixed flags are: compute = " + computeFlag + " save = "+ saveFlag);

    try{

    var input = req.body.input;

    var params = {
        TableName: "concordance",
        Key: req.body
    };

    //Get the item with the matching key (input)
    docClient.get(params, function (err, data) {
        if (err) {
            console.log("users::fetchOneByKey::error - " + JSON.stringify(err, null, 2));
        }
        else {
            //If the JSON is empty
            if(JSON.stringify(data, null, 2)=="{}") {

                //Calculate the concordance
                if(computeFlag == true){
                    console.log("computing");
                    var output = calculate(input);
                }

                res.json(output);

                var input2 = {
                  "input": input, "concordance": output
                };

                var params2 = {
                    TableName: "concordance",
                    Item:  input2,
                    Key: req.body
                };

                //save to DB
                if(saveFlag == true){
                    console.log("saving");
                    console.log("INSERTING ITEM");
                    save(data, params2);
                }
            }
            //If it returns a JSON, dont add anything to the DB
            else{
                console.log("NOT INSERTING ITEM");
                res.json(data.Item.concordance);
            }
        }
    })
    

    }catch(err) {
        res.json({message: err});
    }
});

/*
* Calculate function
*/
let calculate = function (input) {
    var concordance = getConcordance(input);
    var output = {concordance:concordance, input:input};
    return output;
}

/*
* Save Function
*/
let save = function (data, params) {
    //Add the item to the DB
    docClient.put(params, function (err, data) {
        if (err) {
            console.log("users::save::error - " + JSON.stringify(err, null, 2));                      
        } else {
            console.log("users::save::success" );                      
        }
    });
}


/*
//SPECIFIC POST
router.get('/:postId', async (req,res) => {
    try{
        const post = await Post.findById(req.params.postId);
        res.json(post);
    }catch(err) {
        res.json({message: err});
    }
});

//DELETE POST
router.delete('/:postId', async (req,res) => {
    try{
        const removedPost = await Post.remove({_id: req.params.postId});
        res.json(removedPost);
    }catch(err) {
        res.json({message: err});
    }
});

//UPDATE POST
router.patch('/:postId', async (req,res) => {
    try{
        const updatedPost = await Post.updateOne(
            {_id: req.params.postId},
            {$set: {title:req.body.title}
        });
        res.json(updatedPost);
    }catch(err) {
        res.json({message: err});
    }
});
*/

//punctuation I want to remove
var regex = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g;

//removes punctuation
function removePunctuation(string) {
    return string.replace(regex, "");
}

//Get concordance
function getConcordance(input){
    var low = input.toLowerCase();
    var punc = removePunctuation(low);
    var space = punc.replace(/\s\s+/g, ' ');
    var words = space.split(" ");
    var sorted = words.sort();

    obj = {};

    for(var i = 0; i < sorted.length; ++i) {
        if(!obj[sorted[i]])
            obj[sorted[i]] = 0;
        ++obj[sorted[i]];
    }

    var tokens = Object.keys(obj);
    var counts = Object.values(obj);

    var concordance = [];

    for (var i = 0; i < tokens.length; i++) {
        concordance.push({
            token: tokens[i],
            count: counts[i]
        });
    }

    return concordance;
}

module.exports = router;