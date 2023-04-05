import collections
class solution:
    def shortestPathBinaryMatrix(self , grid : list[list[int]]):
        ROWS,COLS = len(grid) , len(grid[0])
        q = collections.deque([(0 , 0 , 1)]) #[row , col , length]
        visit = set((0 , 0))
        directions = [[1 , 0],[0 , 1],[0 , -1],[-1 , 0],
                      [1 , 1],[1 , -1],[-1, 1],[-1 , -1]]
        while q:
            row,col,length = q.popleft()
            if(row < 0 or row >= ROWS or col < 0 or col >=COLS or grid[row][col]==1):
                continue
            if row == ROWS-1 and col==COLS-1:
                return length
            for dr , dc in directions:
                r,c = row+dr , col + dc
                if((r,c) not in visit and r in range(ROWS) and c in range(COLS)): #row and col checking is not necessary because we are ignoring in the above if condition
                    visit.add((r,c))
                    q.append((r , c , length + 1))
        return -1
x = solution()
print(x.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))