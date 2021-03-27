from typing import List

from entities import Place, City


def get_mocked_places() -> List[Place]:
    places_data = [
        {
            "place_id": 1,
            "title": "test_title",
            "type": "test_type",
            "description": "test_desc",
            "lon": 100.0,
            "lat": 200.0,
            "image_url": "https://n1s2.hsmedia.ru"
                         "/83/25/7a/83257a4776bd2b5c8a0299ed6e3620fc"
                         "/690x460_0xc0a8392b_18520924581476094146.jpeg",
            "city_id": 1
        }
    ]
    return [Place(**place_data) for place_data in places_data]


def get_mocked_cities() -> List[City]:
    cities_data = [
        {
            "city_id": 1,
            "title": "Prekol City",
            "image_url": "https://n1s2.hsmedia.ru"
                         "/83/25/7a/83257a4776bd2b5c8a0299ed6e3620fc"
                         "/690x460_0xc0a8392b_18520924581476094146.jpeg"
        }
    ]
    return [City(**city_data) for city_data in cities_data]
