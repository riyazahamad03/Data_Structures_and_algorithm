class solution:
    def arraySign(self,nums : list[int]):
        negCount = 0
        for idx in nums:
            if idx == 0:
                return 0
            negCount += 1 if idx < 0 else 0

        return 1 if not negCount%2 else -1
x = solution()
print(x.arraySign([-1,-2,-3,-4,3,2,1]))