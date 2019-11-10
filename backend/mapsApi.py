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

def getPlaceID(address):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        pythonConvert = response.json()
        placeID = pythonConvert['results'][0]["place_id"]
    except:
        placeID = ""
    return placeID


address = "55 church Ave, brooklyn"
print(getPlaceID(address))

def formal(lat, lng):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'.format(lat, lng, apiKey))
    try:
        response = requests.get(url)
        pythonConvert = response.json()
        address = pythonConvert['results'][1]["formatted_address"]
    except:
        address = ""
    return address
