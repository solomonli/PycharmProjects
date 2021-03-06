def sum_double(a, b):
    """
    Given two int values, return their sum.
    Unless the two values are the same, then return double their sum.

    sum_double(1, 2) → 3
    sum_double(3, 2) → 5
    sum_double(2, 2) → 8
    """
    s = a + b

    if a == b:
        s *= 2

    return s


print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))
