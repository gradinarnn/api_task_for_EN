import os
from dotenv import load_dotenv

from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

uvicorn_host = 'localhost'
uvicorn_port = 8888

redis_server_host = 'localhost'
redis_server_port = 6379
REDIS_URL = f'redis://{redis_server_host}:{redis_server_port}'

db_server_host = os.getenv("host_server")
db_server_port = os.getenv("db_server_port")
db_name = os.getenv("database_name")
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")
POSTGRESQL_URL = f'postgresql+asyncpg://{db_username}:{db_password}@{db_server_host}:{db_server_port}/{db_name}'
