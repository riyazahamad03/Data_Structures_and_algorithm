# 463. Island Perimeter
class solution:
    def islandPerimetre(self,grid:list[list[int]]):
        row,col = len(grid),len(grid[0])
        visitSet = set()
        def dfs(i,j):
            if i>=row or j>=col or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visitSet:
                return 0
            visitSet.add((i,j))
            p =  dfs(i+1,j)
            p += dfs(i-1,j)
            p += dfs(i,j+1)
            p += dfs(i,j-1)
            return p
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return dfs(i,j)
x = solution()
print(x.islandPerimetre([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))