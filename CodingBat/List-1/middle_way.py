def middle_way(a, b):
    """
    Given 2 int arrays, a and b, each length 3,
    return a new array length 2 containing their middle elements.

    middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

    :param a: list of ints
    :param b: list of ints
    :return: list of ints length 2
    """
    return [a[1]] + [b[1]]


print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))
