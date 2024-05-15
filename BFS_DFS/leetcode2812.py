import heapq
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def in_bounds(r, c):
            return min(r, c) >= 0 and max(r, c) < n

        min_dist = {}

        def pre_compute():
            q = deque()
            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            while q:
                r, c, dist = q.popleft()
                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for r2, c2 in nei:
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])
            return min_dist

        min_dist = pre_compute()
        max_heap = [(-min_dist[(0, 0)], 0, 0)]  # (dist , r ,c)
        visit = set()
        visit.add((0, 0))
        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = -dist
            if (r, c) == (n - 1, n - 1):
                return dist
            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for r2, c2 in nei:
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(max_heap, (-dist2, r2, c2))


x = Solution()
print(x.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
