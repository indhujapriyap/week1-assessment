import requests

URL = "https://jsonplaceholder.typicode.com/users"


def get_data(url):
    try:
        return requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        print("Error: the website took too long to answer")
    except requests.exceptions.ConnectionError:
        print("Error: could not connect, check your internet")
    return None


response=get_data(URL)
if response is not None:
    print("Normal call status:", response.status_code)

missing=get_data(URL + "/9999")
if missing is not None:
    if missing.status_code == 404:
        print("/users/9999 -> 404 Not found")