import sys
sys.setrecursionlimit(10**6)
class Solution:

    def maximizeTheCuts(self, n, x, y, z):
        cache = {}

        def dfs(avai):
            if avai <= 0:
                return 0

            if avai in cache:
                return cache[avai]

            a, b, c = float("-inf"), float("-inf"), float("-inf")

            if avai >= x:
                a = 1 + dfs(avai - x)

            if avai >= y:
                b = 1 + dfs(avai - y)

            if avai >= z:
                c = 1 + dfs(avai - z)

            cache[avai] = max(a, b, c)
            return cache[avai]

        result = dfs(n)
        return result if result > 0 else 0
x = Solution()
print(x.maximizeTheCuts(9 , 2 , 2 , 2))