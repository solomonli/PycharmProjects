def love6(a, b):
    """
    The number 6 is a truly great number. Given two int values, a and b,
    return True if either one is 6. Or if their sum or difference is 6.
    Note: the function abs(num) computes the absolute value of a number.

    love6(6, 4) → True
    love6(4, 5) → False
    love6(1, 5) → True

    :param a: int
    :param b: int
    :return: boolean
    """
    s = a + b
    diff = abs(a - b)

    return a == 6 | b == 6 | s == 6 | diff == 6


print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
