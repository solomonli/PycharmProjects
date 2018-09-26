def extra_word(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars
     of the original string. The string length will be at least 2.

    extra_end('Hello') → 'lololo'
    extra_end('ab') → 'ababab'
    extra_end('Hi') → 'HiHiHi'
    :param str: str
    :return: str
    """
    return str[-2:] * 3


print(extra_word('Hello'))
print(extra_word('ab'))
print(extra_word('Hi'))
