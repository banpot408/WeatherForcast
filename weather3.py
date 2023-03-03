import requests
import json

# url = "https://api.openweathermap.org/data/2.5/onecall"

# url = "https://api.openweathermap.org/data/2.5/forecast"


# querystring = {"lat":"13.76455","lon":"100.62296","exclude":"daily","units":"metric","cnt":"2","appid":"92643b90956fffa5f16a46f09c6927e1"}

url = "https://api.openweathermap.org/data/2.5/forecast"

querystring = {"lat":"13.76455","lon":"100.62296","exclude":"daily","units":"metric","cnt":"5","appid":"92643b90956fffa5f16a46f09c6927e1"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)


data_txt = response.text
# print(data_txt)
print(response.json)

data_json = json.loads(data_txt)

# print(data_json)


print('------------ current ---------------------------')
print(data_json["city"]['name'])

day1_temp = data_json["list"][0]['main']['temp']
day1_temp_min = data_json["list"][0]['main']['temp_min']
day1_temp_max = data_json["list"][0]['main']['temp_max']
day1_weather = data_json["list"][0]['weather'][0]['description']

day2_temp = data_json["list"][1]['main']['temp']
day2_temp_min = data_json["list"][1]['main']['temp_min']
day2_temp_max = data_json["list"][1]['main']['temp_max']
day2_weather = data_json["list"][1]['weather'][0]['description']

day3_temp = data_json["list"][2]['main']['temp']
day3_temp_min = data_json["list"][2]['main']['temp_min']
day3_temp_max = data_json["list"][2]['main']['temp_max']
day3_weather = data_json["list"][2]['weather'][0]['description']

day4_temp = data_json["list"][3]['main']['temp']
day4_temp_min = data_json["list"][3]['main']['temp_min']
day4_temp_max = data_json["list"][3]['main']['temp_max']
day4_weather = data_json["list"][3]['weather'][0]['description']

day5_temp = data_json["list"][4]['main']['temp']
day5_temp_min = data_json["list"][4]['main']['temp_min']
day5_temp_max = data_json["list"][4]['main']['temp_max']
day5_weather = data_json["list"][4]['weather'][0]['description']

print("Day 1  ===> Temp : {0} has a Temp Max : {1} Temp Min : {2} Weather : {3}". format(day1_temp, day1_temp_min, day1_temp_max, day1_weather))
print("Day 2  ===> Temp : {0} has a Temp Max : {1} Temp Min : {2} Weather : {3}". format(day2_temp, day2_temp_min, day2_temp_max, day2_weather))
print("Day 3  ===> Temp : {0} has a Temp Max : {1} Temp Min : {2} Weather : {3}". format(day3_temp, day3_temp_min, day3_temp_max, day3_weather))
print("Day 4  ===> Temp : {0} has a Temp Max : {1} Temp Min : {2} Weather : {3}". format(day4_temp, day4_temp_min, day4_temp_max, day4_weather))
print("Day 5  ===> Temp : {0} has a Temp Max : {1} Temp Min : {2} Weather : {3}". format(day5_temp, day5_temp_min, day5_temp_max, day5_weather))

print('------------         ---------------------------')




# # current
# print(response.json)

# print(response.text)


