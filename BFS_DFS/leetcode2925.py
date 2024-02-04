import collections
from typing import List


class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        adj = collections.defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(node, par):
            if len(adj[node]) == 1 and node != 0:
                return values[node]
            s = 0
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    s += dfs(nei, node)
            return min(s, values[node])

        visit = set()
        return sum(values) - dfs(0, 0)


x = Solution()
print(
    x.maximumScoreAfterOperations(
        edges=[[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values=[5, 2, 5, 2, 1, 1]
    )
)
