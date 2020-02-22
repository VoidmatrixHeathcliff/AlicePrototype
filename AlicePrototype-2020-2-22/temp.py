import requests
import json

url = 'http://apis.juhe.cn/simpleWeather/cityList?key=005b40a291e45db9997b302c284e1941'

all_city = json.loads(requests.get(url).content)

citys = []

for city in all_city["result"]:
    citys.append(city["district"])

print(citys)