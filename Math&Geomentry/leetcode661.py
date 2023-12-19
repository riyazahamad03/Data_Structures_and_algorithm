class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        rows, cols = len(img), len(img[0])
        directions = [
            [0, 0],
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
            [-1, 1],
            [1, -1],
            [-1, -1],
            [1, 1],
        ]

        def getVal(r, c):
            cnt = 9
            res = 0
            for dr, dc in directions:
                nR, nC = dr + r, dc + c
                if nR >= rows or nC >= cols or nR < 0 or nC < 0:
                    cnt -= 1
                else:
                    res += img[nR][nC]
            return res, cnt

        ans = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                val, cnt = getVal(r, c)
                ans[r][c] = val // cnt
        return ans


x = Solution()
print(x.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
