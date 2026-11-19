import requests

URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(URL, timeout=5)
print("Status code:", response.status_code)

users = response.json()

for user in users[:3]:
    print(f"{user['id']} - {user['name']} - {user['email']}")