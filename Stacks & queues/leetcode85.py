class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        areaMax = 0
        stack = []

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                areaMax = max(areaMax, height * (i - index))

                startIndex = index
            stack.append((startIndex, h))

        for i, h in stack:
            areaMax = max(areaMax, h * (len(heights) - i))

        return areaMax

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = float("-inf")
        grid = [[0] * (cols) for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    if r > 0:
                        grid[r][c] = 1 + grid[r - 1][c]
                    else:
                        grid[r][c] = 1
        for row in grid:
            res = max(res, self.largestRectangleArea(row))
        return res


x = Solution()
print(
    x.maximalRectangle(
        matrix=[
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
