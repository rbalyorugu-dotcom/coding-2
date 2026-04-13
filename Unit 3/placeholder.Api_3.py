query = "https://pokeapi.co/api/v2/pokemon/tangela"
response = requests.get(query)

print(response)
print(response["name]")

data = json.loads(response.json())