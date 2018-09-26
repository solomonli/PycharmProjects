def has22(nums):
    """
    Given an array of ints, return True if the array contains
    a 2 next to a 2 somewhere.

    has22([1, 2, 2]) → True
    has22([1, 2, 1, 2]) → False
    has22([1, 2, 1, 2]) → False

    :param nums: list of ints
    :return: boolean
    """
    string = ''.join(str(i) for i in nums)
    return '22' in string


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([1, 2, 1, 2]))
