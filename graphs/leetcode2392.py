from typing import List
from collections import defaultdict


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True

        def topo(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if src not in visit:
                    if not dfs(src, adj, visit, path, order):
                        return []  # Return an empty list if a cycle is detected
            return order[::-1]

        row_order = topo(rowConditions)
        col_order = topo(colConditions)

        if not row_order or not col_order:
            return []

        res = [[0] * k for _ in range(k)]

        val_to_row = {n: i for i, n in enumerate(row_order)}
        val_to_col = {n: i for i, n in enumerate(col_order)}

        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num

        return res


x = Solution()
print(
    x.buildMatrix(k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]])
)
