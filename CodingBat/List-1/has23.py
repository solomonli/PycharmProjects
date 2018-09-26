def has23(nums):
    """
    Given an int array length 2, return True if it contains a 2 or a 3.

    has23([2, 5]) → True
    has23([4, 3]) → True
    has23([4, 5]) → False

    :param nums: list of ints length 2
    :return: boolean
    """
    return 2 in nums or 3 in nums


print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))
