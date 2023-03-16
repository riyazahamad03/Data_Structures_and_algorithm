class solution:
    def getConcatenation(self,nums:list[int]):
        res = []
        for i in range(2):
            for n in nums:
                res.append(n)
        return res

x = solution()
print(x.getConcatenation([11,2,21,1]))