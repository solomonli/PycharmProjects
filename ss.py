def wall_tile(matrix, start, end):
    """
    You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
    Each False boolean represents a tile you can walk on.

    Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required
    to reach the end coordinate from the start. If there is no possible path, then return null.
    You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:
    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]

    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required
    to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
    :param matrix: a list of lists containing booleans
    :param start: a tuple of two integers - zero-based indices
    :param end: a tuple of two integers - zero-based indices
    :return: an integer
    """
    num_row, num_column = len(matrix), len(matrix[0])

    if max(start[0], end[0]) > num_row - 1 or max(start[1], end[1]) > num_column - 1:
        return 'The start or end point is out of boundary!'

    board = [[(i, j) for j in range(num_column)] for i in range(num_row)]

"""
Implement locking in a binary tree. A binary tree node can be locked or 
unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.
"""


def reg_exp(string):
    """
    Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

    That is, implement a function that takes in a string and a valid regular expression
    and returns whether or not the string matches the regular expression.

    For example, given the regular expression "ra." and the string "ray", your function should return true.
    The same regular expression on the string "raymond" should return false.

    Given the regular expression ".*at" and the string "chat", your function should return true.
    The same regular expression on the string "chats" should return false.
    :param string: a string containing '.', '*', or both
    :return: a boolean
    """


def remove_item(lst, k):
    """
    Given a singly linked list and an integer k, remove the kth last element from the list.
    k is guaranteed to be smaller than the length of the list.

    The list is very long, so making more than one pass is prohibitively expensive.

    Do this in constant space and in one pass.
    :param lst: a list
    :param k: an integer
    :return: the processed the list
    """
    # Use fast and slow pointers. The fast pointer is n steps ahead of the slow pointer.
    # When the fast reaches the end, the slow pointer points at the previous element of the target element.
    # while (fast.next != null) in Java ???
    # fast =

"""
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. 
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, 
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def coding_problem_29(text):
    """
    Run-length encoding is a fast and simple method of encoding strings.
    The basic idea is to represent repeated successive characters as a single count and character.
    For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

    Implement run-length encoding and decoding. You can assume the string to be encoded have no digits
    and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
    :param text: a string
    :return: a string
    """
    if text.isalpha():  # no numbers, encode

        encoded = ''
        # idx = 0
        while text:

            idx = 0     # the beauty lies here too: you dont need the other two idx = 0

            while idx < len(text) and text[0] == text[idx]:
                idx += 1

            encoded += str(idx) + text[0]

            text = text[idx:]
            # idx = 0
        return encoded

    else:  # decode

        return ''.join(c * int(n) for n, c in zip(text[::2], text[1::2]))


print(coding_problem_29('AAABBBFFFFFFFDDDDD'))

import json, pprint

x = """{
  "data": {
    "translations": [
      {
        "translatedText": "THE PUBLIC GOOD the despatches For Obama, the mustard is from Dijon",
        "detectedSourceLanguage": "fr"
      }
    ]
  }
}"""

y = json.loads(x)

pprint.pprint(y)


"""def run_length_encode(string):
    res = ''

    for i in range(len(string)):
        if string[i] != string[i+1]:
            res += count_same(string[:i+1])
            string = string[i+1:]
            res += run_length_encode(string)
            break

    return res

def count_same(text):
    return str(len(text)) + text[0]

print(run_length_encode('AABBCCCDD'))
"""


