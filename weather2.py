import requests
import json

# url = "https://api.openweathermap.org/data/2.5/onecall"

# url = "https://api.openweathermap.org/data/2.5/forecast"


# querystring = {"lat":"13.76455","lon":"100.62296","exclude":"daily","units":"metric","cnt":"2","appid":"92643b90956fffa5f16a46f09c6927e1"}

url = "https://api.openweathermap.org/data/2.5/forecast"

querystring = {"lat":"13.76455","lon":"100.62296","exclude":"daily","units":"metric","cnt":"2","appid":"92643b90956fffa5f16a46f09c6927e1"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)


data_txt = response.text
print(data_txt)

# data_json = json.loads(data_txt)
# print('------------ current ---------------------------')
# print(data_json["current"]['temp'])
# print(data_json["current"]['humidity'])
# print(data_json["current"]['wind_speed'])
# print('------------         ---------------------------')
# current
# print(response.json)

# print(response.text)


