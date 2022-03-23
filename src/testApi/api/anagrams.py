from fastapi import APIRouter

from sevices.check_anagrams import check_anagrams

from settings import POSTGRESQL_URL

check_anagrams_router = APIRouter(
    prefix='/check_anagrams'
)


@check_anagrams_router.get('/')
async def root(first_word: str, second_word: str):

    print(POSTGRESQL_URL)

    return await check_anagrams(first_word,second_word)
