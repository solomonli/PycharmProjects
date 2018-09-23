def string_bits(str):
    """
    Given a string, return a new string made of every other char
    starting with the first, so "Hello" yields "Hlo".

    string_bits('Hello') → 'Hlo'
    string_bits('Hi') → 'H'
    string_bits('Heeololeo') → 'Hello'

    :param str: str
    :return: str
    """
    return str[::2]


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
