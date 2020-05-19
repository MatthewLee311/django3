import requests
from bs4 import BeautifulSoup
URL = 'https://fftoday.com/stats/players?Pos=QB'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find()
player_data = results.find_all(class_='bodycontent')
for player in player_data:
    player_url = player.find_all('a')
    print(player_url)
    url = soup.href.extract()
