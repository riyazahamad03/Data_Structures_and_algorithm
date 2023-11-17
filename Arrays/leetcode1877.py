class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l < r:
            res = max(res, nums[l] + nums[r])
            l, r = l + 1, r - 1
        return res


x = Solution()
print(x.minPairSum([3, 5, 4, 2, 4, 6]))
