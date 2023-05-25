class solution:
    def new21GameUsingRecursion(self, n: int, k: int, maxPts: int):
        cache = {}

        def dfs(score):
            if score >= k:
                return 1 if score <= n else 0
            if score in cache:
                return cache[score]
            prob = 0
            for idex in range(1, maxPts + 1):
                prob += dfs(idex + score)
            cache[score] = prob / maxPts
            return cache[score]
        return dfs(0)

    def new21GameLinearSolution(self, n: int, k: int, maxPts: int):
        if k == 0:
            return 1.0
        cache = {}
        windowSum = 0
        for i in range(k, k + maxPts):
            if i <= n:
                windowSum += 1
        for i in range(k-1, -1, -1):
            cache[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = cache.get(i + maxPts, 1)
            windowSum = cache[i] - remove
        return cache[0]


x = solution()
print(x.new21GameUsingRecursion(21, 17, 10))
print(x.new21GameLinearSolution(21, 17, 10))
