def near_ten(num):
    """
    Given a non-negative number "num", return True if num is within
    2 of a multiple of 10.
    Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
    See also: Introduction to Mod

    near_ten(12) → True
    near_ten(17) → False
    near_ten(19) → True

    :param num: non-negative int
    :return: boolean
    """
    _, b = divmod(num, 10)
    return b <= 2 | b >= 8


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
