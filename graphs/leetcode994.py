# 994. Rotting Oranges
import collections
class solution:
    def orangesRotting(self , grid:list[list[int]]):
        Queue = collections.deque()
        time,freshOranges = 0,0
        ROWS,COLS = len(grid),len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                if grid[r][c] == 2:
                    Queue.append([r , c])

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while Queue and freshOranges > 0:
            for i in range(len(Queue)):

                row,col = Queue.popleft()
                for dr,dc in directions:
                    if (dr + row < 0 or 
                        dc + col < 0 or
                        dr + row >= ROWS or
                        dc + col >= COLS or
                        grid[dr + row][dc + col] != 1):

                        continue

                    grid[dr + row][dc + col] = 2
                    freshOranges -= 1
                    Queue.append([dr + row , dc + col])
            
            time += 1
        return time if freshOranges == 0 else -1
x = solution()
print(x.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))