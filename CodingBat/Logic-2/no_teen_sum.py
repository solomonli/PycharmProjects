def no_teen_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However,
    if any of the values is a teen -- in the range 13..19 inclusive --
    then that value counts as 0, except 15 and 16 do not count as a teens.
    Write a separate helper "def fix_teen(n):"
    that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times
    (i.e. "decomposition"). Define the helper below and
    at the same indent level as the main no_teen_sum().

    no_teen_sum(1, 2, 3) → 6
    no_teen_sum(2, 13, 1) → 3
    no_teen_sum(2, 1, 14) → 3

    :param a: int
    :param b: int
    :param c: int
    :return:
    """
    # lst = [0 if fix_teen(i) else i for i in [a, b, c]]
    # return sum(lst)

    return sum(filter(safe_teen, [a, b, c]))

# def fix_teen(n):
#     return n in range(13, 15) or n in range(17, 20)


def safe_teen(n):
    my_range = list(range(13, 15)) + list(range(17, 20))
    return n not in my_range


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
