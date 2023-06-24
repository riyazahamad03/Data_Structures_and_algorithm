class solution:
    def tallestBillboard(self, rods: list[int]):
        dp = {}

        def dfs(i, diff):
            if i == len(rods):
                if diff == 0:
                    return 0
                return float("-inf")

            if (i, diff) in dp:
                return dp[(i, diff)]

            dp[(i, diff)] = max(dfs(i + 1, diff), dfs(i + 1,
                                                      rods[i] + diff), rods[i] + dfs(i + 1, diff - rods[i]))
            return dp[(i, diff)]

        return dfs(0, 0)


x = solution()
print(x.tallestBillboard([1, 2, 3, 6]))
