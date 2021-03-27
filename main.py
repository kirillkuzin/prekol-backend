from typing import List

from fastapi import FastAPI
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import great_circle_distance_matrix

from entities import Place, City
import data
from mocked_data import get_mocked_places


app = FastAPI()


@app.on_event('startup')
async def startup_event():
    await data.db.connect()


@app.on_event('shutdown')
async def shutdown_event():
    await data.db.disconnect()


@app.get('/cities', response_model=List[City])
async def get_cities():
    cities = await data.get_cities()
    return [City(**city) for city in cities]


@app.get('/places', response_model=List[Place])
async def get_places():
    places = await data.get_places()
    return [Place(**place) for place in places]


@app.get('/places/{username}', response_model=List[Place])
async def get_user_places(username: str, city_id: int):
    places = await data.get_user_places(username, city_id)
    return [Place(**place) for place in places]


@app.post('/places/{username}', status_code=201)
async def save_user_places(username: str, places_ids: List[int]):
    await data.save_user_places(username, places_ids)


@app.post('/routes/{username}', response_model=List[Place], status_code=201)
async def get_route(username: str, places_ids: List[int]):
    places = await data.get_places_by_ids(places_ids)
    sources = np.array([
        [16.366461, 48.200127],
        [16.366182, 48.200581],
        [16.365774, 48.200504],
        [16.367483, 48.198936]
    ])
    # sources = np.array([])
    # for place in places:
    #     print(place['lat'])
    #     print(place['lon'])
    #     np.append(sources, [place['lat'], place['lon']])
    print(sources)
    distance_matrix = great_circle_distance_matrix(sources)
    print(distance_matrix)
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
    print(permutation)
    print(distance)
    return get_mocked_places()
