from utils.is_anagram import is_anagram
from utils.redis_working import get_value
from utils.redis_working import set_value


async def check_anagrams(first_word, second_word):
    response = {"is_anagram": False}
    amount_anagram = 0 if not await get_value("anagrams") else int(await get_value("anagrams"))
    if is_anagram(first_word, second_word):
        amount_anagram += 1
        await set_value("anagrams", amount_anagram)
    response["val"] = amount_anagram
    return response
