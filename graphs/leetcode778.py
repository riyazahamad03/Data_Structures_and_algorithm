import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visit = set([(0, 0)])

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in direc:
                newR, newC = dr + r, dc + c
                if (
                    newR < 0
                    or newC < 0
                    or newR >= n
                    or newC >= n
                    or (newR, newC) in visit
                ):
                    continue
                visit.add((newR, newC))
                heapq.heappush(minHeap, (max(t, grid[newR][newC]), newR, newC))


x = Solution()
print(x.swimInWater([[0, 2], [1, 3]]))
