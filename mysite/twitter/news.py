import requests
from bs4 import BeautifulSoup
URL = 'https://fftoday.com/stats/players'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='')
