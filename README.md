REST server to return the specified JSON concordance based on an arbitrary English input text.

A video walkthrough of the pipeline implementation can be viewed here https://youtu.be/Y309eHMMIww

An example of this in action deployed using Elastic Beanstalk can be found at http://concordance.eba-em3dtx2m.us-west-2.elasticbeanstalk.com/

Any text put in the input box will be sent to my database once the button is pressed if it does not already exist before calculating the answer. If the answer already exists in the database, it will not be calculated but instead pulled from a previous calculation. The answer will then be dispalyed on the bottom.

For father testing, you can use postman or swagger to POST an input in JSON format to the /analyze and /locate endpoints and get thier respective answers. Once again it will first check the database tables first before calculating.
 
The POST must be a JSON with the input object.
Example of a valid POST: 
```JSON
{
    "input": "The brown fox jumped over the brown log."
}
```

The response will be the object containing the concordance objects (token/count pairs) and the input text.
Example of the response: 
```JSON
{
    "concordance": [
        {
            "token": "brown",
            "count": 2
        },
        {
            "token": "fox",
            "count": 1
        },
        {
            "token": "jumped",
            "count": 1
        },
        {
            "token": "log",
            "count": 1
        },
        {
            "token": "over",
            "count": 1
        },
        {
            "token": "the",
            "count": 2
        }
    ],
    "input": "The brown fox jumped over the brown log."
}
```

Make sure when connecting to your own DynamoDB that you update all the regions and key in read.js, update.js, write.js, delete.js, analyze.js, and locate.js.

To run in your own environment just do npm start!

To upload to elastic beanstalk just select Node.js as the environment type and upload the code as a zip file!

To run on docker port 49160, run these commands:
```
docker build -t concordance .

docker run -p 49160:8080 -d concordance
```

To run on docker compose run this command:
```
docker-compose up
```
To create a concordance lambda function that sends an email on success, use the code in the folder labeled lambda.

# README FOR THE CONCORDANCE APP WITHIN THE PIPELINE FOLDER
Concordance here is written in python and uses AzureDB instead. It also contains a fully automated jenkinsfile for the pipeline to check the github.

# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Installation
Clone MSCS621-concordance git repository

```
git clone https://github.com/Marist-MSCS/MSCS621-concordance.git
```

## Usage
To run the server, please execute the following from the root directory:

```
1. Run with Flask
pip3 install -r requirements.txt
python3 -m swagger_server

2. Run with uwsgi
pip3 install -r requirements.txt
pip3 install uwsgi

uwsgi --http 127.0.0.1:8080 --manage-script-name --mount /=app:app
OR
uwsgi --http-socket 127.0.0.1:8080 --uid uwsgi --plugins python3 --protocol uwsgi --wsgi app:application
```

and open your browser to here:

```
http://localhost:8080/mscs721/concordance/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/mscs721/concordance/1.0.0/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

## Running with Docker Compose with front end web interface

To run the server on a Docker Compose, please execute the following from the root directory:

```bash
# building docker compose
docker-compose build

# starting up docker compose
docker-compose up
```


## Deploy app to AWS Elastic Beanstalk

Install the AWS Elastic Beanstalk CLI. Follow install process for [Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

Deploy Application

```bash
# clone repository if not cloned already
git clone https://github.com/Marist-MSCS/MSCS621-concordance.git

# create AWS Elastic Beanstalk application
eb init -p python-3.6 <Application Name> --region us-east-2

# create AWS Elastic Beanstalk Environment
eb create <Environment Name>

#change default Elastic Beanstalk WSGI path to app.py
```


## Running tests

Tests for the appliction can be run with the following command
```
#Once the server is up and running
python swagger_server/test/run_tests.py
```
