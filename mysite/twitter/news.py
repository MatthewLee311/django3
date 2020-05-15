import requests
from bs4 import BeautifulSoup
URL = 'https://fftoday.com/stats/players?Pos=QB'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find()
player_data = results.find_all(class_='bodycontent')
print(player_data)
for player in player_data:
    player_name = player.find('span', class_='')
    print(player_name)
