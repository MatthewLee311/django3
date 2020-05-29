import requests
import re
from bs4 import BeautifulSoup
URL = 'https://fftoday.com/stats/players?Pos=QB'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find()
player_data = results.find_all(class_='bodycontent')
playerlinks = re.finditer("/stats/players",str(player_data))
for link in playerlinks:
    if link:
        URL = link.group(0)
        print(URL)
