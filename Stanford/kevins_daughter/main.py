# Find at least 40 sets of five distinct unit fractions that add up to 1.
# An example (a set of three items) would be 1/2 + 1/3 + 1/6 = 1.
# A great math puzzle from Kevin's daughter

import time
import itertools


class Solution(object):

    def five_unit_fraction(self):

        tic = time.time()

        a = range(2, 99)
        index = 0
        for i in list(itertools.combinations(a, 5)):
            if i[0]*i[1]*i[2]*i[3]*i[4] == \
                    i[1]*i[2]*i[3]*i[4] +\
                    i[0]*i[2]*i[3]*i[4] +\
                    i[0]*i[1]*i[3]*i[4] +\
                    i[0]*i[1]*i[2]*i[4] +\
                    i[0]*i[1]*i[2]*i[3]:
                print(i)
                index += 1

        toc = time.time()

        print("list length = " + str(index))
        print("time consumed = " + str(toc - tic) + " seconds")


if __name__ == "__main__":
    print(Solution().five_unit_fraction())
