def make_pi():
    """
    Return an int array length 3 containing the first 3 digits of pi,
    {3, 1, 4}.

    make_pi() → [3, 1, 4]

    :return: list of int
    """
    import math
    pie = str(math.pi)

    after_decimal = [int(i) for i in pie[2:]]

    return [3] + after_decimal


print(make_pi())
