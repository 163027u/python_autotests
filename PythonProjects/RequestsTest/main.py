import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Твой тренер-токен'
HEADER = {'Content-Type':'application/json', 'trainer_token': f'{TOKEN}'}
body_registration = {
    "name": "generate",
    "photo_id": -1
}
body_namechange = {
    "pokemon_id": "id",
    "name": "New Name",
    "photo_id": 2
}
body_pokeboll = {
    "pokemon_id": "id"
}

response_registration = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response_registration.text)
response_namechange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_namechange)
print(response_namechange.text)
response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)