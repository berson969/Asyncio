import asyncio
import datetime
from aiohttp import ClientSession
from more_itertools import chunked
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from models import People, Base
import config

URL = 'https://swapi.dev/api/people/'
CHUNK_SIZE = 10

engine = create_async_engine(config.PG_DSN)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def chunked_async(async_iter, size):

    buffer = []
    while True:
        try:
            item = await async_iter.__anext__()
        except StopAsyncIteration:
            break
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []


async def get_person(people_id: int, session: ClientSession):
    print(f'begin {people_id}')
    async with session.get(f'{URL}{people_id}') as response:
        json_data = await response.json()
    print(f'end {people_id}')
    return json_data


async def get_people():
    async with ClientSession() as session:
        async with session.get(URL) as resp:
            count = await resp.json()
        for chunk in chunked(range(1, count['count']), CHUNK_SIZE):
            coroutines = [get_person(people_id=i, session=session) for i in chunk]
            results = await asyncio.gather(*coroutines)
            for item in results:
                yield item


async def insert_people(people_chunk):
    people_list = [
        People(
            birth_year=item['birth_year'],
            eye_color=item['eye_color'],
            films=', '.join(item['films']),
            gender=item['gender'],
            hair_color=item['hair_color'],
            height=item['height'],
            homeworld=item['homeworld'],
            mass=item['mass'],
            name=item['name'],
            skin_color=item['skin_color'],
            species=', '.join(item['species']),
            starships=', '.join(item['starships']),
            vehicles=', '.join(item['vehicles'])
        )
        for item in people_chunk]

    async with Session() as session:
        session.add_all(people_list)
        await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
    async for chunk in chunked_async(get_people(), CHUNK_SIZE):
        asyncio.create_task(insert_people(chunk))

    tasks = set(asyncio.all_tasks()) - {asyncio.current_task()}
    for task in tasks:
        await task

if __name__ == '__main__':
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)
