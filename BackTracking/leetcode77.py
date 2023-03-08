class solution:
    def combine(self,n:int,k:int):
        res = []
        def backTracking(start , combination):
            if len(combination) == k:
                res.append(combination.copy())
                return
            for i in range(start , n + 1):
                combination.append(i)
                backTracking(i + 1, combination)
                combination.pop()
        backTracking(1 , [])
        return res
x = solution()
print(x.combine(4,2))