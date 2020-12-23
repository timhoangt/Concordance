import requests
import json

def test_location(data, expected):
    return test_api('locate', data, expected)

def test_analysis(data, expected):
    return test_api('analyze', data, expected)

def test_api(endpoint, data, expected):
    url = 'http://localhost:8081/mscs721/concordance/1.0.0/' + endpoint
    result = requests.post(
        url, data=data
    )

    return result.json() == expected


