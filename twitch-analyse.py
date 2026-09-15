import requests
import json
import time
from datetime import datetime

CLIENT_ID = "svilhohdh7l9feel94x5pg5xwzpl6x"
CLIENT_SECRET = "ilwuwmw4y8j25mk91q7iajg1lakvz3"

def get_token():
    url = "https://id.twitch.tv/oauth2/token"

    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    r = requests.post(url, params=params)

    data = r.json()
    return data["access_token"]


def get_streams(token):

    url = "https://api.twitch.tv/helix/streams"

    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    return response.json()

token = get_token()
while True:
    data = get_streams(token)
    snapshot = {"timestamp": datetime.now().isoformat(), "data": data["data"]}
    filename = r"C:\Users\Laurent\Desktop\recuperation\Data analyse\Twitch project\twitch_Data\raw\twitch_history.jsonl"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot) + "\n")
        print("Snapshot enregistré :", snapshot["timestamp"])
        time.sleep(300)