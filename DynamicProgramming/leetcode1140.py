class solution:
    def stoneGameII(self , piles : list[int]):
        dp = {}
        def dfs(alice , i , m):
            if i == len(piles):
                return 0
            if (alice , i , m) in dp:
                return dp[(alice , i , m)]

            res = 0 if alice else float("inf")
            tot = 0
            for x in range(1 , 2 * m + 1):
                if i + x > len(piles):
                    break
                tot += piles[i + x-1]

                if alice:
                    res = max(res , tot + dfs(not alice , i + x , max(x , m)))
                else:
                    res = min(res , dfs(not alice , i + x , max(m , x)))
            dp[(alice , i , m)] = res
            return res
        return dfs(True , 0 , 1)
x = solution()
print(x.stoneGameII([2,7,9,4,4]))