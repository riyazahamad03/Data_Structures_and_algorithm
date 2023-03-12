class solution:
    def subsetUnique(self , nums:list[int]):
        res = []
        subset = []

        def dfsBacktrack(idex):
            if idex == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idex])
            dfsBacktrack(idex + 1)
            subset.pop()
            while idex + 1 < len(nums) and nums[idex] == nums[idex + 1]:
                idex += 1
            dfsBacktrack(idex + 1)
        dfsBacktrack(0)
        return res
x = solution()
print(x.subsetUnique([1,2,2]))