import requests

apiKey = open("apiKey.txt", "r").read()

def getLat_Lng(address):
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

def formalAddress(address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace(' ','+'), apiKey))
    try:
        repsone = requests.get(url)
        pythonConvert = response.json()
        formal = pythonConvert['results'][1]
    except:
        formal = ""
    return formal

def reverseSearch(lat, lng):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(lat, lng, apiKey)
    try:
        response = requests.get(url)
        pythonConvert = response.json()
        address = pythonConvert['results'][1]['formatted_address']
    except:
        address = "not working"
    return address
