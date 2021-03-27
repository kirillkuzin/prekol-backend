from typing import Optional

from pydantic import BaseModel


class Place(BaseModel):
    place_id: int
    title: str
    type: str
    description: Optional[str]
    lon: float
    lat: float
    image_url: str
    city_id: int


class City(BaseModel):
    city_id: int
    title: str
    image_url: str
