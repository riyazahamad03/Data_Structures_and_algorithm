class Solution:
    def maxProfit(self, prices: list[int], fee: int):
        dp = {}

        def dfs(idx,  isBought):
            if (idx, isBought) in dp:
                return dp[(idx, isBought)]
            if idx == len(prices):
                return 0

            if not isBought:
                dp[(idx, isBought)] = max(dfs(idx + 1, not isBought) -
                                          prices[idx] - fee, dfs(idx + 1, isBought))
                return dp[(idx, isBought)]
            if isBought:
                dp[(idx, isBought)] = max(dfs(idx + 1, not isBought) +
                                          prices[idx], dfs(idx + 1, isBought))
                return dp[(idx, isBought)]
        return dfs(0, False)


x = Solution()
print(x.maxProfit([1, 3, 7, 5, 10, 3], fee=3))
