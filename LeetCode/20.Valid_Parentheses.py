'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}  # make the left component as the searchable key
        for element in s:
            if element in lookup:
                stack.append(element)
                ## print(stack), print(element)
                # [] becomes richer, containing only left components
            elif len(stack) == 0 or lookup[stack.pop()] != element:  # else: where a right component appears
                # if empty [] (nothing added before), or stack.pop() != THE element, which ensure ')' right after
                # '(' rather than ']' after '('
                # btw, pop() fetches the item and clears the list -- one stone hits two birds
                ##print(stack), print(element)
                return False
        return len(stack) == 0


if __name__ == "__main__":
    # print(Solution().isValid("()[]{}"))
    print(Solution().isValid("()[{]}"))
