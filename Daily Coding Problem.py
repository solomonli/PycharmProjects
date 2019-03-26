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
        a helper function that will be return the numbers of decoding of the last K digits of sub_string
        it will be run recursively in the main function
        :param sub_string: a str, the input string
        :param k: an integer, the last K digits of sub_string
        :return:
        """
        if k == 0:
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

    if k == 0:
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

import datetime


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


tik = datetime.datetime.now()

print(LCS('Jeez I am waiting for snow.', "Jeez I've been waiting for snow.", 0, 0))

tok = datetime.datetime.now()

print(tok - tik)


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

