# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):   # 1st word's length sets the range
            for string in strs[1:]:     # each one in the rest words
                if i >= len(string) or string[i] != strs[0][i]:
                    # if the i meets the 2nd word's length, or Xth letter of 2nd word != Xth letter of 1st word
                    return strs[0][:i]
                    # return X-index-so-far of 1st word
        return strs[0]
        # if there's no early exit, the 1st word is the common


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["helloa", "helloheaven", "helloheavy"]))
