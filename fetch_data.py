import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

def fetch_and_store_articles():
    print("Fetching articles...")
    url = f"{URL}{API_KEY}"
    res = requests.get(url)

    res_json = res.json()
    print(res_json)


fetch_and_store_articles()

