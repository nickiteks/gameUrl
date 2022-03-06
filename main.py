import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games/uncharted-4-a-thiefs-end?key=7c70e86869c7461f95fb64762ed01acf"

headers = {
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com",
    'x-rapidapi-key': "d26f1b6c2fmshbf61dfc0f771d64p150340jsn3061a9c3d604"
    }

response = requests.request("GET", url, headers=headers)
data = response.json()
print(data['name'])
print(data['description'])
print(data['background_image'])
print(data['background_image_additional'])