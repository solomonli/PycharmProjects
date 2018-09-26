def sum67(nums):
    """
    Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6 and
    extending to the next 7 (every 6 will be followed by at least one 7).
    Return 0 for no numbers.

    sum67([1, 2, 2]) → 5
    sum67([1, 2, 2, 6, 99, 99, 7]) → 5
    sum67([1, 1, 6, 7, 2]) → 4

    :param nums: list of ints
    :return: int
    """
    s = 0
    flag = False

    for n in nums:

        if n == 6:
            flag = True     # found a 6!
        elif n == 7 and flag:   # found the corresponding 7!
            flag = False
        elif not flag:      # a normal number
            s += n

    return s


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
