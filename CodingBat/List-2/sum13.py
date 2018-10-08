def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that
     come IMMEDIATELY AFTER a 13 also do not count.

    sum13([1, 2, 2, 1]) → 6
    sum13([1, 1]) → 2
    sum13([1, 2, 2, 1, 13]) → 6

    :param nums: list of ints
    :return: int
    """
    s = counter = 0

    for n in nums:
        if n == 13 | counter == 1:
            counter += 1
        else:
            s += n
            counter = 0

    return s


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
