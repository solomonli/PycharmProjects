class Solution:

    def first(self, word):
        return str(word)[0]

    def last(self, word):
        return str(word)[-1]

    def middle(self, word):
        return str(word)[1:-1]

    def isPalindrome(self, x):
        if len(str(x)) <= 1:
            return True

        if self.first(x) != self.last(x):
            return False

        else:
            return self.isPalindrome(self.middle(x))


if __name__ == "__main__":
    print(Solution().isPalindrome(1234567890987654321))

'''
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s
'''
