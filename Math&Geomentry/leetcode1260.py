class solution:
    def shift2D(self, grid : list[list[int]], idex : int):
        m,n = len(grid),len(grid[0])
        
        def oneDim(r,c):
            return (r * n) + c
        
        def newPos(v):
            return [v//n , v%n]
        
        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                oneVal = (oneDim(i,j) + idex) % (m * n)
                nR,nC = newPos(oneVal)
                res[nR][nC] = grid[i][j]
        return res
    
x = solution()
print(x.shift2D([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]] , 4))


