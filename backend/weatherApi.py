import cgi
import requests
import mapsApi
# response = requests.get("https://api.met.no/weatherapi/locationforecast/1.9/?lat=60.10&lon=9.58&msl=70")
# print(response.json())

data = cgi.FieldStorage()

def init():
    #use this for final:
    #dest = data["form"].value
    dest = 'Northern Blvd, Old Westbury, NY 11568' #change this later!
    lat = mapsApi.getLat_Lng(dest)[0]
    lng = mapsApi.getLat_Lng(dest)[1]
    return lat,lng
 

def currentweather():
    key = open("apiKeyWeather.txt", "r").read()
    #init()
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(init()[0])+"&lon="+str(init()[1])+"&appid="+key
    response = requests.get(url)
    jsonformat = (response.json())

    #list values under here:
    description=(jsonformat['weather'][0]['description'])
    return description




def forecast():
    key= open("apiKeyWeather.txt", "r").read()
    init()
    urlforecast = "http://api.openweathermap.org/data/2.5/forecast?lat="+str(init()[0])+"&lon="+str(init()[1])+"&appid="+key
    response2 = requests.get(urlforecast)
    jsonformat2 = (response2.json())
    #list values under here:
    #population=(jsonformat2['city']['popluation'])
    #cityname=(jsonformat2['city']['name'])
    
    value=0
    currentTotal=0
    templist={}
    while value < 40:
        templist[value]=(jsonformat2['list'][int(value)]['main']['temp'])  
        currentTotal+=float(templist[value])
        value +=1
    avg=float(currentTotal)/39
    celsiusavg=str(float(avg)-273.15)
    fahrenavg=str(float(celsiusavg)+(9/5)+32)

    value=0
    currentTotal=0
    humidlist={}
    while value < 40:
        humidlist[value]=(jsonformat2['list'][int(value)]['main']['humidity'])  
        currentTotal+=float(humidlist[value])
        value +=1
    humidityavg=float(currentTotal)/39
    roundcelsius=round(float(celsiusavg), 1)
    roundfahren=round(float(fahrenavg), 1)
    roundhumidity=round(float(humidityavg), 1)
    return roundcelsius, roundfahren, roundhumidity

def humidcomments(x):
    if x > 80:
        return "Darn, you are in for a tough time! The humidity is so high, Elon Musk is getting jealous."
    elif x < 25:
        return "You better bring a jacket! Somebody's gotta get a humidifier in here."
    elif x > 60 and x <= 80:
        return "You will cook like a lobster - that is, a lobster in a slow-cooker."
    elif x >= 25 and x <=60:
        return "The humidity is tolerable. Just like a A- on that latest math test."
def main():
    init()
    
    humidcomments(forecast()[2])
main()



