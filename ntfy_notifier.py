import os 
import requests
from dotenv import load_dotenv

load_dotenv()
Topic=os.getenv("ntfy_topic")

def notify(content,title):
    response=requests.post(
        f"https://ntfy.sh/{Topic}",
        data=content.encode("utf-8"),
        headers={"Title":title}
    )
    return response

print(notify(content='Are you still locked in',title='Python'))