import requests

url = "https://rickandmortyapi.com/api/character/1"
response = requests.get(url)

RickSanchez = "https://rickandmortyapi.com/api/RickSanchez"
res = requests.get()

SummerSmith = "https://rickandmortyapi.com/api/SummerSmith"
res = requests.get()

RickPrime = "https://rickandmortyapi.com/apiRickPrime"
res = requests.get()

print(response)
print(response.json())
