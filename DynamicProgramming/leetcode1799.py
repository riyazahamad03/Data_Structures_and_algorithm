import collections
import math


class solution:
    def maxScore(self, nums: list[int]):
        dp = collections.defaultdict(int)

        def dfs(mask, op):
            if mask in dp:
                return dp[mask]
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                    newMask = mask | 1 << i | 1 << j
                    Score = op * math.gcd(nums[i], nums[j])
                    dp[mask] = max(dp[mask], Score + dfs(newMask, op + 1))
            return dp[mask]
        return dfs(0, 1)


x = solution()
print(x.maxScore([3, 4, 6, 8]))

# time Complexity (O(n * 2) * 2^n) * O(log n)