import requests

API_ENDPOINT = "https://www.wikidata.org/w/api.php"

query = 'South Africa'

params = {
    'action' : 'wbsearchentities',
    'format' : 'json',
    'language' : 'en',
    'search' : query
}

r = requests.get(API_ENDPOINT, params = params)

print(r.json()['search'][0]['description'])