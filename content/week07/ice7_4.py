import string


def is_pangram(sentence):
    sentence = sentence.lower()
    pool = list(string.ascii_lowercase)
    for ch in sentence:
        if ch in pool:
            pool.remove(ch)
    if pool != []:
        return False
    return True
    # OR
    # for char in string.ascii_lowercase:
    #     if char not in sentence.lower():
    #         return False
    # return True

    # OR
    # return not set(string.ascii_lowercase) - set(sentence.lower())


print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("The quick brown fox jumps over the lazy cat."))
