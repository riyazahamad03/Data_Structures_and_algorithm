class solution:
    def dailyTemp(self , temperatures : list[int])-> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idex , val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                sIdex , sVal = stack.pop()
                ans[sIdex] = idex - sIdex
            stack.append([idex , val])
        return ans
x = solution()
print(x.dailyTemp([73,74,75,71,69,72,76,73]))