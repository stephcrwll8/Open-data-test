# First step is to import the necessary libraries.
# Ex: import requests
# What libraries do you need to accomplish this task?

import requests

#tell the console that we need to install and talk with the api

pip install ambient_api

#next, to tell it about the classes in the api 

from ambient_api import AmbientAPI

    api = AmbientAPI()

devices = api.get_devices()

    device = devices[0]
    
    #this should get me the accessible devices
    
    print(device.get_data())

# Next up we need to make the API call to retrieve the data

#I have to name the variables somewhere, I'll do it now before I forget and wonder why things don't work later. I'm doing it this way instead of telling the code to fetch the variables from test-secrets simply because it's way easier for me


appKey = "93b8237f9d7f487c8e08d08fbef51400eb4d1073e9d549b9bc2821bdf13c73d2"

apiKey = "783ff6a8d19744f6a05a7e61e7bbf9b21db3b39f44e74146b338bde4b2a15aa2"

macAddress = "C0:21:0D:1F:04:EC"

urlBase = "https://api.ambientweather.net/v1/devices/"

#when thinking about the concatenation of the url: on a practical note, it makes sense to name your keys as variables because when a user is responsible for typing strings like those over and over there are going to be typos. Better to do it once and call it a variable that you can remember and use throughout your session or that you can then put into a larger variable (below) that makes things much less confusing to look at. Because my request_url variable is formatted the way it is, I can clearly see that both necessary keys are included in my request as well as my mac address. It also helps me more clearly see the syntax of the url (example: the inclusion of &limit=21, limiting the number of results returned to 21). 
#long story short, naming complicated things as easily human readable items helhps the human follow the development of those things through the code

request_url = "https://api.ambientweather.net/vi/devices/" + str(macAddress) + "?apiKey=" + str(apiKey) + "&applicationKey=" + str(appKey) + "&limit=21"


#I imported requests earlier, so now I'm submitting the get request. The .json at the end should make it so that it's returned in json format

json_data = requests.get request_url.json





# Once we have the data, we need to get it in the format we want
# Think about the end product, we need a CSV file that clearly displays the data to the user

#json_data gives me a dictionary of items, and I can recall them by index term (note: index starts at 0 not 1) and get them out of the json format and into a printable state


temperature_in_f = json_data [1]['tempinf']

#now I want to deal with the if part of temperature so I can put it into my csv later. I want another variable to call on just so I don't get even more confused when it comes time to

#temp_value = temperature_in_f
    #if temp_value < 60:
        #print('Too cold')
    #elif temp_value > 85:
        #print('Too hot')
    #else: 
        #print('Goldilocks')

humidity_percent = json_data [3]['humidityin']

wind_speed_mph = json_data [5]['windspeedmph']

wind_gust_mph = json_data [6]['windgustmph']

daily_rainfall_in = json_data [12]['dailyrainin']

monthly_rainfall_in = json_data [14]['monthlyrainin']

yearly_rainfall_in = json_data [15]['yearlyrainin']

uv = json_data [17]['uv']

date_time = json_data [21]['date']



# Once we have the data where we want it, we need to write the CSV file

import csv

with open('weathercsv.csv', 'w') as new_weather_file:
    
    csvwriter = csv.writer(new_weather_file)
    
        csvwriter.writerow(['Date', str(date_time)])
    
        if temp_value < 60:
            csvwriter.writerow(['Temperature', str(temperature_in_f), 'Farenheit', 'Too cold'])
        elif temp_value > 85:
            csvwriter.writerow(['Temperature', str(temperature_in_f), 'Farenheit', 'Too hot'])
        else: 
            csvwriter.writerow(['Temperature', str(temperature_in_f), 'Farenheit', 'Goldilocks'])
        
        #csvwriter.writerow(['Temperature', str(temperature_in_f), 'Farenheit'])
        
        csvwriter.writerow(['Humidity', str(humidity_percent), '%'])
    
        csvwriter.writerow(['Wind Speed', str(wind_speed_mph), 'Miles per Hour (mph)'])
        
        csvwriter.writerow(['Wind Gust', str(wind_gust_mph), 'Miles per Hour (mph)'])
    
        csvwriter.writerow(['Daily Rainfall', str(daily_rainfall_in), 'Inches (in)'])
    
        csvwriter.writerow(['Monthly Rainfall', str(monthly_rainfall_in), 'Inches (in)'])
        csvwriter.writerow(['Yearly Rainfall', str(yearly_rainfall_in), 'Inches (in)'])
    
        csvwriter.writerow(['UV Index', str(uv)])
        
    for line in csvwriter:
        print (line)
    