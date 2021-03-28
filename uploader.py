import csv
import asyncio

from tqdm import tqdm

from data import db, get_cities, save_place


async def main():
    await db.connect()

    cities = {}
    cities_data = await get_cities()
    for city_data in cities_data:
        cities.update({city_data['title']: city_data['id']})

    print(cities)

    with open('data.csv') as file:
        data = csv.DictReader(file)
        data = list(data)
        with tqdm(total=len(data)) as pbar:
            for row in data:
                try:
                    title = row['name']
                    description = row['wikipedia_extracts']
                    place_type = row['category']
                    lon = float(row['longitude'])
                    lat = float(row['latitude'])
                    image_url = row['clear_link']
                    city_id = cities[row['capital']]
                    await save_place(title=title,
                                     description=description,
                                     place_type=place_type,
                                     lon=lon,
                                     lat=lat,
                                     image_url=image_url,
                                     city_id=city_id)
                    pbar.update(1)
                except Exception as e:
                    print(e)

    await db.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
