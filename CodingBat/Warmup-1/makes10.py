def makes10(a, b):
    """
    Given 2 ints, a and b, return True if
    one of them is 10 or if their sum is 10.

    makes10(9, 10) → True
    makes10(9, 9) → False
    makes10(1, 9) → True

    :param a: int
    :param b: int
    :return: boolean
    """
    return a + b == 10 or a == 10 or b == 10


print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))
