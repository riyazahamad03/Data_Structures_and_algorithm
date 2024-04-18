import collections
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = collections.defaultdict(list)

        for i, v in enumerate(edges):
            adj[v[0]].append([succProb[i], v[1]])
            adj[v[1]].append([succProb[i], v[0]])

        maxHeap = [[-1, start_node]]

        visit = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            visit.add(node)
            if node == end_node:
                return -1 * prob
            for neiVal, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(maxHeap, (prob * neiVal, nei))

        return 0


x = Solution()
print(
    x.maxProbability(
        n=3,
        edges=[[0, 1], [1, 2], [0, 2]],
        succProb=[0.5, 0.5, 0.2],
        start_node=0,
        end_node=2,
    )
)
