def array123(nums):
    """
    Given an array of ints, return True if the sequence of numbers
    1, 2, 3 appears in the array somewhere.

    array123([1, 1, 2, 3, 1]) → True
    array123([1, 1, 2, 4, 1]) → False
    array123([1, 1, 2, 1, 2, 3]) → True

    :param nums: list of int
    :return: boolean
    """
    string = ''.join(str(i) for i in nums)

    return '123' in string


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
