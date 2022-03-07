import requests
from bs4 import BeautifulSoup
import pandas as pd
games = []
page = 1

for i in range(1,19):
    url = f'https://stopgame.ru/games/filter?year_start=2000&rating=musor&p={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    for el in soup.select('.game-summary-horiz > .details'):
        title = el.select('.caption > a')
        games.append(title[0].text)

for i in range(1,19):
    url = f'https://stopgame.ru/games/filter?year_start=2000&rating=izumitelno&p={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    for el in soup.select('.game-summary-horiz > .details'):
        title = el.select('.caption > a')
        games.append(title[0].text)


for i in range(1,40):
    url = f'https://stopgame.ru/games/filter?year_start=2000&rating=pohvalno&p={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    for el in soup.select('.game-summary-horiz > .details'):
        title = el.select('.caption > a')
        games.append(title[0].text)

for i in range(1,20):
    url = f'https://stopgame.ru/games/filter?year_start=2000&rating=prohodnyak&p={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    for el in soup.select('.game-summary-horiz > .details'):
        title = el.select('.caption > a')
        games.append(title[0].text)

for i in range(len(games)):
    games[i] = games[i][:-1]
    games[i] = games[i].replace('\n', '')
    games[i] = games[i].replace(':','')
    games[i] = games[i].replace('(', '')
    games[i] = games[i].replace(')', '')
    games[i] = games[i].replace('/', '')
    games[i] = games[i].replace('.', '')
    games[i] = games[i].replace("'", '')
    games[i] = games[i].replace(" ", '-')

print(games)
print(len(games))
header = ['Name', 'description', 'background_image']
CSV_Data = []
for game in games:
    result = []
    try:
        url = f"https://rawg-video-games-database.p.rapidapi.com/games/{game}?key=7c70e86869c7461f95fb64762ed01acf"
        headers = {
            'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com",
            'x-rapidapi-key': "d26f1b6c2fmshbf61dfc0f771d64p150340jsn3061a9c3d604"
            }

        response = requests.request("GET", url, headers=headers)
        data = response.json()
        result.append(data['name'])
        result.append(data['description'])
        result.append(data['background_image'])
        CSV_Data.append(result)
    except:
        pass

data = pd.DataFrame(CSV_Data, columns=header)
data.to_csv('games.csv')