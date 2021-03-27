from typing import List

from fastapi import FastAPI

from entities import Place, City
from data import get_mocked_places, get_mocked_cities


app = FastAPI()


@app.get('/cities', response_model=List[City])
async def get_cities():
    return get_mocked_cities()


@app.get('/places', response_model=List[Place])
async def get_places():
    return get_mocked_places()


@app.get('/places/{username}', response_model=List[Place])
async def get_city_places(username: str, city_id: int):
    return get_mocked_places()


@app.post('/places/{username}', response_model=List[Place])
async def get_user_places(username: str, data: List[int]):
    return get_mocked_places()
