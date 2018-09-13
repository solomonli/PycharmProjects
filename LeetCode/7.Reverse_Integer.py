class Solution:

    def rvs(self, x):
        if abs(x) >= 2**32-1:
            return False
        else:
            return int(str(x)[::-1])


if __name__ == "__main__":
    print(Solution().rvs(2432535349))
