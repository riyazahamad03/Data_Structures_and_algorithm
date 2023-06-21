class solution:
    def minCost(self, nums: list[int], cost: list[int]):
        def calCost(base):
            Sum = 0
            for i, x in enumerate(nums):
                Sum += abs(base - x) * cost[i]
            return Sum
        l, r = min(nums), max(nums) + 1
        m = (l + r)//2
        while l < r:
            c1 = calCost(m)
            c2 = calCost(m + 1)

            if c1 < c2:
                r = m
            else:
                l = m + 1
            m = (l + r)//2
        return calCost(l)


x = solution()
print(x.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]))
