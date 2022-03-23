from fastapi import APIRouter


from sevices.add_10_devices import add_10_devices

from utils.db import get_devices_without_endpoint1

devices_router = APIRouter(
    prefix='/devices'
)


@devices_router.post('/add_10_devices', status_code=201)
async def add_devices():
    return await add_10_devices()


@devices_router.get('/get_devices_without_endpoint')
async def get_devices_without_endpoint():
    return get_devices_without_endpoint1()