var AWS = require("aws-sdk");
let awsConfig = {
    "region": "YOUR REGION HERE",
    "endpoint": "http://dynamodb.YOUR REGION HERE.amazonaws.com",
    "accessKeyId": "YOUR ACCESSKEYID HERE", "secretAccessKey": "YOUR SECRECT ACCESS KEY HERE"
};
AWS.config.update(awsConfig);

let docClient = new AWS.DynamoDB.DocumentClient();

let remove = function () {

    var params = {
        TableName: "concordance",
        Key: {
            "email_id": "example@gmail.com"
        }
    };
    docClient.delete(params, function (err, data) {

        if (err) {
            console.log("users::delete::error - " + JSON.stringify(err, null, 2));
        } else {
            console.log("users::delete::success");
        }
    });
}

remove();