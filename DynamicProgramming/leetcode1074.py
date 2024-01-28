from typing import List
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        sub_sum = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                topleft = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0

                sub_sum[r][c] = matrix[r][c] + top + left - topleft

        res = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                count = defaultdict(int)
                count[0] = 1

                for c1 in range(cols):
                    curr = sub_sum[r2][c1] - (sub_sum[r1 - 1][c1] if r1 > 0 else 0)
                    diff = curr - target
                    res += count[diff]
                    count[curr] += 1
        return res


x = Solution()
print(x.numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
