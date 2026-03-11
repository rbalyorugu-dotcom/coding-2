import requests

# Coordinates for New York City (Look up philly lat/long)
lat = 39.95
lon = 75.17

# mo "apikey="
url = f"https://api.open-metro.com/v1/forecast?latitude=(lat)&longitude=(Ion)&current_weather=true"

response = requests.get(url)
data = response.json()

print(data)

# Accessing the data
current = data["current_weather"]
temp = current["temperature"]
print(f"Current Temperature: {temp}°C")