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


def cdr(f):
    def right(a, b):
        return b

    return f(right)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, 
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to 
get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

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
    :param l: an integer - the length of list lst minus one
    :return: an integer
    """
    if l == 0:
        return lst[0]

    if l == 1:
        return max(lst[0], lst[1])

    return max(max_sum(lst, l - 2) + lst[l], max_sum(lst, l - 1))


print(max_sum([5, 1, 1, 5], 3))

