from typing import Optional

from pydantic import BaseModel


class Place(BaseModel):
    id: int
    title: str
    type: str
    description: Optional[str]
    lon: float
    lat: float
    image_url: str
    city_id: int


class City(BaseModel):
    id: int
    title: str
    image_url: str


class News(BaseModel):
    id: int
    title: str
