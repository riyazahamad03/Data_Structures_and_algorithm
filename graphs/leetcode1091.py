import collections


class solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        q.append((0, 0, 1))
        visit = set((0, 0))
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def isValid(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 1:
                return False
            return True
        while q:
            for i in range(len(q)):
                r, c, length = q.popleft()
                if not isValid(r, c):
                    continue
                if r == ROWS-1 and c == COLS-1:
                    return length
                for dr, dc in directions:
                    if (r + dr, c + dc) not in visit:
                        q.append((r + dr, c + dc, length + 1))
                        visit.add((r + dr, c + dc))
        return -1


x = solution()
print(x.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
