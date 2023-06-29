import collections


class solution:
    def shortestPathAllKeys(self, grid: list[str]):
        m, n = len(grid), len(grid[0])

        q = collections.deque()
        totKeys = 0
        keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        locks = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    q.append((i, j, 0, 0))
                elif grid[i][j] in keys:
                    totKeys += 1
        visit = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, - 1]]
        while q:
            for _ in range(len(q)):
                i, j, found, step = q.popleft()
                curr = grid[i][j]
                if curr in locks and not (found >> locks[curr]) & 1 or curr == '#':
                    continue
                if curr in keys:
                    found |= 1 << keys[curr]
                    if found == (1 << totKeys)-1:
                        return step
                for dr, dc in directions:
                    newR, newC = dr + i, dc + j
                    if 0 <= newR < m and 0 <= newC < n and (newR, newC, found) not in visit:
                        visit.add((newR, newC, found))
                        q.append((newR, newC, found, step + 1))
        return -1


x = solution()
print(x.shortestPathAllKeys(["@.a..", "###.#", "b.A.B"]))

print(1 >> 2)