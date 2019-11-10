import requests

apiKey = open("apiKey.txt", "r").read()

def getLat_Lng(Address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        pythonConvert = response.json()
        lat = pythonConvert['results'][0]['geometry']['location']['lat']
        lng = pythonConvert['results'][0]['geometry']['location']['lng']
    except:
        lat = 0
        lng = 0
    return lat, lng


