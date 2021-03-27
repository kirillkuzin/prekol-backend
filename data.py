from typing import List, Mapping, Optional

from databases import Database
import sqlalchemy as sa

from tables import cities, places, user_places


db = Database('sqlite:///data.db')


async def get_cities() -> List[Mapping]:
    query = cities.select()
    return await db.fetch_all(query)


async def get_places() -> List[Mapping]:
    query = places.select()
    return await db.fetch_all(query)


async def get_places_by_ids(places_ids: List[int]) -> List[Mapping]:
    query = places.select().where(places.c.id.in_(places_ids))
    return await db.fetch_all(query)


async def get_user_places(username: str, city_id: int) -> List[Mapping]:
    query = sa.select([places])
    query = query.where(sa.and_(user_places.c.username == username,
                                places.c.city_id == city_id))
    join_clause = user_places.join(
        places,
        onclause=(user_places.c.place_id == places.c.id)
    )
    query = query.select_from(join_clause)
    result = await db.fetch_all(query)
    return result


async def save_user_places(username: str, places_ids: List[int]):
    for place_id in places_ids:
        query = user_places.insert().values(username=username,
                                            place_id=place_id)
        await db.execute(query)
