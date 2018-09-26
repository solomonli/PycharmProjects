def max_end(nums):
    """
    Given an array of ints length 3, figure out which is larger,
    the first or last element in the array, and set all the other elements
    to be that value. Return the changed array.

    max_end3([1, 2, 3]) → [3, 3, 3]
    max_end3([11, 5, 9]) → [11, 11, 11]
    max_end3([2, 11, 3]) → [3, 3, 3]

    :param nums: list of ints length 3
    :return: list of ints
    """
    m = max(nums[0], nums[-1])
    return [m for i in nums]


print(max_end([1, 2, 3]))
print(max_end([11, 5, 9]))
print(max_end([2, 11, 3]))
