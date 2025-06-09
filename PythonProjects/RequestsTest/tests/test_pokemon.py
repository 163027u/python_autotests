import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Твой тренер-токен'
HEADER = {'Content-Type':'application/json', 'trainer_token': f'{TOKEN}'}
TRAINER_ID = 'твой тренер-айди'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200