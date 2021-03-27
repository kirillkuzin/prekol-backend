from typing import List

from fastapi import FastAPI
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import great_circle_distance_matrix
import httpx

from entities import Place, City
import data


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
    places = await data.get_user_places(username)
    cities = await data.get_cities()

    predict_url = 'http://94.143.44.149:8080/predict'
    predict_data = {
        "sight_ids": [place['id'] for place in places],
    }
    predict_params = {
        "cities": [city['title'] for city in cities if city['id'] == city_id][0]
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(predict_url, json=predict_data, params=predict_params)
        places_ids = r.json()['sight_ids'][:10]
    places = await data.get_places_by_ids(places_ids)

    return [Place(**place) for place in places]


@app.post('/places/{username}', status_code=201)
async def save_user_places(username: str, places_ids: List[int]):
    await data.save_user_places(username, places_ids)


@app.post('/routes', response_model=List[Place], status_code=201)
async def get_route(places_ids: List[int], lat: float, lon: float):
    places = await data.get_places_by_ids(places_ids)

    if len(places) <= 1:
        return []

    sources = np.array([[lat, lon]])
    i = 0
    for place in places:
        print('index', i)
        i += 1
        print('id', place['id'])
        place_coords = np.array([[place['lat'], place['lon']]])
        sources = np.concatenate((sources, place_coords))

    distance_matrix = great_circle_distance_matrix(sources)
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

    print(permutation)

    route = []
    for place_index in permutation[1:]:
        print('index', place_index - 1)
        print('id', places[place_index - 1]['id'])
        route.append(places[place_index - 1])

    return [Place(**place) for place in places]


@app.get('/news/{city_id}')
async def get_news(city_id: int):
    pass
