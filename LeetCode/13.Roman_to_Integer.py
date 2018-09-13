class Solution:

    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToDecimal(self, s):
        res = 0     # res stands for 'result'
        i = 0

        while i < len(s):   # while i still in the range

            # Getting value of symbol s[i]
            s1 = self.value[s[i]]

            if i+1 < len(s):

                # Getting value of symbol s[i+1]
                s2 = self.value[str(s[i+1])]

                # Comparing both values
                if s1 >= s2:

                    # Value of current symbol is greater or equal to the next symbol
                    res += s1
                    i += 1
                else:

                    # Value of current symbol is greater or equal to the next symbol
                    res = res + s2 - s1
                    i += 2
            else:
                res += s1
                i += 1

        return res


if __name__ == '__main__':
    print("Integer form of Roman Numeral is ", end='')
    print(Solution().romanToDecimal("MCMIV"))
