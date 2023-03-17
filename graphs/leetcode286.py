import collections
class solution:
    def wallsAndGates(self , rooms : list[list[int]]):
        visitSet = set()
        ROWS,COLS = len(rooms) , len(rooms[0])
        q = collections.deque()
        def roomsAdd(r , c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or (r , c) in visitSet or rooms[r][c] == -1):
                return
            visitSet.add((r , c))
            q.append([r , c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visitSet.add((r , c))
                    q.append([r , c])

        d = 0
        directions = [[1 , 0] , [0 , 1] , [0 , -1] , [-1 , 0]]
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                rooms[r][c] = d
                for dr,dc in directions:
                    roomsAdd(r  + dr , c + dc)
            d += 1
        return rooms
x = solution()
print(x.wallsAndGates([['inf' , -1 , 0 , 'inf'] , ['inf' , 'inf' , 'inf' , -1] , ['inf' , -1 , 'inf' , -1] , [0 , -1 ,'inf' , 'inf']]))