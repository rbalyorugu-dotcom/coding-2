





import requests

query = "https://pokeapi.co/api/v2/pokemon/tangela"
response = requests.get(query)

print(response)
print(response.status_code)

data = response.json()

if response.status_code == 200:
    data = response.json()
    # print(data)

    filtered_data = {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": data["types"],
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
        "sprites": data["sprites"]
    }

    print(filtered_data)
else:
    print("data not found")
    print("response.status_code")

