class solution:
    def maxProfit(self, prices: list[int]):
        dp = {}
        def dfs(idex, buy):
            if idex >= len(prices):
                return 0
            if (idex, buy) in dp:
                return dp[(idex, buy)]
            cool = dfs(idex + 1, buy)
            if buy:
                buying = dfs(idex + 1 , not buy) - prices[idex]
                dp[(idex, buy)] = max(buying, cool)
            else:
                selling = dfs(idex + 2, not buy) + prices[idex]
                dp[(idex, buy)] = max(selling, cool) 
            return dp[(idex, buy)]
        return dfs(0, True)


x = solution()
# print(x.maxProfit([1, 2, 3, 0, 2]))
print(x.maxProfit([1]))
