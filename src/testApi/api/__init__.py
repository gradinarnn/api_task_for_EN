from fastapi import APIRouter

from .anagrams import check_anagrams_router
from .devices import devices_router

api_router = APIRouter()
api_router.include_router(check_anagrams_router)
api_router.include_router(devices_router)