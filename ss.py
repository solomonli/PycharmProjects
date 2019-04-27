class orderlog:
    """
    You run an e-commerce website and want to record the last N order ids in a log.
    Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    """
    def __init__(self, num):
        self.container = [None] * num
        self.current_index = len(self.container)

    def record(self, order_id):
        self.container.append(order_id)
        return f'The Order ID {order_id} has been added to the log.'

    def get_last(self, i):
        if i > self.current_index:
            print(f'The whole log returned since the number {i} outsized the log length {self.current_index}.')
        return self.container[-i:]


my_log = orderlog(5)
print(my_log.record(7))
print(my_log.get_last(3))
print(my_log.get_last(10))

"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext 
and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 
containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""


def maximum_subarray(lst, window):
    """
    Given an array of integers and a number k, where 1 <= k <= length of the array,
    compute the maximum values of each subarray of length k.

    For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

        10 = max(10, 5, 2)
        7 = max(5, 2, 7)
        8 = max(2, 7, 8)
        8 = max(7, 8, 7)

    Do this in O(n) time and O(k) space. You can modify the input array in-place and you needn't  store the results.
    You can simply print them out as you compute them.
    :param lst: a list of int
    :param window: an integer
    :return: a list of int
    """
    if k >= len(lst):
        return lst

    res = []

    for i in range(len(lst) - k + 1):
        res.append(max(lst[i: i+k]))

    return res


def house_color(matrix, color_names='ROYGBIV'):
    """
    A builder is looking to build a row of N houses that can be of K different colors.
    He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

    Given an N * K matrix where the Nth row and Kth column represents the cost - matrix[house][color]
    return the minimum cost which achieves this goal.
    :param matrix: a N-length list, with each token of K-length list
    :param color_names: a string sequence containing the names of the colors
    :return: an integer
    """

    num_houses = len(matrix)

    if not num_houses:
        return []

    num_colors = len(matrix[0])

    totals = [None] * num_houses
    totals[0] = matrix[0][:]

    # After the first house, dynamic programming does its magic.
    # At each step, add the price of painting this house to the minimum of the total painting of the other colors.
    for house in range(1, num_houses):
        totals[house] = [matrix[house][color] +
                         min(totals[house - 1][c] for c in range(num_colors) if c != color)
                         for color in range(num_colors)]


    # Now we have the totals to paint up to each house.
    # We'll just work backwards to find the coloring of the houses.
    colorings = [None] * num_houses
    colorings[-1] = min(range(num_colors), key=lambda c: totals[-1][c])

    for house in range(num_houses - 2, -1, -1):
    # Take the index of the cheapest option (infinite cost prohibits consecutive houses with the same color)
        colorings[house] = min(range(num_colors),
                               key=lambda c: totals[house][c] if c != colorings[house + 1]
                               else float('Inf'))

    # Convert color indexes to names
    return [color_names[colorings[house]] for house in range(num_houses)]



















