class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []
        grid = [[0] * (n) for _ in range(m)]
        idx = 0
        for r in range(m):
            for c in range(n):
                grid[r][c] = original[idx]
                idx += 1

        return grid


x = Solution()
print(x.construct2DArray(original=[1, 2, 3], m=1, n=3))
