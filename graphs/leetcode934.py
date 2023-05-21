import collections


class solution:
    def shortestBridge(self, grid: list[list[int]]):
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def inValidPath(r, c):
            return r >= n or c >= n or r < 0 or c < 0

        visit = set()

        def dfs(r, c):
            if (r, c) in visit or inValidPath(r, c) or not grid[r][c]:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            res,  q = 0, collections.deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        if inValidPath(r + dr, c + dc) or (r + dr, c + dc) in visit:
                            continue
                        if grid[r + dr][c + dc]:
                            return res
                        visit.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))
                res += 1
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    dfs(row, col)
                    return bfs()


x = solution()
print(x.shortestBridge([[0, 1], [1, 0]]))
print(x.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
print(x.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
      1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))
