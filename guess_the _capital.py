import requests
import random

response=requests.get("https://countriesnow.space/api/v0.1/countries/capital")
use=response.json()

while True:
    random_country=random.randint(1,250)
    capital=use['data'][random_country]['capital'].lower()
    user=input(f'What is the capital of {use['data'][random_country]['name']}? or quit: ').lower()

    if user==capital:
        print(f'Yes you are right!! It was {capital}')

    elif user!=capital and user!='quit':
        print(f'Wrong that was not the capital.Answer={capital}')

    else:
        print('Thank you')
        break 
    


