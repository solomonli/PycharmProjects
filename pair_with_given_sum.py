l = [1, 4, 5, 8]
s = 9


def find_pair_given_the_sum1(lst, sm):
    """
    Return the pair(s) whose elements add up to the fixed sum
    :param lst: an order list with integers
    :param sm: an int
    :return: pair(s) with ints
    """
    lst.sort()

    if len(lst) < 2 or lst[-2] + lst[-1] < sm:
        return "No qualified pair can be found."

    import itertools

    return [[i, j] for i, j in itertools.combinations(lst, 2) if i + j == sm] or "No qualified pair can be found."


def find_pair_given_the_sum2(lst, sm):
    """
    Return the pair(s) whose elements add up to the fixed sum
    :param lst: an order list with integers
    :param sm: an int
    :return: pair(s) with ints
    """
    lst.sort()

    if len(lst) < 2 or lst[-2] + lst[-1] < sm:
        return "No qualified pair can be found."

    res = []

    for i in range(len(lst) - 1):
        if sm - lst[i] in lst[i + 1:]:
            res.append([lst[i], sm - lst[i]])

    return res


print(find_pair_given_the_sum2(l, s))
