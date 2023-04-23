import os
import requests
from fastapi import FastAPI

app = FastAPI()

def ping_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Pinged {url} successfully!")
        else:
            print(f"Received a {response.status_code} status code when pinging {url}")
    except Exception as e:
        print(f"Encountered an error while pinging {url}: {e}")

@app.get("/")
async def index():
    ping_website("https://localhost:8089/get")
    name = os.getenv("NAME", "world")
    return f"hello {name}!"
