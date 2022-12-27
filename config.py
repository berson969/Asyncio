import os

PG_PASSWORD = os.getenv('PG_PASSWORD', 'secret')
PG_USER = os.getenv('PG_USER', 'some_user')
PG_DB = os.getenv('PG_DB', 'db_for_asyncio')
PG_HOST = os.getenv("PG_HOST", "127.0.0.1")
PG_PORT = int(os.getenv("PG_PORT", 5432))

PG_DSN = os.getenv(
    "PG_DSN",
    f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)
# print(f'{PG_USER=}')
# print(f'{PG_PASSWORD=}')
# print(f'{PG_HOST=}')
# print(f'{PG_PORT=}')
# print(f'{PG_DB=}')