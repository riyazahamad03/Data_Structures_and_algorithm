from collections import deque


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows, cols = len(land), len(land[0])
        res = []

        def processLand(r, c):
            q = deque([(r, c)])
            land[r][c] = 0
            top_left = (r, c)
            bottom_right = (r, c)
            while q:
                R, C = q.popleft()
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    newR, newC = R + dr, C + dc
                    if 0 <= newR < rows and 0 <= newC < cols and land[newR][newC] == 1:
                        q.append((newR, newC))
                        land[newR][newC] = 0
                        bottom_right = (
                            max(bottom_right[0], newR),
                            max(bottom_right[1], newC),
                        )
            return [top_left[0], top_left[1], bottom_right[0], bottom_right[1]]

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    res.append(processLand(r, c))

        return res


x = Solution()
print(x.findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
