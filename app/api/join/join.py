# pip3 install requests
import requests
import json

API_KEY_SECRET = "pradeep"
FLUENTO_URL = "http://localhost:3000/api/v1/join"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "room": "test",
    "name": "Pradeep",
    "audio": "true",
    "video": "true",
    "screen": "false",
    "hide": "false",
    "notify": "true",
    "token": {
        "username": "username",
        "password": "password",
        "presenter": "true",
        "expire": "1h",
    }
}

response = requests.post(
    FLUENTO_URL,
    headers=headers,
    json=data,
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("join:", data["join"])
