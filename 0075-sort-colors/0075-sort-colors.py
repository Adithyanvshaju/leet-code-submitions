class Solution(object):
    def sortColors(self, nums):
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)

        nums[:] = [0] * zeros + [1] * ones + [2] * twos


nums = [2, 0, 2, 1, 1, 0]

obj = Solution()
obj.sortColors(nums)

print(nums)