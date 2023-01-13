# 695. Max Area of Island
class solution:
    def maxAreaOfIsland(self,grid:list[list[int]]):
        rows,cols = len(grid),len(grid[0])
        visitSet = set()
        def maxArea(i,j):
            if i>=rows or j>=cols or i<0 or j<0 or grid[i][j]==0 or (i,j) in visitSet:
                return 0
            visitSet.add((i,j))
            return (
                1 + maxArea(i+1,j) +
                maxArea(i-1,j) +
                maxArea(i,j+1) +
                maxArea(i,j-1)
            )
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    res = max(res,maxArea(r,c))
        return res
x = solution()
print(x.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))