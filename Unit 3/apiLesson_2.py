# API - Application Programming Interface
# Allows computers to share data between devices
# via the internet

# functions that let us share data back and forth over
# the internet

import requests # modules -->
# is object with methods and properties that
# were already written/ prewwritten for us

data = requests.get('https://restcountries.com/v3.1/name/peru')

print(data)
print(data.json())
# Use the API to find data on 1 African country
# 1 South American country, and 1 Asian country. You should have 3
# variables returning data for each type of country.

africanCountry = requests.get('https://restcountries.com/v3.1/name/angola')
asianCountry = requests.get('https://restcountries.com/v3.1/name/japan')
southAmericanCountry = requests.get('https://restcountries.com/v3.1/name/columbia')

print(africanCountry[0].json())
print(asianCountry[0].json())
print(southAmericanCountry[0].json())

