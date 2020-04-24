import numpy
import pandas as pd
import requests
import json


url = 'https://api.smartable.ai/coronavirus/stats/' + country_name
params = {
    'Cache-Control': 'no-cache',
    'Subscription-Key': 'a5853f4359674b35b373ade277d73e24',
}

r = requests.get(url=url, params=params)
r = r.text
jsonData = json.loads(r)
print(jsonData)


jsonData = json.loads(data)
x = jsonData.keys()

latestData = jsonData['stats']['breakdowns'][0]

print(latestData['totalConfirmedCases'])

def totalConfirmed():
    totalConfirmedCases = latestData['totalConfirmedCases']
def cuntry():
    country = latestData['countryOrRegion']
def newlyConfirmed():
    newlyConfirmedCases = latestData['newlyConfirmedCases']
def totalDeat():
    totalDeaths = latestData['totalDeaths']
def newDeat():
    newDeaths = latestData['newDeaths']
def totalRecovered():
    totalRecoveredcases = latestData['totalRecoveredCases']
