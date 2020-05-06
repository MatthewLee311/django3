import requests
URL = 'https://www.espn.com/nfl/'
page = requests.get(URL)

print(page)
