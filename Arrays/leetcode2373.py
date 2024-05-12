from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[-1] * (n - 2) for _ in range(n - 2)]
        for r in range(n - 2):
            for c in range(n - 2):
                mx = float("-inf")
                for l in range(3):
                    for m in range(3):
                        mx = max(mx, grid[r + l][c + m])
                res[r][c] = mx
        return res


x = Solution()
print(x.largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
