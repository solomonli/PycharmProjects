def string_times(str, n):
    """
    Given a string and a non-negative int n, return a larger string
    that is n copies of the original string.

    string_times('Hi', 2) → 'HiHi'
    string_times('Hi', 3) → 'HiHiHi'
    string_times('Hi', 1) → 'Hi'

    :param str: str
    :param n: non-negative int
    :return: str
    """
    return str * n


print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))
