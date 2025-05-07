import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
data = response.json()

if data["success"] and data["data"]:
    user = data["data"]["data"]
    for  value in user:
        print(f" full name is a'{value["name"]["first"]}''{value["name"]["last"]}'")
