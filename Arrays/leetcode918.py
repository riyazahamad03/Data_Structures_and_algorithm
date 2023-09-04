# Kadene's algorithm
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        globalMax = globalMin = nums[0]
        currMax = currMin = 0
        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, 0)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return max(globalMax, sum(nums) - globalMin) if globalMax > 0 else globalMax


x = Solution()
print(x.maxSubarraySumCircular([1, -2, 3, -2]))
