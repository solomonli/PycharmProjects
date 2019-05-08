def add_up(lst, k):
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?

    :param lst: a list of integers
    :param k: an integer
    :return: boolean
    """
    assert isinstance(k, int)
    l = len(lst)
    ll = []
    for i in range(l // 2):
        for j in range(l // 2, l):
            ll.append(lst[i] + lst[j] == k)
    return any(ll)

# in a single line

def add_up(lst, k):
    return any([lst[i] + lst[j] == k for i in range(len(lst) // 2) for j in range(len(lst) // 2, len(lst))])

def add_up(lst, k):
    from itertools import combinations
    return any(a + b == k for a, b in combinations(lst, 2))



def multiple_rest(lst):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is
    the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?

    :param lst: a list of integers
    :return: a list of integers with same length
    """
    from itertools import combinations
    from functools import reduce

    res = []

    for i in list(combinations(lst, len(lst) - 1)):
        res.append(reduce(lambda x, y: x * y, i))

    res.reverse()
    # res[::-1]

    return res


# print(multiple_rest([1, 2, 3]))


"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# this function doesn't seem very fit to this problem
def serialize(tree_node):
    vals = []

    def encode(node):
        if node:
            vals.append(node.val)
            encode(node.left)
            encode(node.right)
        else:
            vals.append('#')

    encode(tree_node)

    return '.'.join(vals)


# this function seems problematic...
def deserialize(tree_serial):
    def decode(vals):

        val = next(vals)
        if val == '#':
            return None

        node = Node(val)
        node.left = decode(vals)
        node.right = decode(vals)

        return node

    vals = iter(tree_serial.split('.'))

    return decode(vals)


# below is what I found on the Internet
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """
        the right occasion for a repr to fit in
        :return:
        """
        return ('Node(' + repr(self.val) + ', '
                        + repr(self.left) + ', '
                        + repr(self.right) + ')')

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.val == other.val and
                    self.left == other.left and
                    self.right == other.right)
        else:
            return False

    def __hash__(self):
        """
        optional here
        :return:
        """
        return hash((self.val, self.left, self.right))


serialize = repr
deserialize = eval

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)) == node
assert hash(deserialize(serialize(node))) == hash(node)
# above is what I found on the Internet


def missing_int(lst):
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.

    :param lst: a list of integers that can contain duplicates and negative numbers
    :return: an integer
    """
    pos = list({x for x in lst if x > 0})

    pos.sort()

    if not pos:
        return 1

    standard = pos[0] + 1

    for i in pos[1:]:
        if i == standard:
            standard += 1
        else:
            break

    return standard


# print(missing_int([1]))


# You need some reading from https://docs.python.org/3.6/library/heapq.html#theory
def merge(lists):
    import heapq

    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        # value, list index, element index

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)

    return merged_list


print(merge([[1], [1, 3, 5], [1, 10, 20, 30, 40]]))


"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair

# @cons The function cons, car, or cdr was not written as a decorator


def car(f):
    def left(a, b):
        return a

    return f(left)


def car(f):
    return f(lambda a, b: a)        # !


def cdr(f):
    def right(a, b):
        return b

    return f(right)


def cdr(f):
    return f(lambda a, b: b)        # !


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, 
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to 
get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


def decode_count(string):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    You can assume that the messages are decodable. For example, '001' is not allowed.

    :param string: a string of alpha letters
    :return: an integer, by running base_count(string, len of string)
    """

    def base_count(sub_string, k):
        """
        A helper function that will be return the numbers of decoding of the last K digits of sub_string.
        It will be run recursively in the main function.
        :param sub_string: a str, the input string
        :param k: an integer, the last K digits of sub_string
        :return: an int
        """
        if not k:
            return 1

        s = len(sub_string) - k

        if sub_string[s] == '0':
            return 0

        res = base_count(sub_string, k - 1)

        if k >= 2 and sub_string[s: s+2] <= '26':
            res += base_count(sub_string, k - 2)

        return res

    return base_count(string, len(string))


print(decode_count('222222'))


def decode_count_dp(string):

    memo = [None for _ in range(len(string) + 1)]
    return base_count_dp(string, len(string), memo)


def base_count_dp(sub_string, k, memo):

    if not k:
        return 1

    s = len(sub_string) - k

    if sub_string[s] == '0':
        return 0

    # global memo

    if memo[k] is not None:
        return memo[k]

    res = base_count_dp(sub_string, k - 1, memo)

    if k >= 2 and sub_string[s: s+2] <= '26':
        res += base_count_dp(sub_string, k - 2, memo)

    memo[k] = res

    return res


print(decode_count_dp('222222'))


"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_sum(lst, l):
    """
    returns the largest sum of non-adjacent numbers: [2, 4, 6, 2, 5] should return 13,
    since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    :param lst: a list of numbers that can be 0 or negative
    :param l: an integer - the length of list lst
    :return: an integer
    """
    if l == 1:
        return lst[0]

    if l == 2:
        return max(lst[0], lst[1])

    return max(max_sum(lst, l - 2) + lst[l - 1], max_sum(lst, l - 1))
    # be careful how you use 'l' here


print(max_sum([2, 4, -6, 2, 15], 5))

"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


def LCS(s1, s2, i1, i2):
    """
    find the Longest Common Sequence between two strings
    :param s1: str
    :param s2: str
    :param i1: int, the position pointer
    :param i2: int, the position pointer
    :return: the LCS str
    """
    if i1 == len(s1) or i2 == len(s2):
        return ''

    if s1[i1] == s2[i2]:
        return s1[i1] + LCS(s1, s2, i1+1, i2+1)
    else:
        return max(LCS(s1, s2, i1, i2+1), LCS(s1, s2, i1+1, i2))


print(LCS('Jeez I am waiting for snow.', "Jeez I've been waiting for snow.", 0, 0))


def LCSmemo(s1, s2, i1, i2):
    """
    find the Longest Common Sequence between two strings
    :param s1: str
    :param s2: str
    :param i1: int, the position pointer
    :param i2: int, the position pointer
    :param memo: a list of lists of None to memory the results
    :return: the LCS str
    """
    memo = [[None] * len(s2) for _ in range(len(s1))]       # cool trick!

    return helper(s1, s2, i1, i2, memo)


def helper(s1, s2, i1, i2, memo):

    if i1 == len(s1) or i2 == len(s2):
        return ''

    if memo[i1][i2] is not None:
        return memo[i1][i2]

    if s1[i1] == s2[i2]:
        memo[i1][i2] = s1[i1] + helper(s1, s2, i1+1, i2+1, memo)
        return memo[i1][i2]
    else:
        memo[i1][i2] = max(helper(s1, s2, i1, i2+1, memo), helper(s1, s2, i1+1, i2, memo))
        return memo[i1][i2]


tiik = datetime.datetime.now()

print(LCSmemo('Jeez, I am waiting for snow.', "Jeez, I've been waiting for snow.", 0, 0))

took = datetime.datetime.now()

print(took - tiik)


seq = []


def collatz(num):
    """
    Then each term is obtained from the previous term as follows:
    if the previous term is even, the next term is one half the previous term.
    If the previous term is odd, the next term is 3 times the previous term plus 1.
    The conjecture is that no matter what value of n, the sequence will always reach 1.
    :param num: a positive int
    :return: the Collatz Sequence as a list
    """
    try:
        int(num)
    except ValueError:
        print('Please input an integer instead')

    seq.append(num)

    if seq[-1] == 1:
        return seq

    # print(seq)

    if seq[-1] % 2 == 0:
        return collatz(num // 2)
    elif seq[-1] % 2 != 0:
        return collatz(num * 3 + 1)


print(collatz(97))


def comma_code(lst):
    """
    spam = ['apples', 'bananas', 'tofu', 'cats']
    Write a function that takes a list value as an argument and returns
    a string with all the items separated by a comma and a space, with and
    inserted before the last item. For example, passing the previous spam list to
    the function would return 'apples, bananas, tofu, and cats'.
    But your function should be able to work with any list value passed to it.
    :param lst: a list
    :return: a str
    """
    string = ''

    for i in lst[:-1]:
        string += (str(i) + ', ')

    return string + 'and ' + str(lst[-1])


print(comma_code([3.4, 'bananas', 'tofu', 'cats']))


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def rotate_clockwise(lst):
    """
    to print this image:
    ..OO.OO..
    .OOOOOOO.
    .OOOOOOO.
    ..OOOOO..
    ...OOO...
    ....O....
    :param lst: a list of lists (m*n)
    :return: an array of strings (n*m)
    """
    for n in range(len(lst[0])):
        for m in range(len(lst)):
            print(lst[m][n], end='')
        print()
    pass

    # print(70, 60, 51 41, 31, 21, 10, 00)


print(rotate_clockwise(grid))


spam = {}
spam.setdefault('color', 'black')

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):

    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    return "Total number of items: " + str(item_total)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(display_inventory(stuff))


def add_to_inventory(inventory, added_items):

    for element in added_items:
        if element in inventory:        # also work "element in inventory.keys()"
            inventory[element] += 1
        else:
            inventory[element] = 1

    return inventory


inv = {'gold coin': 42, 'rope': 1}

dragon_loot = ['gold coin', 'dagger', 'sword', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)

print(inv)


"""
Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:
"""
table = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

size = [[None for _ in range(len(table[0]))] for _ in range(len(table))]

for i in range(len(table)):
    for j in range(len(table[0])):
        size[i][j] = len(table[i][j])

max_size = [max(row) for row in size]


assert len(size) == len(table)
assert None not in max_size


for x in range(len(table[0])):
    for y in range(len(table)):
        print(table[y][x].rjust(max_size[y]), end=' ')      # here you can also do " .rjust(max_size[y] + 1), end='' "
    print('')


def job_scheduler(func, n):
    """
    Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
    :param f: a pre-defined function
    :param n: int of milliseconds
    :return: called function f
    """
    import time
    time.sleep(n / 1000)

    return func()


def h():
    return "Hello, world!"


print(job_scheduler(h, 5000))

# from decorators import timer, debug, job_schedule

def query_string(string, target):
    """
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.
    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
    Can I assume case sensitivity?
    :param string: str (e.g. 'de')
    :param target: list of strings (e.g. [dog, deer, deal])
    :return: list of strings
    """
    return list(filter(lambda x: x.startswith(string), target))


print(query_string('de', ['dog', 'deer', 'deal']))


def climb_stairs(n):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
    Given N, write a function that returns the number of unique ways you can climb the staircase.
    The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number
    from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    :param n: positive int, a staircase with N steps
    :return: an int
    """
    if not n:
        return 1

    res = climb_stairs(n - 1)

    if n >= 2:
        res += climb_stairs(n - 2)

    return res


# print(climb_stairs(0))


def climb_any_stair(N, st):
    """
    see the above function
    :param n: positive int, a staircase with N steps
    :param st: a set of positive integers
    :return: an int
    """
    def base(n):
        if not n:
            return 1

        res = 0

        for i in st:
            if i == 1:
                res = base(n - 1)
            elif n >= i:
                res += base(n - i)
            else:
                res = 1     # there's something not right for this line or the above
        return res

    return base(N)

############################################

    if N == 0:
        return 1  # leaf case

    available_choices = [c for c in st if c <= N]
    if not available_choices:
        return 0  # unfeasible

    count = 0
    for c in available_choices:
        count += climb_any_stair(N - c, st)

    return count


print(climb_any_stair(6, {2, 3}))

"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import math

r = 10000       # make a circle with a radius of 10000 unit length

# only consider the points of positive x and y
coordinates = [(x, math.floor((10000**2 - x**2)**0.5)) for x in range(0, 10001)]

guessed_area = 4 * sum(token[1] for token in coordinates)

guessed_pi = guessed_area / 10000**2

"""
Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.

https://en.wikipedia.org/wiki/Reservoir_sampling
"""


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
        res.append(max(lst[i: i + k]))

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

    # At each step, add the price of painting this house to the minimum of the total painting of the other colors.
    for house in range(1, num_houses):
        totals[house] = [matrix[house][color] +
                         min(totals[house - 1][c] for c in range(num_colors) if c != color)
                         for color in range(num_colors)]
    # After the first house, dynamic programming does its magic: current house + the min of previous total

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


def common(A, B):
    """
    Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
    For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
    In this example, assume nodes with the same value are the exact same node objects.
    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
    """
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j] and A[i+1] == B[j+1]:
                return A[i]

print(common([0,9,1,2,4], [3,2,4]))


def classroom(lst):
    """
    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
    find the minimum number of rooms required.
    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
    :param lst: a list of tuples, each containing two integers
    :return: an int
    """
    import itertools

    for token in itertools.combinations(lst, 2):
        return sum(overlapping(a, b) for a, b in token)

def overlapping(a, b):
    return 1 if set(range(a, b)) & set(range(a, b)) else 0
    # set(range(a, b)).intersection(set(range(a, b)))

print(classroom([(30, 75), (0, 50), (60, 150)]))


def word_break(text, dictionary):
    """
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
    If there is more than one possible reconstruction, return any of them.
    If there is no possible reconstruction, then return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
    you should return ['the', 'quick', 'brown', 'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
    return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    :param text: a string of letters, without space
    :param dictionary: a list of strings
    :return: a list of strings
    """
    if not text or not dictionary:
        return [None]

    words = set(dictionary)
    memo = list()

    for i in range(len(text)+1):
        if text[:i] in words:
            memo.append(text[:i])       # append the found match
            words.remove(text[:i])      # shrink the dictionary
            memo += word_break(text[i:], words)         # repeat the process on the truncated text and shrunk dict
            # and append to MEMO
            break       # once A match is found, BREAK the loop!

    return memo


print(word_break("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))
assert word_break("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == ['the', 'quick', 'brown', 'fox']
assert word_break("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']) == ['bed', 'bath', 'and', 'beyond']










