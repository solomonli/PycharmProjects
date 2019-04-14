l = [1, 2, 4, 4]
s = 8


def find_pair_with_the_sum(lst, sm):
    """
    Return the pair(s) whose elements add up to the fixed sum
    :param lst: an order list with integers
    :param sm: an int
    :return: pair(s) with ints
    """
    if len(lst) < 2 or lst[0] + lst[-1] < sm:
        return "No qualified pair can be found."

    lst.sort()

    k = len(lst)

    for i in range(len(lst)):
        while lst[i] + lst[k - i - 1]