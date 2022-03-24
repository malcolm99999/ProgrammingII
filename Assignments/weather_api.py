import requests
import json
from pprint import pprint
latitude = input("What Latitude would you like to put in: ")
longitude = input("What's the longitude: ")
data = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=" + latitude + ("&lon=") + longitude + "&units=imperial&appid=84e0e82c767a5c60de4b4edd6bf625ae")
data_dict = json.loads(data.text)
pprint(data_dict)
print("It is: " + str(data_dict.get('main').get('temp')))
print("you chose " + str(data_dict.get('coord')))
print("In " + str(data_dict.get('sys').get('country')))
print("Feels like: " + str(data_dict.get('main').get('feels_like')))
print(data)