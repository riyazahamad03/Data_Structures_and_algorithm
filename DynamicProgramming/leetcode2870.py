import collections


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        maxN = max(count.values())

        dp = [float("inf")] * (maxN + 2)
        dp[0] = 0

        for i in range(2, maxN + 2):
            v = float("inf")
            if i - 2 >= 0:
                v = min(v, dp[i - 2])
            if i - 3 >= 0:
                v = min(v, dp[i - 3])
            dp[i] = 1 + v
        res = 0
        for c in count:
            res += dp[count[c]]
        return res if res != float("inf") else -1


x = Solution()
print(x.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
