def without_end(str):
    """
    Given a string, return a version without the first and last char,
    so "Hello" yields "ell". The string length will be at least 2.

    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'

    :param str: str
    :return: str
    """
    return str[1:-1]


print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))
