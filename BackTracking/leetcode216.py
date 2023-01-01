class solution:
    def combinationSum3(self,k:int,n:int):
        res = []
        lst = [i  for i in range(1,10)]

        def dfs(i,curr,tot):
            
            if tot == n and len(curr) == k:
                res.append(curr.copy())
                return
            if  len(curr) > k or i>=len(lst) or tot > n:
                return
            curr.append(lst[i])
            dfs(i+1,curr,tot+lst[i])
            curr.pop()
            dfs(i+1,curr,tot)
        dfs(0,[],0)
        return res
        





x = solution()
print(x.combinationSum3(2,18))