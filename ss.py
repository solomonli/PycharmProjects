def max_sum(lst, l):
    """
    returns the largest sum of non-adjacent numbers: [2, 4, 6, 2, 5] should return 13,
    since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    :param lst: a list of numbers that can be 0 or negative
    :param l: an integer - the length of list lst minus one
    :return: an integer
    """
    if l == 0:
        return lst[0]

    if l == 1:
        return max(lst[0], lst[1])

    return max(max_sum(lst, l - 2) + lst[l], max_sum(lst, l - 1))


print(max_sum([5, 1, 1, 5], 3))
