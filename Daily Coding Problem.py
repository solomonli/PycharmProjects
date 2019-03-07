"""

"""

def add_up(lst, k):
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
    :param lst: a list of integers
    :param k: an integer
    :return: boolean
    """
    assert isinstance(k, int)
    l = len(lst)
    ll = []
    for i in range(l // 2):
        for j in range(l // 2, l):
            ll.append(lst[i] + lst[j] == k)
     return any(ll)

# in a single line

def add_up(lst, k):
    return any([lst[i] + lst[j] == k for i in range(len(lst) // 2) for j in range(len(lst) // 2, len(lst))])

from itertools import combinations
any(a + b == k for a, b in combinations(lst, 2))



def multiple_rest(lst):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is
    the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?

    :param lst: a list of integers
    :return: a list of integers with same length
    """
    from itertools import combinations
    from functools import reduce

    res = []

    for i in list(combinations(lst, len(lst) - 1)):
        res.append(reduce(lambda x, y: x * y, i))

    res.reverse()
    # res[::-1]

    return res


print(multiple_rest([1, 2, 3]))
















