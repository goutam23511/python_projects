import requests


user=input("Enter which country's weather you want to know: ")

geo_coding="https://geocoding-api.open-meteo.com/v1/search"
params={
    'name':user,
    'count':1
}
ans=requests.get(geo_coding,params)
pack=ans.json()


lat=pack['results'][0]['latitude']
long=pack['results'][0]['longitude']


web=("https://api.open-meteo.com/v1/forecast")
params={
    'latitude': lat,
    'longitude': long,
    'current_weather': True
}


response=requests.get(web,params=params)
data=response.json()

print(f'{data['current_weather']['temperature']}°C')