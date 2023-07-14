class solution:
    def maxProfit(self, prices: list[int]):
        l, r = 0, 1
        maxProfit = float("-inf")
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit


x = solution()
print(x.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
