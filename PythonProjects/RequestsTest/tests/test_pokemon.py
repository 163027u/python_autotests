import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '48bfa9c978a6aa0d0022235d75c375fb'
HEADER = {'Content-Type':'application/json', 'trainer_token': f'{TOKEN}'}
TRAINER_ID = '36788'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200