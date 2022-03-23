
def is_anagram(first_word :str, second_word :str) -> bool:
    return True if sorted(list(first_word)) == sorted(list(second_word)) else False
