def count_evens(nums):
    """
    Return the number of even ints in the given array. Note:
    the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

    count_evens([2, 1, 2, 3, 4]) → 3
    count_evens([2, 2, 0]) → 3
    count_evens([1, 3, 5]) → 0

    :param nums: list of ints
    :return: int
    """
    return len([x for x in nums if x % 2 == 0])
    # [expr for val in collection if condition]


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
