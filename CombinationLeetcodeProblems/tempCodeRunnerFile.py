import collections


class solution:
    def canCross(self, row: int, col: int,  cells: list[list[int]], days: int):
        q = collections.deque()
        grid = [[0] * col for _ in range(row)]
        visit = set()

        for i in range(days):
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1

        for idx in range(col):
            if not grid[0][idx]:
                q.append((0, idx))
                visit.add((0, idx))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nR, nC = r + dr, c + dc
                    if 0 <= nR < row and 0 <= nC < col and grid[nR][nC] == 0 and (nR, nC) not in visit:
                        q.append((nR, nC))
                        visit.add((nR, nC))
        return False

    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]):
        l, r = 1, (row * col)
        while l < r:
            mid = (l + r)//2
            if self.canCross(row, col, cells, mid):
                l = mid
            else:
                r = mid - 1
        return l


x = solution()
print(x.latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))

x = solution()
print(x.latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]]))

x = solution()
print(x.latestDayToCross(row=3, col=3, cells=[[1, 2], [2, 1], [
      3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]))
