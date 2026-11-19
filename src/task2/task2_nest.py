import json
import requests

URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(URL, timeout=5)
users = response.json()

users_with_city = []
for user in users:
    users_with_city.append({
        "id": user.get("id"),
        "name": user.get("name"),
        "city": user.get("address", {}).get("city"),
    })

with open("data/users.json", "w") as file:
    json.dump(users_with_city, file, indent=4)

print("Saved users.json with", len(users_with_city), "users")
print(users_with_city[0])