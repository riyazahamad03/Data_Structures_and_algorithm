class solution:
    def closedIsland(self , grid : list[list[int]]):
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        def dfs(r , c):
            if r < 0 or r >= rows or c < 0 or c>=cols:
                return 0
            if grid[r][c] == 1 or (r,c) in visit:
                return 1
            visit.add((r , c))
            return min(dfs(r + 1 , c) ,
                       dfs(r - 1 , c) ,
                       dfs(r , c + 1) ,
                       dfs(r , c - 1) )
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1 and (r , c) not in visit:
                    res += dfs(r , c)
        return res
x = solution()
print(x.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))