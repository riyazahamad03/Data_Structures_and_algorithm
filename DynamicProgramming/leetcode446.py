import collections


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += 1 + dp[j][diff]
        return res - (n * (n - 1) // 2)


x = Solution()
print(x.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
