import collections
class solution:
    def walls_and_gate(self,rooms:list[list[int]]):
        ROWS,COLS = len(rooms),len(rooms[0])
        q = collections.deque()
        visit = set()
        
        def visitRoom(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or rooms[r][c] == -1):
                return
            q.append([r,c])
            visit.add((r,c))


        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        roomDist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = roomDist

                visitRoom(r + 1, c)
                visitRoom(r - 1 , c)
                visitRoom(r , c + 1)
                visitRoom(r , c - 1)
            roomDist += 1
        return rooms
            
x = solution()
print(x.walls_and_gate([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))