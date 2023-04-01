class solution:
    def findOrder(self , numCourses : int , prerequisites : list[list[int]]):
        cycle , visit = set() , set()
        preReq , res ={i : [] for i in range(numCourses)} , []
        for crs,pre in prerequisites:
            preReq[crs].append(pre)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            
            for c in preReq[crs]:
                if not dfs(c):
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for idex in range(numCourses):
            if not dfs(idex):
                return []
        return res
x = solution()
print(x.findOrder(4 , [[1,0],[2,0],[3,1],[3,2]]))