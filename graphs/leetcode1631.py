import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def isValid(r, c):
            return (r >= 0 and c >= 0 and r < rows and c < cols)
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        minHeap = [[0, 0, 0]]
        dist[0][0] = 0

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while minHeap:
            cost, row, col = heapq.heappop(minHeap)

            if row == rows - 1 and col == cols - 1:
                return cost

            for dr, dc in directions:
                newR, newC = dr + row, dc + col
                if not isValid(newR, newC):
                    continue
                newEffort = max(
                    abs(heights[row][col] - heights[newR][newC]), dist[row][col])
                if newEffort < dist[newR][newC]:
                    dist[newR][newC] = newEffort
                    heapq.heappush(minHeap, [newEffort, newR, newC])
        # return -1


x = Solution()
print(x.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
