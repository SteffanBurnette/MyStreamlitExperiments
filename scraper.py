import requests
from bs4 import BeautifulSoup

#Getting up to date yugioh meta datas
url = "https://www.yugiohmeta.com/top-decks/duelist-mainland-ocg-29-11-2025/dracotail/player/RmO0F"
response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

print(response.text)


