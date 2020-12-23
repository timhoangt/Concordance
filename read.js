var AWS = require("aws-sdk");
let awsConfig = {
    "region": "YOUR REGION HERE",
    "endpoint": "http://dynamodb.YOUR REGION HERE.amazonaws.com",
    "accessKeyId": "YOUR ACCESSKEYID HERE", "secretAccessKey": "YOUR SECRECT ACCESS KEY HERE"
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();
let fetchOneByKey = function () {
    var params = {
        TableName: "concordance",
        Key: {
            "input": "Woet wet."
        }
    };
    docClient.get(params, function (err, data) {
        if (err) {
            console.log("users::fetchOneByKey::error - " + JSON.stringify(err, null, 2));
        }
        else {
            console.log("users::fetchOneByKey::success - " + JSON.stringify(data, null, 2));
        }
    })
}


fetchOneByKey();