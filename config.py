import os

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'secret')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'some_user')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'db_for_asyncio')
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
PORT = int(os.getenv("POSTGRES_PORT", 5429))

PG_DSN = os.getenv("PG_DSN", f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{PORT}/{POSTGRES_DB}")
