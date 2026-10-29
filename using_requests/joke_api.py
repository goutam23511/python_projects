import requests 
import time 

response=requests.get("http://www.official-joke-api.appspot.com/random_joke")
data=response.json()
print(data['setup'])
time.sleep(5)
print(data['punchline'])
