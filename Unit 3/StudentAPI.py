import requests

url = "https://rickandmortyapi.com/api/character/1,183"
res = requests.get(url)

if res.status_code == 200:
    charData = res.json()
    filtData = {
        "name": charData["name"],
        "gender": charData["gender"],
        "image": charData["image"],
    }
    print(filtData)
else:
    print("something went wrong")
    print(res.status_code)

url_2 = "https://rickandmortyapi.com/api/character/60"
res = requests.get(url_2)

if res.status_code == 200:
    charData = res.json()
    filtData = {
        "name": charData["name"],
        "gender": charData["gender"],
        "image": charData["image"],
    }
    print(filtData)
else:
    print("something went wrong")
    print(res.status_code)


url_3 = "https://rickandmortyapi.com/api/character/400"
res = requests.get(url_3)

if res.status_code == 200:
    charData = res.json()
    filtData = {
        "name": charData["name"],
        "gender": charData["gender"],
        "image": charData["image"],
    }
    print(filtData)
else:
    print("something went wrong")
    print(res.status_code)