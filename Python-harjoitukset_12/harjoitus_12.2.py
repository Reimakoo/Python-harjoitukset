import requests
import json

city = input("Syötä kaupunki minkä säätilan haluat tietää!: ")
country = input("Syötä maan kaksikirjaiminen tunnus (esim: Suomi = FI) : ")
lat_lon = "http://api.openweathermap.org/geo/1.0/direct?q={" + city +"},{" + country +"}&limit={1}&appid={13cb57640ffdd78a2b0925984351297d}"
cordinates = requests.get(lat_lon).json()
json_cordinates = cordinates
print(json.dumps(json_cordinates))



