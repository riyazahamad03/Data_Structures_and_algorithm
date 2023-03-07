class solution:
    def subSet(self,nums:list[int]):
        res=[]
        sub = []
        def dfs(i):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            # recursively on left subSet
            dfs(i + 1)
            # recursively on right subSet
            sub.pop()
            dfs(i + 1)
        dfs(0)
        return res
x = solution()
print(x.subSet([1,2,3]))