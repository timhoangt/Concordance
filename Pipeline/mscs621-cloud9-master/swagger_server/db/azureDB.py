#!/usr/bin/env python3

import os
from pymongo import MongoClient


class AzureDB:
    def __init__(self, collectionName):
        self.uri = self.getCert()  # Azure mango DB connection string
        self.client = MongoClient(self.uri, retrywrites=False)
        self.mscs621_DB = self.client["mscs621"]
        self.collectionName = collectionName
        self.collection = self.mscs621_DB[collectionName]

    def getCert(self):
        with open("swagger_server/db/azureDB.cert") as certFile:
            azureUri = certFile.read().strip()

        return azureUri

    def inputExists(self, key):

        result = []
        keyExists = False
        collections = self.mscs621_DB.list_collection_names()
        if self.collectionName in collections:
            query = self.collection.find({key: {"$exists": True}}).limit(1)

            # get key results if it already exists in database
            for item in query:
                result = item[key]
                keyExists = True

        return keyExists, result

    def insert(self, key, value):
        self.collection.insert_one({key: value})
