import requests

url = "https://catfact.ninja/fact"

response = requests.get(url) 

data = response.json()

fact = data["fact"]

print("🐱 Random Cat Fact:")
print(fact)
