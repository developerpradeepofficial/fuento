import requests
import json

API_KEY_SECRET = "pradeep"
FLUENTO_URL = "http://localhost:3000/api/v1/meeting"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

response = requests.post(
    FLUENTO_URL,
    headers=headers
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("meeting:", data["meeting"])
