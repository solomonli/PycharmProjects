class Solution:

    def twosum(self, nums, target):
        if len(nums) <= 1:
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                print(d)
                return tuple([d[nums[i]], i])
            else:
                d[target - nums[i]] = i
                print(d)


if __name__ == "__main__":
    # print(twosum([2, 7, 18, 3, 100], 102))
    print(Solution().twosum([2, 7, 18, 3, 100], 101))
