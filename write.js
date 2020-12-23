var AWS = require("aws-sdk");
let awsConfig = {
    "region": "YOUR REGION HERE",
    "endpoint": "http://dynamodb.YOUR REGION HERE.amazonaws.com",
    "accessKeyId": "YOUR ACCESSKEYID HERE", "secretAccessKey": "YOUR SECRECT ACCESS KEY HERE"
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();

let save = function () {

    var input = {
        "input": "example-1@gmail.com", "created_by": "clientUser", "created_on": new Date().toString(),
        "updated_by": "clientUser", "updated_on": new Date().toString(), "is_deleted": false
    };
    var params = {
        TableName: "concordance",
        Item:  input
    };
    docClient.put(params, function (err, data) {

        if (err) {
            console.log("users::save::error - " + JSON.stringify(err, null, 2));                      
        } else {
            console.log("users::save::success" );                      
        }
    });
}

save();