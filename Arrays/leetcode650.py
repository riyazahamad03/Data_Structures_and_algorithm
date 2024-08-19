class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}

        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000

            if (count, paste) in cache:
                return cache[(count, paste)]

            res1 = 1 + helper(count + paste, paste)
            res2 = 2 + helper(count + count, count)

            cache[(count, paste)] = min(res1, res2)

            return min(res1, res2)

        if n == 1:
            return 0
        return 1 + helper(1, 1)


x = Solution()
print(x.minSteps(n=3))
