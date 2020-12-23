import connexion
import six

from swagger_server.models.result import Result  # noqa: E501
from swagger_server import util
from swagger_server.db.azureDB import AzureDB

import re
import hashlib
from collections import Counter


def get_concordance(body=None, calculate=False, store=True):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes
    :param force: Force input to be analyzed even if it's been analyzed already
    :type force: bool

    :rtype: Result
    """

    result = {}
    if connexion.request.is_json:
        # jsonBody = connexion.request.get_json()
        # body = str.from_dict(connexion.request.get_json())  # noqa: E501
        result = {
            "title": "Bad POST Request",
            "Message": "Request doesn't accept json data structure.. Try text/plain data type",
        }
    else:
        concordance = []
        body = body.decode("utf-8")

        newBody = cleanup(body)
        listOfWords = newBody.split()  # split words in new body into a list

        concordanceDict = Counter(listOfWords)  # get concordance using Counter method
        sortedWords = sorted(concordanceDict.keys())  # sort unique words found

        hashData = "".join(sortedWords).encode("utf-8")  # join set of words into one giant word
        hashObject = hashlib.sha256(hashData)
        hashString = hashObject.hexdigest()

        # in case app can't connect to database server
        try:
            db = AzureDB("concordance")
            dbAvailable = True
            # check if input has already been analyzed and stored in database
            inputExists, dbConcordance = db.inputExists(hashString)
        except:
            #
            db = None
            dbAvailable = False
            inputExists = False
            dbConcordance = []

        if inputExists == False or calculate == True:

            # listOfWords = newBody.split()  #split words in new body into a list
            # setOfWords = sorted(set(listOfWords))  #generate unique set of words and sort in asc. order

            # create concordance dictionary
            for word in sortedWords:
                concordance.append({"token": word, "count": concordanceDict[word]})

            result = {"concordance": concordance, "input": body}

            if dbAvailable and inputExists == False and store == True:
                # insert concordance only if input have never been analyzed and store flag is set.. if database is available
                if db:
                    db.insert(hashString, concordance)  # insert into database
        else:
            result = {"concordance": dbConcordance, "input": body}

    return result


def get_locations(body=None, calculate=False, store=True):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes
    :param force: Force input to be analyzed even if it's been analyzed already
    :type force: bool

    :rtype: Result
    """

    result = {}
    if connexion.request.is_json:
        # jsonBody = connexion.request.get_json()
        # body = str.from_dict(connexion.request.get_json())  # noqa: E501
        result = {
            "title": "Bad POST Request",
            "Message": "Request doesn't accept json data structure.. Try text/plain data type",
        }
    else:
        concordance = []
        body = body.decode("utf-8")

        newBody = cleanup(body)

        listOfWords = newBody.split()  # split words in new body into a list
        sortedWords = sorted(set(listOfWords))  # generate unique set of words and sort in asc. order

        hashData = "".join(sortedWords).encode("utf-8")  # join set of words into one giant word
        hashObject = hashlib.sha256(hashData)
        hashString = hashObject.hexdigest()

        # in case app can't connect to database server
        try:
            db = AzureDB("locations")
            dbAvailable = True
            # check if input has already been analyzed and stored in database
            inputExists, dbConcordance = db.inputExists(hashString)
        except:
            #
            db = None
            dbAvailable = False
            inputExists = False
            dbConcordance = []

        if inputExists == False or calculate == True:

            concordanceDict = {}  # concordance dictionary with word as key and list of index as values
            for index in range(len(listOfWords)):
                try:
                    # generic lookup to see if key already exists.. append to list if it does
                    concordanceDict[listOfWords[index]] = concordanceDict[listOfWords[index]] + [index]
                except:
                    # new word.. initialize index
                    concordanceDict[listOfWords[index]] = [index]

            # generate location concordance
            for word in sortedWords:
                locations = concordanceDict[word]
                concordance.append({"token": word, "locations": locations})

            result = {"concordance": concordance, "input": body}

            if dbAvailable and inputExists == False and store == True:
                # insert concordance only if input have never been analyzed and store flag is set.. and if database is available
                if db:
                    db.insert(hashString, concordance)  # insert into database
        else:
            result = {"concordance": dbConcordance, "input": body}

    return result


def cleanup(body):
    """clean up POST body"""
    newBody = body.lower()
    newBody = re.sub(r"[^\w\d'\s\-]+", " ", newBody)  # remove all punctuations.. except hyphens and apostrophes for now
    newBody = re.sub(r"([-])\1+", " ", newBody)  # remove 2 or more hyphens.. eg 'all-knowing' is a word(1 token)
    #                                                                              but 'all--knowing' will be broken into 2 tokens
    newBody = re.sub(r"('s)|(')", " ", newBody)  # remove apostrphes.. eg brother's will be stored as brother

    newBody = newBody.strip()  # removing leading/trailing spaces
    return newBody
