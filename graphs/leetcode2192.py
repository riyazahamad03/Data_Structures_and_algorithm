from typing import List
from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        adj_list = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1

        ancestors = [set() for _ in range(n)]

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:

                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result


x = Solution()
print(
    x.getAncestors(
        8,
        [
            [0, 3],
            [0, 4],
            [1, 3],
            [2, 4],
            [2, 7],
            [3, 5],
            [3, 6],
            [3, 7],
            [4, 6],
        ],
    )
)
