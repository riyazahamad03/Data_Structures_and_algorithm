class solution:
    def singleNumber(self , nums : list[int]):
        res = 0
        for i in nums:
            res ^= i 
        return res
x = solution()
print(x.singleNumber([4 , 1 , 2 , 1 , 2]))