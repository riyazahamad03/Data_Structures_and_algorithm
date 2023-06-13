class solution:
    def equalPairs(self, grid: list[list[int]]):
        n = len(grid)
        res, resMap = 0, {}

        for row in grid:
            resMap[tuple(row)] = 1 + resMap.get(tuple(row), 0)

        for r in range(n):

            elems = []
            for c in range(n):
                elems.append(grid[c][r])

            elems = tuple(elems)
            if elems in resMap:
                res += resMap[elems]
        return res


x = solution()
print(x.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(x.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
