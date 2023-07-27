class solution:
    def maxRunTime(self, n, batteries):
        l, r = 1, sum(batteries)
        while l < r:
            m = r - (r - l)//2
            extra = 0
            for bat in batteries:
                extra += min(bat, m)
            if extra >= n * m:
                l = m
            else:
                r = m - 1
        return l


x = solution()
print(x.maxRunTime(n=2, batteries=[1, 1, 1, 1]))
print(x.maxRunTime(n=2, batteries=[3, 3, 3]))
