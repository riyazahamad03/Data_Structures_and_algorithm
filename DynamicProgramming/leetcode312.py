import collections


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        dp = collections.defaultdict(int)

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            for i in range(l, r + 1):
                cnt = nums[l - 1] * nums[i] * nums[r + 1]
                cnt += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], cnt)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


x = Solution()
print(x.maxCoins([3, 1, 5, 8]))
