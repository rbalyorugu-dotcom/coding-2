import requests
url = ("https://pokeapi.co/api/v2/pokemon-species/{id or name}/")
response = requests.get(url)

print(response)
print(response.json())