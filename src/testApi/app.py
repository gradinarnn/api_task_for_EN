import uvicorn
from fastapi import FastAPI

from api import api_router
from settings import uvicorn_port, uvicorn_host

app = FastAPI()
app.include_router(api_router)

uvicorn.run(app, host=uvicorn_host, port=uvicorn_port)
