class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prevRow = [poured]

        for row in range(1, query_row + 1):
            curr = [0]*(row + 1)
            for i in range(row):
                extra = prevRow[i] - 1
                if extra > 0:
                    curr[i] += extra * 0.5
                    curr[i + 1] += extra * 0.5
            prevRow = curr
        return min(1, prevRow[query_glass])


x = Solution()
print(x.champagneTower(poured=1, query_row=1, query_glass=1))
