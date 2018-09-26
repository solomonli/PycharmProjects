def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) → 1
    array_count9([1, 9, 9]) → 2
    array_count9([1, 9, 9, 3, 9]) → 3

    :param nums: list of ints
    :return: int
    """

    return nums.count(9)


print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))
